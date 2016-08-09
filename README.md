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
2. Open main.py and change the line that says
``` Python
TOKEN = 'API TOKEN'
``` to
``` Python
TOKEN = 'whatever your api token from BotFather is'
```