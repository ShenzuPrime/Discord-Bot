from discord.ext.commands import Bot
from discord import Game
import random

TOKEN = "NTM1MzY2NTg0NzAxODEyNzM3.DyHHDQ.ObETFzF81gPRWtPikDzSslovubI"

client=Bot(command_prefix="!")

@client.command
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

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == ("Magic Eight Ball"):
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
