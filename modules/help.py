import json
import discord
from discord.ext import commands

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

VERSION = config["version"]
PREFIX = config["prefix"]
BOT_ID = config["client_id"]
SERVER_INVITE = config["server_invite"]
prefiximg = ':prefiximg:612474539120525312'

bot = commands.Bot(command_prefix=PREFIX)


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command(aliases=["information", "about"])
    async def info(self, ctx):
        e = discord.Embed(title="$usermap", description=f"Un robot d'analyse pour votre serveur. Version : {VERSION}")
        e.add_field(name='✨ Liens utiles', value='[Lien d\'invite](http://bit.ly/2uIQwmh) | [Serveur de support](https://discord.gg/H7ZcCB) | [Site web du développeur](https://apertureproject.me/)')
        e.set_image(url='https://cdn.discordapp.com/attachments/683756494369587200/683798154667098122/usermap_banner-01_2.png')
        await ctx.send(embed=e)

    @commands.command(aliases=["aide"])
    async def help(self, ctx):
        e = discord.Embed(title="Liste des commandes", description="usage : tapez `$<nom de la commande>` en retirant les crochets.")
        e.add_field(name='✨ Aide', value="""`info` : En savoir plus sur moi
        `help` : Affiche la liste de mes commandes""")
        e.add_field(name='✨ Aide', value="""`scan-user` : Effectue une recherche des rapports associés à l'utilisateur spécifié
        `scan-server` : Effectue une analyse complète des paramètres du serveur""")
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Help(bot))
