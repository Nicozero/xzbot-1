import discord
from discord.ext import commands
import datetime
import asyncio
import os
import heroku3
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
client = commands.Bot(command_prefix="..")

@client.event
async def on_ready():
  print("ready")
  chnl = client.get_channel(579101262893809684) 
  today = datetime.datetime.now()
  switchTime = today + datetime.timedelta(days=10)
  sleepTime = (switchTime.timestamp() - today.timestamp())
  heroku_conn = heroku3.from_key(os.getenv("KEY"))
  app = heroku_conn.app('xzbot-0')
  app.process_formation()['worker'].scale(0)
  await chnl.send("xzbot-0 OFF ")
  await asyncio.sleep(sleepTime)
  await chnl.send("switch xzbot-1 > xzbot-0")
  app.process_formation()['worker'].scale(1)

@client.event
async def on_message_delete(msg):
  if msg.channel.id == 956636986150617211 :
    return
  if msg.author.bot: return
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url('https://discord.com/api/webhooks/956638174073983076/u4toNNrti5srgIGKYBdem6ePcuYAilg9aD_1Y2AZcjzBQo0ZqN9apbYwjNcYacUxKkcB', adapter=AsyncWebhookAdapter(session))
    await webhook.send(msg.content, username=msg.author.name,avatar_url=msg.author.avatar_url,files=[await f.to_file() for f in msg.attachments]) 
    
@client.command()
async def ping(ctx):
  await ctx.reply(f"Pong! {round(client.latency * 1000)}ms")

  
client.run(os.getenv("TOKEN"))
