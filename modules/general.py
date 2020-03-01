import json

from discord.ext import commands

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

SERVER_INVITE = config["server_invite"]

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong !')

    @commands.command()
    async def pong(self, ctx):
        await ctx.send('Ping !')

    @commands.command(aliases=['support'])
    async def join(self, ctx):
        await ctx.send(f'✨ Serveur de support : {SERVER_INVITE}')

    @commands.command(aliases=['add'])
    async def invite(self, ctx):
        await ctx.send(
            f'✨ Lien d'ajout : <http://bit.ly/2uIQwmh>')

def setup(bot):
    bot.add_cog(General(bot))
