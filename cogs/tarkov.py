#IMPORTS
import discord
from discord.ext import commands
import os

#COMMAND
class tarkov (commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    #EVENTS     -----------------------------------------------------------------------------------------------------------


    #COMMANDS   -----------------------------------------------------------------------------------------------------------
    @commands.command()
    async def factory(self, ctx):
        embed = discord.Embed(
            title = 'Factory',
            description = 'https://www.gamemaps.co.uk/game/tarkov/maps/factory_iso_es',
            colour = discord.Colour.blue()
        )

        embed.set_image(url="https://forum.escapefromtarkov.com/uploads/monthly_2017_08/Tarkin_v4_+tunels_Factory.jpg.686b65ccd9f64f83144e0ed3fe6ab98a.jpg")
        await ctx.send(embed = embed)
    

    @commands.command()
    async def shoreline(self, ctx):
        embed = discord.Embed(
            title = 'Shoreline',
            description = 'https://www.gamemaps.co.uk/game/tarkov/maps/shoreline_3d_maksen',
            colour = discord.Colour.blue()
        )

        embed.set_image(url="https://preview.redd.it/rhrnm0yw9wd41.jpg?width=3310&format=pjpg&auto=webp&s=16fc2edf95f005a76d92ba3cd58a2a8de2196c61")
        await ctx.send(embed = embed)


    @commands.command()
    async def customs(self, ctx):
        embed = discord.Embed(
            title = 'Customs',
            description = 'https://www.gamemaps.co.uk/game/tarkov/maps/customs_2d_roflwoffl_v9',
            colour = discord.Colour.blue()
        )

        embed.set_image(url="https://i.redd.it/zmanfyd558841.png")
        await ctx.send(embed = embed)


    @commands.command()
    async def woods(self, ctx):
        embed = discord.Embed(
            title = 'Woods',
            description = 'https://www.gamemaps.co.uk/game/tarkov/maps/woods_callouts',
            colour = discord.Colour.blue()
        )

        embed.set_image(url="https://gamerjournalist.com/wp-content/uploads/2020/01/Escape-From-Tarkov-Woods-Map-Guide-2020-scaled.jpg")
        await ctx.send(embed = embed)
    

    @commands.command()
    async def interchange(self, ctx):
        embed = discord.Embed(
            title = 'Interchange',
            description = 'https://www.gamemaps.co.uk/game/tarkov/maps/full_lorathor_v2',
            colour = discord.Colour.blue()
        )

        embed.set_image(url="https://gamerjournalist.com/wp-content/uploads/2020/01/escape-from-tarkov-interchange-spawns-1.png")
        await ctx.send(embed = embed)
    

    @commands.command()
    async def labs(self, ctx):
        embed = discord.Embed(
            title = 'Labs',
            description = 'https://www.gamemaps.co.uk/game/tarkov/maps/explained_en',
            colour = discord.Colour.blue()
        )

        embed.set_image(url="https://img.resized.co/dexerto/eyJkYXRhIjoie1widXJsXCI6XCJodHRwczpcXFwvXFxcL2ltYWdlcy5kZXhlcnRvLmNvbVxcXC91cGxvYWRzXFxcLzIwMjBcXFwvMDFcXFwvMDcxMTAwMTdcXFwvRXNjYXBlLWZyb20tVGFya292LVRoZS1MYWItbWFwLWFuZC1leHRyYWN0aW9uLXBvaW50cy0xMDI0eDMwMC5wbmdcIixcIndpZHRoXCI6XCJcIixcImhlaWdodFwiOlwiXCIsXCJkZWZhdWx0XCI6XCJodHRwczpcXFwvXFxcL3MzLWV1LXdlc3QtMS5hbWF6b25hd3MuY29tXFxcL3BwbHVzLmltYWdlcy5kZXhlcnRvLmNvbVxcXC91cGxvYWRzXFxcLzIwMTlcXFwvMTFcXFwvMTEyMTQ5NDNcXFwvcGxhY2Vob2xkZXIuanBnXCJ9IiwiaGFzaCI6ImQ1ZWM1ODUzZGE4NDFmMmY1MDk5NjY0NzZmOWFkOGZkOWM5MGE4ZGEifQ==/escape-from-tarkov-the-lab-map-and-extraction-points-1024x300.png")
        await ctx.send(embed = embed)


    @commands.command()
    async def reserve(self, ctx):
        embed = discord.Embed(
            title = 'Reserve',
            description = 'https://www.gamemaps.co.uk/game/tarkov/maps/reserve_3d_photonready',
            colour = discord.Colour.blue()
        )

        embed.set_image(url="https://i.redd.it/d3pxs4cmsbv31.png")
        await ctx.send(embed = embed)


    @commands.command(aliases = ['caliber', 'bullets', 'ammo', 'bala', 'municion', 'municiones'])
    async def bullet(self,ctx):
        await ctx.send("https://docs.google.com/spreadsheets/d/1_CQGo_W3AFEe0Ll8AXbLF7zN6xUN1h_ZpQKFdvGd25M/htmlview?sle=true#gid=1970148328")



## SETUP   -----------------------------------------------------------------------------------------------------------
def setup(bot):
    bot.add_cog( tarkov( bot ) ) 
