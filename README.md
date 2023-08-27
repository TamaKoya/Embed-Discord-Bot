# Embed-Discord-Bot
A Discord Bot written in Python using discord.py and discordhelp libraries.

Upon reacting to a message with specified emote, the bot will send a embed message as a reply, that'll ping the author of the message.

Example:
```
User1: *Sends a message*: "Lorem Ipsum dolor sit amet..."
User2: *adds 🤖 as a reaction to User1's message* (the emote can be changed)
Bot: Creates an embed message with given parameters, returns it as embed variable, which is then sent as a reply that'll mention User1
```
NOTE: This is a local hosted version of the bot, for bot hosted on VPS/Cloud, you may have to adjust the code so it runs on that.

NOTE 2 (For local hosted): The code doesn't contain a token needed to run the bot, you must get one yourself in Discord Developer Portal and then put it either in a `.env` file (STRONGLY preferred for security reasons) or replace `client.run(os.getenv('token'))` with `client.run("<token>")`, where `<token>` is the token you got from Discord Developer Portal.
