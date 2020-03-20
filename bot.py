#IMPORTS
import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import secret
import json


#DECLARATIONS
bot = commands.Bot(command_prefix = '.')
status = cycle(['Plague Inc: Corona update', 'God', 'monkey killer simulator', 'UU AA UU AA', 'corona', 'killing jews'])

LOCALE_GUILD_METADATA_FILE = './locales/locales.json'

########## EVENTS  ##########
@bot.event
async def on_ready():
    update_status.start()
    await clear_cache()

    print("Carla is ready")

@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@bot.event
async def on_member_remove(member):   
    print(f'{member} has been removed from a server.')




########### TASKS ############
@tasks.loop(seconds = 300)
async def update_status():
    await bot.change_presence(activity=discord.Game(next(status)))



########### COMMANDS ############
@bot.command()
async def reload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print(filename)
            if filename == "locales.py":
                return
            try:
                bot.unload_extension(f'cogs.{filename[:-3]}')
                bot.load_extension(f'cogs.{filename[:-3]}')
            except Exception:
                print("ERROR: Could not reload COGS")
    await clear_cache()

@bot.command()
async def set_locale(ctx, locale_code): 
    locale_data = {}

    with open(LOCALE_GUILD_METADATA_FILE) as json_file:
        locale_data = json.load(json_file)     


    with open(LOCALE_GUILD_METADATA_FILE, 'w') as outfile:
        locale_data["guilds"][ctx.guild.name] = locale_code
        json.dump(locale_data, outfile)


############ UTIL ###############
async def clear_cache():
    for filename in os.listdir('./cogs/cache'):
        with open("./cogs/cache/" + filename,"r+") as file:
            file.truncate(0)
            file.close()

#MAIN
if __name__ == "__main__":
    
    #Load COGS
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            if filename != "locales.py":
                bot.load_extension(f'cogs.{filename[:-3]}')

    #Run Bot
    bot.run(secret.DISCORD_TOKEN)