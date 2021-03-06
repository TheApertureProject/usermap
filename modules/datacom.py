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

    @commands.command(aliases=['check', 'recherche', 'rechercher', 'scan'])
    async def search(self, ctx, playerid:int):
        z = discord.Embed(title = "<a:loading:684031670520643640> Recherche en cours")
        y = await ctx.send(embed = z)
        user1 = db.reported_user.find_one({'u_id' : playerid})
        if user1 is None:
            a = discord.Embed(title="❌ Aucune entrée associée à cet ID n'a été trouvée")
            await y.edit(embed=a)
        else:
            UNAME = user1["u_name"]
            UID = user1["u_id"]
            UARTICLES = user1["u_articles"]
            UINFRINGMENT = user1["u_infringment"]
            ULEVEL = user1["u_level"]

            e = discord.Embed(title="Résultats de la recherche", description="✨ Une entrée a été trouvée. Consultez la suite du rapport pour plus de détails, et [notre charte](https://discord.gg/3UPQZN) pour connaître le contenu des articles enfreints.")
            
            a = f"""Niveau : `{ULEVEL}`
            Articles enfreints (x{len(UARTICLES)}) : `{UARTICLES}`
            Détails : {UINFRINGMENT}"""
            cremoval = "[]'\""
            for c in cremoval:
                a = a.replace(c, "")
            
            e.add_field(name = f"Rapport de l'utilisateur `{UNAME}`", value = a)
            if ULEVEL == 1:
                bannerurl="http://bit.ly/38gY1i2"
            elif ULEVEL == 2:
                bannerurl="http://bit.ly/38hmweM"
            else:
                bannerurl="http://bit.ly/2IcJzNq"
            
            e.set_image(url=bannerurl)

            await y.edit(embed=e)


            @commands.command(aliases=["rapport"])
            async def report(self, ctx, playerid:int, playername, link, infringment):
                e = discord.Embed(title=f"Rapport pour l'utilisateur {playername}", description=f"""ID : {playerid}
                Raison : {infringment}""")
                e.set_image(url=link)
                y = await ctx.send(embed = z)
                z = discord.Embed(title = "<a:loading:684031670520643640> Envoi du rapport en cours")


def setup(bot):
    bot.add_cog(Datacom(bot))
