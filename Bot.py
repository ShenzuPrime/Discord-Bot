import time
import random
import requests
import discord
from discord.ext import commands

tokenfile =  open("token.txt", "r")
TOKEN = tokenfile.read()

client = commands.Bot(command_prefix='~')

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

@client.command()
async def oddsoutof(ctx,int:int,*args):
    await ctx.send("you have 5 seconds to guess a number between 1 and "+str(int))
    number = random.randrange(1,int)
    holder = ""
    for i in args:
        holder += (" "+i)
    time.sleep(5)
    await ctx.send("If you guessed "+str(number)+holder)


client.run(TOKEN)
