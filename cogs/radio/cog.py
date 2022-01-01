from discord.ext import commands
from .radio_view import RadioView
from .cs_view import csView
import discord

class RadioCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """When the bot is ready, load the view"""
        self.__bot.add_view(RadioView(ctx))
        self.__bot.add_view(csView())
        print("Button view added")

    @commands.command(aliases=["p","radio"])
    async def play(self, ctx: commands.Context):
        embed=discord.Embed(title="Radio Station", description="Select station to start the radio", color=0xff0000)
        embed.set_author(name="Asia Dream Radio", url="https://asiadreamradio.torontocast.stream/", icon_url="https://cdn.discordapp.com/attachments/613417127143014520/926569774824181791/Asia_Dream_Radio.png")
        await ctx.send(embed=embed, view=RadioView())

    @commands.command(aliases=["currentsong","np","nowplaying"])
    async def cs(self, ctx: commands.Context):
        embed=discord.Embed(title="Radio Station", description="Select station to see current song ", color=0xff0000)
        embed.set_author(name="Asia Dream Radio", url="https://asiadreamradio.torontocast.stream/", icon_url="https://cdn.discordapp.com/attachments/613417127143014520/926569774824181791/Asia_Dream_Radio.png")
        await ctx.send(embed=embed, view=csView())

# setup functions for bot
def setup(bot):
    bot.add_cog(RadioCog(bot))
