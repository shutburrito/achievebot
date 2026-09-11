import discord
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv
from backend.config import DISCORD_TOKEN #brings in the discord token from the config file

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #this adds the parent directory to the path so that the bot can access the backend folder

intents = discord.Intents.default() #this sets the intents, what the bot recieves from discord, to the default values
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is logged in.")

@bot.command()
async def ping(ctx):
    """checking latency"""
    await ctx.send(f"pong {round(bot.latency * 1000)}ms")

if __name__ == "__main__":
    if DISCORD_TOKEN is None:
        print("Error: DISCORD_TOKEN is not set")
        sys.exit(1)
    bot.run(DISCORD_TOKEN)