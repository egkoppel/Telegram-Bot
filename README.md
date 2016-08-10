# Telegram-Bot
How to create a bot for Telegram

## Set the bot up in Telegram
1. Set up a Telegram account if you haven't got one already
  - Go to the [Telegram website](https://web.telegram.org/)
  - Follow the instructions to set up an account
2. Open a chat with `@BotFather` or go to [telegram.me/botfather](telegram.me/botfather)
3. Click start if prompted to, and enter `/newbot`
4. BotFather should reply 'Alright, a new bot. How are we going to call it? Please choose a name for your bot.'
5. Enter a name for your bot
6. BotFather should then ask what your bot's username will be. Enter a username ending in `bot`
7. If the username hasn't been taken, BotFather will give you an API token
8. You can then set a description for the bot and add a picture. See the wiki page for more
9. Now you will need to set up some commands like `/help`. To do this send `/setcommands` to BotFather. He will prompt you for a bot and then tell you to format one command per line. By default, to type a new line press `shift + enter`

## Download the code
1. Click the green download button and download the files as a .zip and unzip them
2. Open `main.py` and change the line that says
```Python
TOKEN = 'API TOKEN'
```
to
```Python
TOKEN = 'whatever your api token from BotFather is'
```

## Set up the project in Google Cloud Console
1. Go to the [Google Cloud Console](console.cloud.google.com)
2. Click create new project, and enter your bot's name
	- Underneath the name it should show a project id
	- Note this id down somewhere
3. Create the project
4. In `app.yaml` change the line that says
```YAML
application: project id
```
to
```YAML
application: the project id from step 2
```

## Download and setup Google App Engine Launcher
1. Download the [Google App Engine for Python](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
	- Download it
	- Install it
	- Open it
2. Choose `File/Add Existing Application` and in the path box, browse to the `Code` folder
3. Click Add
4. In the main screen, select it (It should have the project id you entered under name) and choose `Deploy`
5. It will then open up a log of the deployment

## Testing
1. In a browser go to `https://project-id.appspot.com/me` replacing project-id with your Google Project ID
2. Once it has loaded, it should come up with a JSON file like this
```JSON
{
	"ok":true,
	"result":{
		"id":123456789,
		"first_name":"My Bot",
		"username":"SomeBot"
	}
}
```
3. Once that has succeeded, go to the URL `https://project-id.appspot.com/set_webhook?url=https://project-id.appspot.com/webhook` replacing both instances of project-id with your Google Project ID
4. It should then say `Webhook was set`
5. Now in Telegram, open a chat with your bot. You can do this by either searching for `@bot-username` or going to `telegram.me/bot-username`, replacing `bot-username` with your bot's username
6. It should then show up with a start button. Click it, and it will show you sent `/start`. If everything is working, your bot will reply `Bot Enabled`.
7. Now try sending `hello`. Your bot should reply `Hello YourName`

## Customising
1. Open `main.py`
2. On line 116 there is the below code
```python
	# CUTOMISE FROM HERE
                send('I\'m a bot')
            elif '/roll' in text:
                send(name + ' rolled a die and got ' + str(random.randrange(1,7)))
```
3. Customise the code. The `send('I\'m a bot')` is what is called when someone types `/help`. The add 
```python
elif '/command' in text:
	#DO SOMETHING
``` for each command you have.
4. Then customise
```python
# MESSAGES
# CUSTOMISE FROM HERE
elif 'who are you' in text.lower():
    reply('I am a bot.\nFor more information type /help.')
elif 'hello' in text.lower():
    send('Hello ' + first_name)
elif 'hi' in text.lower():
    send('Hi')
```
to do what you wan't when someone sends a message. You can use `send('my message')` to send a message and `reply('my message')` to reply to the message. Both types are shown below