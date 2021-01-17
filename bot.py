import discord
#import os
#import random
import asyncio
import aiohttp
#import time as t
import datetime
#from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import errors
from main import *

token = "ODAwNDMxODk1MDYyMTE4NDg2.YASCSw.-qKkcRkXefvgGPB89eokXm6agcU"
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    now = datetime.datetime.now()
    print(f'{bot.user.name} çalışıyor...' + "-" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    await bot.change_presence(activity=None)

@bot.command()
async def i(ctx, *args):
    errorColor=0xed4337
    mainColor=0xfde107
    if len(args) > 1:
        embed = embedFunc("Hata","Lütfen tek kelime giriniz.",errorColor)
    elif len(args) == 0:
        embed = embedFunc("Hata", "Lütfen kelime giriniz",errorColor)
    else:
        title, gif, description = getData(args[0])
        if title != "0":
            embed = embedFunc(title,description,mainColor)
            embed.set_image(url=gif)
            embed.set_footer(text="isaretce.com")
            
        else:
            title="Kelime Bulunamadı"
            embed = embedFunc(title,args[0],errorColor)
    await ctx.send(embed=embed)

def embedFunc(title,description,color):
    embed = discord.Embed(
                    title=title,
                    description=description,
                    color=discord.Colour(color)
                )
    return embed
bot.run(token)