#IMPORTS
import discord
from discord.ext import commands
import requests

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import secret

import sys
sys.path.append("..")
import locales

#COMMAND
class meme (commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    #EVENTS    -----------------------------------------------------------------------------------------------------------

    #COMMANDS   -----------------------------------------------------------------------------------------------------------
    @commands.command()
    async def meme_api(self,ctx):
        await ctx.send("https://api.imgflip.com/popular_meme_ids")


    @commands.command( aliases = ['novio'])
    async def boyfriend(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '112126428', text1, text2)
        

    @commands.command( aliases = ['bat', 'slap', 'robin'])
    async def batman(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '438680', text1, text2)


    @commands.command( aliases = ['button'])
    async def buttons(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '87743020', text1, text2)


    @commands.command( aliases = ['bob', 'esponja', 'sponge'])
    async def spongebob(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '102156234', text1, text2)


    @commands.command( aliases = ['hotline'])
    async def drake(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '181913649', text1, text2)


    @commands.command( aliases = ['cat_yelling'])
    async def yelling(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '188390779', text1, text2)


    @commands.command( aliases = ['change', 'cambiadeopinion'])
    async def changemymind(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '129242436', text1, text2)


    @commands.command( aliases = ['waitingskeleton', 'esperando', 'esqueleto'])
    async def waiting(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '4087833', text1, text2)


    @commands.command( aliases = ['entodoslados', 'buzz', 'woody'])
    async def everywhere(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '91538330', text1, text2)


    @commands.command( aliases = ['is this', 'esesto'])
    async def isthis(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '100777631', text1, text2)


    @commands.command( aliases = ['gaviota', 'inhalar', 'inhale'])
    async def seagull(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '114585149', text1, text2)


    @commands.command( aliases = ['bill', 'firmar'])
    async def trump(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or " "

        await self.display_api_embed(ctx, '91545132', text1, text2)


    @commands.command( )
    async def kermit(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '84341851', text1, text2)


    @commands.command( aliases = ['detector', 'mentira', 'liedetector'])
    async def lie(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]
        text2 = split_text[1] or ""

        await self.display_api_embed(ctx, '444501', text1, text2)


    @commands.command( aliases = ['retarded', 'retard'])
    async def ohno(self, ctx, *, text):
        split_text = text.split(",")
        text1 = split_text[0]

        await self.display_api_embed(ctx, '44606798', text1, " ")



    ########## UTIL ##########   -----------------------------------------------------------------------------------------------------------
    async def display_api_embed(self, ctx, template_id, text1 = " ", text2 = " "):
        image_url = await self.request_image(template_id, text1, text2)

        loc = await locales.get_locale_content(ctx.guild.name, "meme_embed")
        
        embed = discord.Embed(
            title = loc,
            colour = discord.Colour.orange()
        )

        embed.set_image(url= image_url)
        await ctx.send(embed = embed)


    async def request_image(self, template_id, text1 = "", text2 = ""):
        base_url = 'https://api.imgflip.com/caption_image'

        PARAMS = {'template_id' : template_id,
                'username' : secret.IMGFLIP_USERNAME,
                'password' : secret.IMGFLIP_PASSWORD,
                'font' : 'arial',
                'text0' : text1,
                'text1' : text2}

        response = requests.get(url = base_url, params = PARAMS)

        data = response.json()

        if data['success'] == False:
            print("ERROR: API Error, could not load image")

        data = data['data']
        image_url = data['url']

        return image_url



    #ERROR HANDLERS   -----------------------------------------------------------------------------------------------------------
 


#SETUP  -----------------------------------------------------------------------------------------------------------
def setup(bot):
    bot.add_cog( meme( bot ) ) 
