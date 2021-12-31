from disscord.ext import commands
from .Radio import RadioView


class RadioCog(commands.Cog, name="Radio"):

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """When the bot is ready, load the view"""
        self.__bot.add_view(RadioView())
        print("Radio Button view added")

    @commands.command()
    async def roles(self, ctx: commands.Context):
        await ctx.send("Click a button to add or remove a role.", view=RadioView())


# setup functions for bot
def setup(bot):
    bot.add_cog(RadioCog(bot))
