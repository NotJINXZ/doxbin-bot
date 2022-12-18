import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})\n')


@client.event
async def on_message(message):
    if message.content.startswith('!dox'):
        if message.author.voice and message.author.voice.channel:
            # User is in a voice channel
            guild = message.guild
            if guild.voice_client:
                # Bot is already in a voice channel
                voice = guild.voice_client
            else:
                # Bot is not in a voice channel, so join the channel
                channel = message.author.voice.channel
                voice = await channel.connect()
        
        voice.play(discord.FFmpegPCMAudio('song.mp3'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1
      


client.run(TOKEN)
