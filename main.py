#from moderation import Moderation
import os                           #==========================================================
import random                       #
import discord                      #
from discord.ext import commands    #  Importig packs
from discord import Intents         #
from keep_alive import keep_alive   #
import datetime                     #==========================================================

client = commands.Bot(command_prefix = "^_" , intents = Intents.all())

#bot = discord.Client()
channel = client.get_channel(839157641179299963)

@client.event
async def on_ready():
    print("Bot is ready")
    global startPoint
    startPoint = datetime.datetime.now()
    await client.change_presence(status = discord.Status.idle , activity = discord.Game("mind tricks on you"))
    await client.get_channel(839157641179299963).send("Bot started/restarted")
        
@client.event
async def on_member_join(member):
    await client.get_channel(839157641179299963).send(f"{member} has joined")

@client.event
async def on_member_remove(member):
    await client.get_channel(839157641179299963).send(f"{member} has left")

@client.command()
async def uptime(ctx):
    current = datetime.datetime.now()
    delta = startPoint - current
    await ctx.send(f"It has been {delta.day} days, {delta.hour} hours, {delta.minute} minutes and {delta.second} seconds since last accident.")

@client.command()
async def delete(ctx , amount = 2):
    await ctx.channel.purge(limit = amount)

@client.command()
async def clear(ctx , amount = 1):
    await ctx.channel.purge(limit = amount)

@client.command()
async def randomiser(ctx , * ,max):
    await ctx.send(random.randrange(start=1 , stop = int(max)))

@client.command(aliases = ["gh" , "creator"])
async def github(ctx):
    await ctx.send("github.com/testroyer")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms!")

@client.command(aliases = ["8ball" , "eightball" , "test"])
async def _8ball(ctx , * , question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]
    await ctx.send(random.choice(responses))


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


keep_alive()
token = os.getenv("Token")
client.run(token)