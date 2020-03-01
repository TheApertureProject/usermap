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
        e = discord.Embed(title="$username", description="Un robot à but sécuritaire et informatif")
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Help(bot))
