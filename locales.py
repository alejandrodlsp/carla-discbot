import os
import json


LOCALE_GUILD_METADATA_FILE = './locales/locales.json'

LOCALE_PATHS = {
    'es' : './locales/es.json',
    'en' : './locales/en.json'
}


async def get_locale(guild_name):
    locale_code = 'en'
    with open(LOCALE_GUILD_METADATA_FILE) as json_file:
        locale_data = json.load(json_file)     
        locale_code = locale_data["guilds"][guild_name] or "en"

    return locale_code


async def get_locale_content(guild_name, content_id):
    locale_code = await get_locale(guild_name)
    locale_file_path = LOCALE_PATHS[locale_code]

    if os.path.isfile(locale_file_path) and locale_file_path:
        with open(locale_file_path) as json_file:
            locale_data = json.load(json_file)
            return locale_data[content_id] or "LOCALE ERROR"
    else:
        print(f"LOCALE ERROR, could not load locale file for {locale_code}")
        return "LOCALE ERROR"

