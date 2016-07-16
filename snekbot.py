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
    await bot.change_status(game=discord.Game(name="snake.exe"), idle=False)

#@bot.event
#async def on_message(message):
#    if not message.author.id == bot.user.id:
#        if message.server == None:
#            await bot.send_typing(message.channel)
#            await bot.send_message(message.channel, cb.ask(message.content))
#        else:
#            m = re.match(r'(.*)\s*<@!?'+bot.user.id+'>\s*(.*)',message.content)
#            if m != None:
#                await bot.send_typing(message.channel)
#                await bot.send_message(message.channel, cb.ask(m.group(1)+' '+m.group(2)))
#thanks jag

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
    await bot.say('to add snekbot to your server click this: https://goo.gl/HTxJWJ')

@bot.command()
async def intensifies():
    """[SNEK INTENSIFIES]"""
    await bot.say('http://i.imgur.com/hSZfCiD.gif')

@bot.command()
async def hello():
    """hi"""
    await bot.say('hello yes this is snek.')

@bot.command()
async def noboop():
    """noboop snek"""
    await bot.say('http://i.imgur.com/j4p70OX.jpg')

@bot.command()
async def play(*, game_to_play):
    """snek likes playing game"""
    await bot.change_status(game=discord.Game(name=game_to_play), idle=False)

@bot.command()
async def sourcecode():
    """snek's source code"""
    await bot.say('https://github.com/SplitPixl/snekbot')


bot.run('giv token pls')
