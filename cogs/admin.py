#IMPORTS
import discord
from discord.ext import commands
import os

import sys
sys.path.append("..")
import locales

#COMMAND
class admin (commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #EVENTS     -----------------------------------------------------------------------------------------------------------


    #COMMANDS   -----------------------------------------------------------------------------------------------------------
    @commands.command( aliases = ['echar'])
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        self.log(f'{member.name} was kicked: {reason}', ctx.guild.name)


    @commands.command( aliases = ['banear'])
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        self.log(f'{member.name} was banned: {reason}', ctx.guild.name)


    @commands.command( aliases = ['pardon', 'perdonar'])
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

                loc = await locales.get_locale_content(ctx.guild.name, "on_pardon")

                await ctx.send(f' {loc} {user.name}#{user.discriminator}')
                
                self.log(f'{user.name} Was pardoned', ctx.guild.name)
                return


    #UTIL   -----------------------------------------------------------------------------------------------------------
    def log(self, message, guild):

        path = "/logs/guilds" + guild + ".log"
        file = None

        try:
            file = open(path, 'r')
        except IOError:
            file = open(path, 'w')
        finally:
            with open(path, 'a') as file:
                file.write(message)
                file.close()

#SEUP  -----------------------------------------------------------------------------------------------------------
def setup(bot):
    bot.add_cog( admin( bot ) ) 
