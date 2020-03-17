#IMPORTS
import discord
from discord.ext import commands
from random import randrange
import random
import os
import requests

import sys
sys.path.append("..")
import locales


#COMMAND
class fun (commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    #EVENTS    -----------------------------------------------------------------------------------------------------------


    #COMMANDS   -----------------------------------------------------------------------------------------------------------
    @commands.command()
    async def carla(self, ctx):
        loc = await locales.get_locale_content(ctx.guild.name, "carla")
        await ctx.send(  loc  )


    @commands.command( aliases = ['8ball', 'pregunta'] )
    async def question(self, ctx, *, question):
        options = ['Que si, pesado', 'AJAJJAJAJAJAJAJAJJ, no', 'Casi pero me da a mi que no eh', 'Venga va, intentalo luego', 'Ji amo', 'Siii', 'Nooo :C', 'Claro que si maricona', 'Maricon es lo que eres, que si cojones', 'Puede ser...', 'Tal vez',  'Depende de que partido politico seas', 'Nope', 'Si no fueses un simio, si', 'Esta claro que si', 'Como que no', 'Mejor no te lo digo', 'Mu raro que pasase', 'Mi respuesta es: no', 'El horoscopo hoy me dice que si', 'Si.', 'No cuentes con ello']
        answer = random.choice(options)
        await ctx.send(answer)


    @commands.command( aliases = [ 'progresistas', 'podemos', 'progre', 'liberal'])
    async def sjw(self, ctx):
        loc = await locales.get_locale_content(ctx.guild.name, "sjw")
        await ctx.send( loc )


    @commands.command( aliases = [ 'espana', 'españa', 'abascal', 'santiago', 'spain', 'mexico'])
    async def vox(self, ctx):
        loc = await locales.get_locale_content(ctx.guild.name, "vox")
        await ctx.send( loc )


    @commands.command( aliases = ['tristeperono', 'triste'])
    async def sad(self,ctx):
        loc = await locales.get_locale_content(ctx.guild.name, "sad")
        await ctx.send( loc )


    @commands.command( aliases = ['perro', 'wouf', 'perrito'])
    async def dog(self, ctx):
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        image_url = response.json()["message"]
        
        embed = discord.Embed(
            title = ':dog: :dog: :dog: :dog: :dog: :dog:  ',
            colour = discord.Colour.purple()
        )

        embed.set_image(url= image_url)
        await ctx.send(embed = embed)


    @commands.command( aliases = ['gato', 'meaw', 'gatito'])
    async def cat(self, ctx):
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        image_url = response.json()[0]["url"]
        
        embed = discord.Embed(
            title = ':kissing_cat: :kissing_cat: :kissing_cat: :kissing_cat: ',
            colour = discord.Colour.red()
        )

        embed.set_image(url= image_url)
        await ctx.send(embed = embed)
    

    @commands.command( aliases = [ 'tamaño', 'rabo', 'pito', 'polla', 'size'])
    async def dick(self, ctx, user : discord.User):
        username = user.name
        size = 0

        with open('cogs/cache/dicks.txt','r') as file:
            while True:
                x = file.readline()
                x = x.rstrip()

                if x[:-1] == username:
                    size = int(x[-1:])
                    file.close()
                    break
                if not x:
                    break

        if size == 0:
           size = randrange(9)
           with open('cogs/cache/dicks.txt', 'a') as file:
                file.write(username + "" + str(size) + '\n')
                file.close()
                                         
        str_send = "8="
        for i in range(0, size):
            str_send = str_send + "="
        str_send = str_send + "D"
        
        loc = await locales.get_locale_content(ctx.guild.name, "dick")
        await ctx.send(f'{ loc }  {username}:\n{str_send}')

   


    #ERROR HANDLERS   -----------------------------------------------------------------------------------------------------------

    @question.error
    async def question_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            loc = await locales.get_locale_content(ctx.guild.name, "ERROR_question")
            await ctx.send( loc )

    @dick.error
    async def dick_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            loc = await locales.get_locale_content(ctx.guild.name, "ERROR_dick")
            await ctx.send( loc )


#SETUP   -----------------------------------------------------------------------------------------------------------
def setup(bot):
    bot.add_cog( fun( bot ) ) 
