import random
import requests
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game

TOKEN = "NTM1MzY2NTg0NzAxODEyNzM3.DyHHDQ.ObETFzF81gPRWtPikDzSslovubI"

client = commands.Bot(command_prefix='!')

@client.command(name="8ball")
async def eight_ball():
    possible_responses = [
        'No',
        'Yes',
        'Ask Again later',
        'Outlook good',
        'Very Doubtful',
        'Cannot predict now',
    ]
    await client.say(random.choice(possible_responses))

@client.command(name="roll")
async def dice_roll(number:int):
    await client.say(random.randint(0,number))

@client.command(name="choose")
async def randomchoose(*arg):
    options = ""
    for i in arg:
        options += (" "+i)
    print(options.split(';'))
    await client.say(random.choice(options.split(';')))

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="!help for cmds"))
    print("Up and running")

client.run(TOKEN)
