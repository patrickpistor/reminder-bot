from keep_alive import keep_alive
import discord
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import os
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash.utils import manage_commands

TOKEN = os.environ['TOKEN']

client = discord.Client()

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online, activity=discord.Game(name='Discord')
    )  #Bot status, change this to anything you like
    print("Bot online")


@slash.slash(name="ping", description="Ping Pong")
async def _help(ctx: SlashContext):
    await ctx.send(content="pong!")


@slash.slash(
    name="space",
    description="Space your text",
    options=[
        manage_commands.create_option(  #create an arg
            name="text",
            description="The text to space",
            option_type=3,
            required=True)
    ])
async def _space(ctx: SlashContext, sentence):
    newword = ""  #
    for char in sentence:
        newword = newword + char + "   "
    await ctx.send(content=newword)


keep_alive()

#Run our bot
client.run(TOKEN)
