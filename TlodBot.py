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
	if message.content == "!cookie":
		await client.send_message(message.channel, ":cookie:")
	if message.content == "!invite":
	    await client.send_jessage(message.channel, "https://discordapp.com/api/oauth2/authorize?client_id=433650603290394645&permissions=0&scope=bot")	



client.run("NDMzNjUwNjAzMjkwMzk0NjQ1.DbO4xQ.jqJuEoVHsxRSNikGYsCL2Vj-ueI")
    
    