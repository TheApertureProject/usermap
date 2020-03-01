import asyncio
import json
import logging
import os
import sys
import discord
from discord.ext import commands

print('All modules successfully imported.')

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

logging.basicConfig(level='INFO')

PREFIX = config["prefix"]
MODULES = config["modules"]
OWNER = config["owner_id"]
VERSION = config["version"]
TOKEN = os.environ["TOKEN"]

bot = commands.Bot(command_prefix=[PREFIX])

bot.config = config
bot.ready = False


async def status():
    while True:
        names = [f'\'{PREFIX}help\' !', f'servir {len(bot.guilds)} serveurs', f'observer {len(bot.users)} utilisateurs']
        for name in names:
            await bot.change_presence(activity=discord.Game(name=name))
            await asyncio.sleep(120)


@bot.event
async def on_connect():
    print('Successfully connected !')


@bot.event
async def on_ready():
    loaded = len(MODULES)
    bot.remove_command('help')
    for module in MODULES:
        try:
            logging.info('Loading %s', module)
            bot.load_extension(f'modules.{module}')
        except Exception as e:
            logging.exception('Failed to load {} : {}'.format(module, e))
    print('Logged in.')
    print('{}/{} modules loaded'.format(loaded, len(MODULES)))
    print(f'discord.py lib version : {discord.__version__}')
    bot.loop.create_task(status())


bot.run(TOKEN)
