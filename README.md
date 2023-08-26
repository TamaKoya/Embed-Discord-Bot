# Embed-Discord-Bot
A Discord Bot written in Python using discord.py and discordhelp libraries.

Upon reacting to a message with specified emote, the bot will send a embed message as a reply, that'll ping the author of the message.

Example:

User1: *Sends a message*: "Lorem Ipsum dolor sit amet..."
User2: *adds 🤖 as a reaction to User1's message* (the emote can be changed)
Bot: Creates an embed message with given parameters, returns it as embed variable, which is then sent as a reply that'll mention User1
