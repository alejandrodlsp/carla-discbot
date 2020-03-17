#IMPORTS
import discord
from discord.ext import commands
import os
from time import sleep

import sys
sys.path.append("..")
import locales

#COMMAND
class util (commands.Cog):


    
    def __init__(self, bot):
        self.bot = bot


    #EVENTS   -----------------------------------------------------------------------------------------------------------


    #COMMANDS -----------------------------------------------------------------------------------------------------------
    @commands.command( aliases = ['png', 'latency'])
    async def ping(self, ctx):
        await ctx.send(f'Pong! - {round(self.bot.latency * 1000)}ms')


    @commands.command( aliases = ['limpiar', 'reciclar', 'borrar', 'borra'])
    @commands.has_permissions( manage_messages=True )
    async def clear(self, ctx, amount : int):
        amount = max(0, min(amount, 20))
        await ctx.channel.purge(limit=amount)

        loc = await locales.get_locale_content(ctx.guild.name, "clear")
        await ctx.send( loc )
        sleep(5)
        await ctx.channel.purge(limit=1)


    @commands.command(pass_context = True)
    async def request(self, ctx, *, message):
        log_message = (f'{ctx.message.author} requested: {message}')

        path = "./requests.txt"
        with open(path, 'a') as file:
            file.write(log_message)
            file.close()




    #ERROR HANDLERS -----------------------------------------------------------------------------------------------------------
    @clear.error
    async def clear_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            loc = await locales.get_locale_content(ctx.guild.name, "ERROR_clear")
            await ctx.send( loc )

    @request.error
    async def request_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            loc = await locales.get_locale_content(ctx.guild.name, "ERROR_request")
            await ctx.send( loc )




def setup(bot):
    bot.add_cog( util( bot ) ) 
