import random
import requests
import discord
from discord.ext import commands

tokenfile =  open("token.txt", "r")
TOKEN = tokenfile.read()

client = commands.Bot(command_prefix='~')

@client.command()
async def ping(ctx):
    await ctx.send('pong')

client.run(TOKEN)
print("everything is working")
