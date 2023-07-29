import discord
from discord.ext import commands #importing the commands extension for prefixes!
import os
from dotenv import load_dotenv #thing for hiding my token
from random import randint  



load_dotenv() #loads my token for the bot from the env file

#bot = discord.Bot() //was used for slash commands, not needed i want prefix

#Here are the good old prefixed commands
intents = discord.Intents.default() #I have no clue what this is but i need it
intents.message_content = True #allows me to read user messages in the server
bot = commands.Bot(command_prefix = "!", intents=intents) #Bot will work using the exclamation mark for a prefix before the command


@bot.event
async def on_ready():
    print(f"{bot.user} is up and running")

#Cannot use currently, need to figure out how to have both prefix and slash commands
#@bot.slash_command(name = "hello", description = "Say hello to the bot") #slash commands are the new way discord bots work. I hate it i want the prefix ones back
#async def hello(ctx):
#    await ctx.respond("Hey!")


#____________________________________________________________________________________________________________
#Commands where bot will read chat and answer if it sees certain words used
@bot.event
async def on_message(message):
    #grabs this information. Prints it to console.
    username = str(message.author).split('#')[0]

    if message.author == bot.user: #ignore messages made by the bot
        return
    
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'------------------------\n{username}: {user_message} --{channel}')
    
    if user_message.lower() == "hello": #replies whenever it sees the word hello
        await message.channel.send(f'Hello there {username}')

    await bot.process_commands(message)




#_______________________________________________________________________________________________________________
#Normal commands
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command() #command i used to have for the old bot, is fun to see what sorta latency it gets
async def latency(ctx):
    await ctx.channel.send(f'The latency is {round(bot.latency * 1000)}ms')

@bot.command()
async def roll(ctx, num):
    randomNum = randint(1, int(num))
    await ctx.channel.send(f'You rolled a {randomNum}')



#running the bot
bot.run(os.getenv('TOKEN')) # Gets the token to start the bot