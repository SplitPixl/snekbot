import discord
from discord.ext import commands
import asyncio
import re
import random

bot = commands.Bot(command_prefix=['snek ', 'snekbot '], description='this is snekbot.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="snek.py"))

@bot.command()
async def hss(*, stuff_for_snek_to_say):
    """says stuff"""
    await bot.say(stuff_for_snek_to_say)

@bot.command()
async def pls():
    """try it"""
    await bot.say(':snake:')

@bot.command()
async def whomade():
    """who made snek?"""
    await bot.say('splitpixl made snekbot')

@bot.command()
async def info():
    """info about snekbot"""
    await bot.say('snekbot was coded in python with the library discord.py. hss.')

@bot.command()
async def invite():
    """snekbot invite link"""
    await bot.say('to add snekbot to your server click this: https://snek.splitpixl.xyz/')

@bot.command()
async def intensifies():
    """[SNEK INTENSIFIES]"""
    await bot.say('https://snek.splitpixl.xyz/intense.gif')

@bot.command()
async def hello():
    """hi"""
    await bot.say('hello yes this is snek.')

@bot.command()
async def noboop():
    """noboop snek"""
    await bot.say('https://snek.splitpixl.xyz/noboop.jpg')

@bot.command()
async def play(*, game_to_play):
    """snek likes playing game"""
    await bot.change_presence(game=discord.Game(name=game_to_play))

@bot.command()
async def boop(*, who_to_boop):
    """boop that heckr"""
    await bot.say("*boops " + who_to_boop + "*")

@bot.command()
async def sourcecode():
    """snek's source code"""
    await bot.say('https://github.com/SplitPixl/snekbot')

@bot.command()
async def snek():
    """sneksneksnek"""
    sneks = ['snek', 'hss', 'ssssnek', 'slither', 'snek sneek']
    await bot.say(random.choice(sneks))


bot.run(open('./token.discord','r').read().replace('\n', ''))
