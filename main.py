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
    
        # run the bot
    async with client:
        await load_extensions()
        await client.start(config.BOT_TOKEN)

asyncio.run(main())

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")
    
    # load all cogs
    async def load_extensions():
        for folder in os.listdir("cogs"):
            if os.path.exists(os.path.join("cogs", folder, "cog.py")):
                await client.load_extension(f"cogs.{folder}.cog")
                
    async def on_message(message):
        if "https://media.discordapp.net" in message.content :
            x = message.content.replace("https://media.discordapp.net" , "https://cdn.discordapp.com")
        await message.reply(x)
        
    @client.command()
    async def ping(ctx):
        await ctx.send(f'Pong! {round (client.latency * 1000)} ms')


if __name__ == "__main__":
    main()
