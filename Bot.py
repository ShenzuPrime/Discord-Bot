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

@client.command(name='8ball')
async def eightball(ctx):
    holder = ['yes', 'no','try again']
    await ctx.send(random.choice(holder))

@client.command()
async def choose(ctx,*args):
    holder = ""
    for i in args:
        holder += (" "+i)
    await ctx.send(random.choice(holder.split(',')))

@client.command()
async def gchange(ctx,*args):
    holder = ""
    for i in args:
        holder += (" "+i)
    game = discord.Game(holder)
    await client.change_presence(status=discord.Status.idle, activity=game)

client.run(TOKEN)
