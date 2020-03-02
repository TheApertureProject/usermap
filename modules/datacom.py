import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import json
import os

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

DB_USERNAME = os["DBUSERNAME"]
DB_PASSWORD = os["DBPASSWORD"]

client = MongoClient(f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@usermap-duaqm.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.dis_user

class Datacom(commands.Cog):
    
    def __init__(self, bot):
    self.bot = bot
    self.config = bot.config

    @commands.command(aliases=['check', 'search', 'recherche', 'rechercher']
    async def search(self, ctx, playerid:int):
        user1 = db.reported_user.find_one({'u_id' : playerid})
        if user1 = "None":
            await ctx.send(embed = discord.Embed(description=":warning: Aucune entrée associée à cet ID n'a pu être identifiée.", color=0xffff00)
        else:
            e = discord.Embed(description="")

def setup(bot):
    bot.add_cog(Datacom(bot))
