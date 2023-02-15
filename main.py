import discord
import os
from discord.ext import commands
from datetime import datetime, timedelta

client = discord.Client()
token = os.environ['TOKEN']
server = os.environ['SERVER']


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name="🔨The Toolbox")
    print(guild)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


try:
    client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
    else:
        raise e
