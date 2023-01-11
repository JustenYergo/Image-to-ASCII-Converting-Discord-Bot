import os
import discord
from discord.ext import commands
import pil

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents = intents)
@bot.command(name='test', help='input url and name the image, converts inputted image to ascii art')
async def test(ctx, url):
  print(url)
  pil.url = url
  print(pil.url)
  print(pil.ascii_converter(pil.url))
  file1 = open('ascii_image.txt', 'r')
  lines = file1.readlines()
  print(lines)
  await ctx.send("I made this for you: \n")
  await ctx.send("\n {0}".format(lines))


@bot.command()
async def echo(ctx, arg):
  await ctx.send(arg)
  
bot.run(os.getenv('TOKEN'))
