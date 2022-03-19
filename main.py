import os
import discord
from discord.ext import commands
import config


async def main():
    # allows privledged intents for monitoring members joining, roles editing, and role assignments
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    client = commands.Bot(command_prefix=config.PREFIX, intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    # load all cogs
    async def load_extensions():
        for folder in os.listdir("cogs"):
            if os.path.exists(os.path.join("cogs", folder, "cog.py")):
                await client.load_extension(f"cogs.{folder}.cog")

    # run the bot
    async with client:
        await load_extensions()
        await client.start(config.BOT_TOKEN)

asyncio.run(main())

if __name__ == "__main__":
    main()
