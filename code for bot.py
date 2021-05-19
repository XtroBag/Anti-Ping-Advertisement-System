import discord
import asyncio
import sys, traceback
from discord.ext import commands, tasks
from discord.ext.tasks import loop
discord.ext.commands.Bot.login
discord.ext.commands.Bot.logout
import keep_alive
from translate import Translator
translator= Translator(to_lang="zh")
import random,string
import os
from datetime import datetime
import json
import os
import sys
import typing
from discord.utils import get
import time
import re
import random
anti_add = 'on'
anti_adds = 'on'
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
intents = discord.Intents.default()  
intents.members = True

client = commands.Bot(command_prefix='!',help_command = None,  intents=intents)

client._skip_check = lambda x, y: False
x = True

time_window_milliseconds = 5000
max_msg_per_window = 5
author_msg_times = {}

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Pings and ads"))

@client.event
async def on_message(message):
  global anti_add
  if "809606228300005377" in message.content.lower():
    if message.author.bot:
        return
    else:
        if anti_add == 'on':
          if message.author.id == (PUT PEOPLES DISCORD ID'S HERE OF WHO CAN PING YOU) : #(Name of ID) ID
            return
          if message.author.id == (PUT PEOPLES DISCORD ID'S HERE OF WHO CAN PING YOU) : #(Name of ID) ID
            return
          if message.author.id == (PUT PEOPLES DISCORD ID'S HERE OF WHO CAN PING YOU) : #(Name of ID) ID
            return
          if message.author.id == (PUT PEOPLES DISCORD ID'S HERE OF WHO CAN PING YOU) : #(Name of ID) ID
            return
          else:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Please do not ping that user thank you very much!", delete_after=10)
  elif "https://tenor.com" in message.content.lower():
    if message.author.bot:
        return
    else:
        if anti_adds == 'on':
          if message.author.id == (PUT PEOPLES DISCORD ID'S HERE OF WHO CAN ADVERTISE HERE) :
            return
          if message.author.id == (PUT PEOPLES DISCORD ID'S HERE OF WHO CAN ADVERTISE HERE) :
            return
          else:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Sorry but we don't allow GIF's here right now.", delete_after=10)

client.run(token)












Token = "YOUR TOKEN"
