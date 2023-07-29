import discord
from discord.ext import commands #importing the commands extension for prefixes!
import os
from dotenv import load_dotenv #thing for hiding my token

load_dotenv() #loads my token for the bot from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is up and running")

@bot.slash_command(name = "hello", description = "Say hello to the bot") #slash commands are the new way discord bots work. I hate it i want the prefix ones back
async def hello(ctx):
    await ctx.respond("Hey!")

#Here are the good old prefixed commands
intents = discord.Intents.default() #I have no clue what this is but i need it
bot = commands.Bot(command_prefix = "!", intents=intents) #Bot will work using the exclamation mark for a prefix before the command

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


bot.run(os.getenv('TOKEN')) # Gets the token to start the bot