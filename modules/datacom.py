import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import json
import os

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

DB_USERNAME = os.environ["DBUSERNAME"]
DB_PASSWORD = os.environ["DBPASSWORD"]

client = MongoClient(f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@usermap-duaqm.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.dis_user

class Datacom(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command(aliases=['check', 'search', 'recherche', 'rechercher'])
    async def search(self, ctx, playerid:int):
        user1 = db.reported_user.find_one({'u_id' : playerid})
        if user1 == "None":
            a = discord.Embed(title="Résultat de la recherche", description="❌ Aucune entrée associée à cet ID n'a pu être identifiée.", color=0xffff00)
            await ctx.send(embed=a)
        else:
            UNAME = user1["u_name"]
            UID = user1["u_id"]
            UARTICLES = user1["u_articles"]
            UINFRINGMENT = user1["u_infringment"]
            ULEVEL = user1["u_level"]

            e = discord.Embed(title="Résultat de la recherche", description="✨ Une entrée a été trouvée. Consultez la suite du rapport pour plus de détails")

            e.add_field(name=f"Rapport de l'utilisateur `{UNAME}`", value=f"""Niveau : `{ULEVEL}`
            Articles enfreints (`{len(UARTICLES)}`) : `{UARTICLES}`
            Détails : {UINFRINGMENT}""")

            if ULEVEL == 1:
                bannerurl="http://bit.ly/38gY1i2"
            elif ULEVEL == 2:
                bannerurl="http://bit.ly/38hmweM"
            else:
                bannerurl="http://bit.ly/2IcJzNq"
            
            e.set_image(url=bannerurl)

            await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Datacom(bot))
