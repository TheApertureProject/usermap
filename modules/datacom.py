import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import json

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

class Datacom(commands.Cog):
    
    def __init__(self, bot):
    self.bot = bot
    self.config = bot.config

def setup(bot):
    bot.add_cog(Datacom(bot))
