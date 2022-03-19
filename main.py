import os
import discord
from discord.ext import commands
import config


def main():
    # allows privledged intents for monitoring members joining, roles editing, and role assignments
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    client = commands.Bot(command_prefix=config.PREFIX, intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    # load all cogs
    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            client.load_extension(f"cogs.{folder}.cog")
            
    @client.command()
    async def ping(ctx):
        await ctx.send(f'Pong! {round (client.latency * 1000)} ms')

    @client.event
    async def on_message(message):
        if "https://media.discordapp.net" in message.content :
            x = message.content.replace("https://media.discordapp.net" , "https://cdn.discordapp.com")
            await message.reply(x)

    # run the bot
    client.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()
