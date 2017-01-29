import discord
from discord.ext import commands
import asyncio
import re
from cleverbot import Cleverbot

bot = commands.Bot(command_prefix=['snek ', 'snekbot '], description='this is snekbot.')
cb = Cleverbot()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_status(game=discord.Game(name="snake"), idle=False)

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
    await bot.say('jacob made snekbot2 which was based off of SplitPixl\'s snekbot')

@bot.command()
async def info():
    """info about snekbot"""
    await bot.say('snekbot was coded in python with the library discord.py. hss.')

@bot.command()
async def invite():
    """snekbot invite link"""
    await bot.say('to add snekbot to your server click this: goo.gl/xqfKWn')

@bot.command()
async def intensifies():
    """[SNEK INTENSIFIES]"""
    await bot.say('http://i.imgur.com/hSZfCiD.gif')

@bot.command()
async def hello():
    """hi"""
    await bot.say('hello yes this is snek.')
	
@bot.command()
async def hi():
    """hi"""
    await bot.say('hi yes this is snek.')

@bot.command()
async def noboop():
    """noboop snek"""
    await bot.say('http://i.imgur.com/j4p70OX.jpg')

@bot.command()
async def step():
    """no step on snek"""
    await bot.say('http://i.imgur.com/CjCZX9c.png')

@bot.command()
async def nervous():
    """nervous hissing"""
    await bot.say('http://i.imgur.com/b6s9WTJ.gif')

@bot.command()
async def play(*, game_to_play):
    """snek likes playing game"""
    await bot.change_status(game=discord.Game(name=game_to_play), idle=False)

@bot.command()
async def bully():
	if(randint(0,1)==0)
		await bot.say ('http://i.imgur.com/NRMo4jZ.jpg')
	else
		await bot.say ('http://i.imgur.com/7NEWEFu.jpg')


@bot.command()
async def sourcecode():
    """snek's source code"""
    await bot.say('https://github.com/SplitPixl/snekbot')


bot.run('giv token pls')