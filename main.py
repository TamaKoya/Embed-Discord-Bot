import discord
import discordhelp
import dotenv
import os


intents = discord.Intents.all()
client = discord.Client(intents=intents)

dotenv.load_dotenv()


@client.event
async def on_ready():
    print(f'I have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('hello'):
        await message.channel.send("hello!")
    if msg.startswith('Test'):
        await message.channel.send("Testing...")


@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == discordhelp.getEmoteFromName(":robot:") and reaction.count <= 1:
        response_message = discordhelp.createEmbed("Test Title", "Test Response", "Test Footer",
                                                   "Tamamo Koyanskaya", discord.Color.light_embed())
        await reaction.message.reply(content=None, embed=response_message, mention_author=True)


client.run(os.getenv('token'))
