import StringIO
import json
import logging
import random
import urllib
import urllib2



# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

TOKEN = 'API TOKEN'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'



class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)


# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False


# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        try:
            message = body['message']
        except:
            message = body['edited_message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']
        first_name = fr.get('first_name')

        if not text:
            logging.info('no text')
            return

        def reply(msg=None):
            resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                'chat_id': str(chat_id),
                'text': msg.encode('utf-8', 'strict'),
                'disable_web_page_preview': 'true',
                'reply_to_message_id': str(message_id),
            })).read()

            logging.info('send response:')
            logging.info(resp)

        def send(msg=None):
            resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                'chat_id': str(chat_id),
                'text': msg.encode('utf-8', 'strict'),
                'disable_web_page_preview': 'true',
            })).read()

            logging.info('send response:')
            logging.info(resp)
        # COMMANDS
        if text.startswith('/'):
            if '/start' in text:
                reply('Bot enabled')
                setEnabled(chat_id, True)
            elif '/stop' in text:
                reply('Bot disabled')
                setEnabled(chat_id, False)
            elif '/help' in text:
                # CUTOMISE FROM HERE
                send('I\'m a bot')
            elif '/roll' in text:
                send(first_name + ' rolled a die and got ' + str(random.randrange(1,7)))
            else:
                reply('What command?' + u'\U0001F615')
        # MESSAGES
        # CUSTOMISE FROM HERE
        elif 'who are you' in text.lower():
            reply('I am a bot.\nFor more information type /help.')
        elif 'hello' in text.lower():
            send('Hello ' + first_name)
        elif 'hi' in text.lower():
            send('Hi')
        else:
            if getEnabled(chat_id):
                sendWithEmoji('I don\'t understand ' + u'\U0001F615')
            else:
                logging.info('not enabled for chat_id {}'.format(chat_id))


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
