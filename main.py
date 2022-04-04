import discord
from discord.ext import commands
import datetime
import asyncio
import os , re
import heroku3
from discord import Webhook, AsyncWebhookAdapter
import aiohttp

client = commands.Bot(command_prefix="..")

@client.event
async def on_ready():
    print("ready")
    chnl = client.get_channel(int(os.getenv("logChannel"))) 
    today = datetime.datetime.now()
    switchTime = today + datetime.timedelta(hours=23)
    sleepTime = (switchTime.timestamp() - today.timestamp())
    heroku_conn = heroku3.from_key(os.getenv("KEY"))
    app = heroku_conn.app('xzbot-0')
    app.process_formation()['worker'].scale(0)
    await chnl.send("xzbot-0 OFF \nLog Ready ")
    await asyncio.sleep(sleepTime)
    await chnl.send("switch xzbot-1 > xzbot-0")
    app.process_formation()['worker'].scale(1)
@client.event
async def on_message_delete(msg):
    if msg.author.bot: return
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(os.getenv("Webhook"), adapter=AsyncWebhookAdapter(session))
        await webhook.send(msg.content, username=msg.author.name,avatar_url=msg.author.avatar_url,files=[await f.to_file() for f in msg.attachments]) 

@client.event
async def on_message(msg):
    if msg.author.bot: return
    if "https://media.discordapp.net/" in msg.content:
    #Checking if a webhook exists
        webhook = discord.utils.get(await msg.channel.webhooks(), name=client.user.name)
        if webhook is None:
        # If the webhook didn't exist, we create one
            webhook = await msg.channel.create_webhook(name=client.user.name) 
        x = msg.content.split()
        r = re.compile('https?.*?\.mp?4$')
        output = list(filter(r.match, x))
        if len(output) != 0:
            await webhook.send(msg.content.replace("https://media.discordapp.net/","https://cdn.discordapp.com/"),username=msg.author.name,avatar_url=msg.author.avatar_url)
            await msg.delete()
        return
    await client.process_commands(msg)

@client.command()
async def ping(ctx):
    await ctx.reply(f"Pong! {round(client.latency * 1000)}ms")

client.run(os.getenv("TOKEN"))
