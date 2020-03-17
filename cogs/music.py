#IMPORTS
import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

import sys
sys.path.append("..")
import locales

#COMMAND
class music (commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    ######## COMMANDS #########   -----------------------------------------------------------------------------------------------------------
    @commands.command( aliases = ['j', 'joi', 'conectar'] )
    async def join(self, ctx):
        global voice

        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected:
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        
        loc = await locales.get_locale_content(ctx.guild.name, "join")
        await ctx.send(f'{loc} {channel}')



    @commands.command( aliases = ['l', 'leav', 'salir', 'desconectar'] )
    async def leave(self, ctx):

        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected:
            await voice.disconnect()
            print(f'The bot has left the channel {channel}')
        else:
            loc = await locales.get_locale_content(ctx.guild.name, "leave_error")
            await ctx.send(loc)


    @commands.command( aliases = ['p', 'music', 'pla'] )
    async def play(self, ctx, url : str):
        song_cache_path = (f'./cogs/cache/song-{ctx.guild.name}.mp3')
        song_there = os.path.isfile(song_cache_path)

        try:
            if song_there:
                os.remove(song_cache_path)
                print(f'{ctx.guild.name}Removed old song cache')
        except PermissionError:
            print(f'{ctx.guild.name}Trying to delete song cache, but permission denied\n')
            await ctx.send(f':red_circle: ERROR: The song is already on!!!')
            return
        
        loc = await locales.get_locale_content(ctx.guild.name, "play")
        await ctx.send("loc")

        voice = get(self.bot.voice_clients, guild= ctx.guild)

        ydl_opts = {
            'outtmpl': song_cache_path,
            'format' : 'bestaudio/best',
            'quiet': True,
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192',
            }],

        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        await self.join(ctx)

        voice.play(discord.FFmpegPCMAudio(song_cache_path), after=lambda e: print(f'{ctx.guild.name}Song has finished playing') )
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.value = 0.07


    @commands.command( aliases = ['pa', 'paus', 'pau', 'pausa', 'pausar', 'parar'] )
    async def pause(self, ctx):

        voice = get(self.bot.voice_clients, guild= ctx.guild)

        if voice and voice.is_playing():
            voice.pause()
            print(f'{ctx.guild.name} music paused')

    @commands.command( aliases = ['re', 'resum', 'resumir', 'continuar', 'r'] )
    async def resume(self, ctx):

        voice = get(self.bot.voice_clients, guild= ctx.guild)

        if voice and voice.is_playing():
            voice.resume()
            print(f'{ctx.guild.name} music resumed')

    @commands.command( aliases = ['s', 'sto', 'st', 'quitar'] )
    async def stop(self, ctx):

        voice = get(self.bot.voice_clients, guild= ctx.guild)

        if voice and voice.is_playing():
            voice.stop()
            print(f'{ctx.guild.name} music stopped')



    #ERROR HANDLERS   -----------------------------------------------------------------------------------------------------------

    @play.error
    async def play_error(self, ctx, error):
        await ctx.send(str(error))



# SETUP   -----------------------------------------------------------------------------------------------------------
def setup(bot):
    bot.add_cog( music( bot ) ) 
