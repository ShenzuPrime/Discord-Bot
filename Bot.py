import random
import requests
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game

TOKEN = "NTM1MzY2NTg0NzAxODEyNzM3.DyHHDQ.ObETFzF81gPRWtPikDzSslovubI"

client = commands.Bot(command_prefix='?')

@client.command(name="8ball", pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'No',
        'Yes',
        'Ask Again later',
        'Outlook good',
        'Very Doubtful',
        'Cannot predict now',
    ]
    print("it actually works")
    await client.say(conext.message.author + ", " + random.choice(possible_responses))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!!8ball"):
        possible_responses = [
            'No',
            'Yes',
            'Ask Again later',
            'Outlook good',
            'Very Doubtful',
            'Cannot predict now',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Bots are Stupid"))
    print("Shit is working I guess")

client.run(TOKEN)
