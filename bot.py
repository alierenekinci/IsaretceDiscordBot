import discord
import os
import random
import asyncio
import aiohttp
import time as t
import datetime
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import errors
from main import *

token = "NzgxNDU3ODg3ODk2NjY2MTEz.X797Xw.9pvvip5e8gvqJOo3OY6WmQbOtBQ"
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    now = datetime.datetime.now()
    print(f'{bot.user.name} çalışıyor...' + "-" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    await bot.change_presence(activity=None)

@bot.command()
async def i(ctx, *args):
    title = getData(args[0])[0]
    gif = getData(args[0])[1]
    description = getData(args[0])[2]
    embed = discord.Embed(
                title=title,
                description=description,
                color=discord.Colour.purple()
            )
    embed.set_image(url=gif)
    await ctx.send(embed=embed)
    #await ctx.send("**"+title+"**"+"\n"+description+"\n"+gif)

bot.run(token)

#Geliştirmelerinizi bekliyorum :)
#Yapılacaklar
"""
#+# Kanallar düzenlenebilir olacak
#-# Tek bir kanal için değil oluşturulan kanal listesi için sorgulama yapacak
#-# Tek bir rol için değil belirli kanalları belirli roller için sorgulama yapacak
"""
