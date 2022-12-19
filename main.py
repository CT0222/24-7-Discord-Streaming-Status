import discord, os, keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix="!", self_bot=True, help_command=None)

async def on_ready():
  aawait bot.change_presence(activity=discord.Streaming(name="Cool Stream", url="Twitch Url"))

keep_alive.keep_alive()
client.run(os.getenv("token"), bot=False)
