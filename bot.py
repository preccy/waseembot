import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="chat")
    await channel.send(f"Waseem welcome's you sir {member.mention}")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="chat")
    await channel.send(f"Waseem never liked you anyway. {member.mention}")

@client.command()
async def waseem(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/624258840250155028/702571521234698260/IMG_20200417_023227_472.jpg')

@client.command()
async def tom(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/702585932083363891/702586081303855184/TWNB.jpg')

@client.command()
async def ben(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/702585932083363891/702586136010293319/JWNB.jpg')

@client.command()
async def ethan(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/702585932083363891/702586149432066058/EWNB.jpg')

@client.command()
async def ksaw(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/702585932083363891/702586187189321748/slavWNB.jpg')

@client.command()
async def csgo(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/702585932083363891/702586065307041822/BeWNB.jpg')


as


client.run('NzAyNTQyOTIwNzYyMjYxNjM1.XqBkHg.gjzjETNHYAexbHUOhmE6E7VcfWg')
