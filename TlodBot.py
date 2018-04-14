import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
Client = discord.Client()
client =  command.Bot(command_perfix = "!")

@client.event
async def on_ready():
	print("Bot is ready")
	
@client.event
async def on_message(message):
	if message.content == ".cookie":
		await client.send_message(message.channel, ":cookie:")	



client.run("NDMzNjUwNjAzMjkwMzk0NjQ1.Da_I7w.YvXVZJ6llIT7xDQ98P1offhGYA0")
