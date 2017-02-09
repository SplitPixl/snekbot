import discord
from discord.ext import commands
import asyncio
import re
import random

bot = commands.Bot(command_prefix=['snek ', 'snekbot ', 'Snek ', 'snekbot2 ', 'Snekbot2 ', 'snek2 ', 'Snek2 '], description='Hssssss \nhi, am snekbot2, like snekbot but better and buffer')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="snake"))

@bot.command()
async def hss(*, stuff_for_snek_to_say):
	"""says stuff"""
	await bot.say(stuff_for_snek_to_say)
	print(stuff_for_snek_to_say)

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
    """hello"""
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
    await bot.change_presence(game=discord.Game(name=game_to_play))
	
@bot.command()
async def stream(*, game_to_play):
	"""snek likes streaming game"""
	#await bot.change_presence(game=discord.Game(name=game_to_play))
	await bot.change_presence(game=discord.Game(type=1,name=game_to_play,url='https://www.twitch.tv/pokespeedrunbots'))

	
@bot.command()
async def ily():
	"""tell snek ily"""
	await bot.say('snek loves yogurt 2')

@bot.event
async def on_member_join(member):
	if format(member.server)=='[S]quad':
		# await bot.send_message(member.server, 'Welcome {0}!'.format(member))
		await bot.send_message(member.server, 'Welcome to the [S]quad Discord!\nIf you have any questions, feel free to ask any of the mods')

@bot.command()
async def whoBully():
	"""who does snek bully? (not implemented)"""
	
@bot.command()
async def bully(member : discord.User = bot.user):
	"""watch out, snek will bully u"""
	bully_reply=[]
	bully_object=open("bully.txt","r")
	while 1:
		line = bully_object.readline()
		if not line:
			break	
		else:
			bully_reply.append(line)
	await bot.say(random.choice(bully_reply).format(member.name));	

@bot.command()
async def ifbully():
	"""to bully or not to bully"""
	await bot.say (random.choice(['http://i.imgur.com/NRMo4jZ.jpg' , 'http://i.imgur.com/7NEWEFu.jpg']))

@bot.command()
async def art():
	"""jacob's beautiful art"""
	await bot.say (random.choice(['https://farm2.staticflickr.com/1622/24885440680_02487a7356_o_d.gif' , 'https://farm6.staticflickr.com/5700/23833016945_7cab5c3e92_o_d.png']))

@bot.command()
async def plsno():
	"""pls no this is a bad idea u will regret it"""
	await bot.say('snek pls')
	await bot.say('snek pls')
	await bot.say('snek pls')
	await bot.say('snek pls')
	await bot.say('snek pls')
	await bot.say('snek pls')


@bot.command()
async def smug():
	"""u srs askin snek what smug is?"""
	await bot.say ('http://orig09.deviantart.net/6e2f/f/2010/132/d/7/5th_gen_starter___tsutaaja_by_arkeis_pokemon.png')

@bot.command()
async def live():
	await bot.say ('i have risen my son')
	
@bot.command()
async def git():
    """snek's source code"""
    await bot.say('https://github.com/SplitPixl/snekbot')
file_object=open("key.txt","r")
bot.run(file_object.read())