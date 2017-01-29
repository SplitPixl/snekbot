import discord
from discord.ext import commands
import asyncio
import re
import random
from cleverbot import Cleverbot

bot = commands.Bot(command_prefix=['snek ', 'snekbot ', 'Snek', 'snekbot2', 'Snekbot2', 'snek2', 'Snek2'], description='this is snekbot.')
cb = Cleverbot()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="snake"), idle=False)

@bot.command()
async def help():
    await bot.say('Hssssss \nhi, am snekbot2, like snekbot but better and buffer\ncall me with snek and tell me what to do eg. snek pls\nlist of commands:\n *hss* make me say thigns\n*pls*\n *whomade*\n*info*\n*invite* this give a link to add snekbot to your server\n*intensifies*\n*hello*\n*hi*\n*noboop*\n*step*\n*nervous*\n*play* say what game you want me to play\n*bully* decide if akarin will protect someone or bully them\n*art* shows you my beautiful art\n*smug*\n*git* i dunno why you would want the github but you can get it')
	
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
    await bot.say('to add snekbot to your server click this: https://goo.gl/xqfKWn')

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
	await bot.say (random.choice(['http://i.imgur.com/NRMo4jZ.jpg' , 'http://i.imgur.com/7NEWEFu.jpg']))

@bot.command()
async def art():
	await bot.say (random.choice(['https://farm2.staticflickr.com/1622/24885440680_02487a7356_o_d.gif' , 'https://farm6.staticflickr.com/5700/23833016945_7cab5c3e92_o_d.png']))

@bot.command()
async def smug():
	await bot.say ('http://orig09.deviantart.net/6e2f/f/2010/132/d/7/5th_gen_starter___tsutaaja_by_arkeis_pokemon.png')

@bot.command()
async def git():
    """snek's source code"""
    await bot.say('https://github.com/SplitPixl/snekbot')


bot.run('giv token pls')