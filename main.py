import discord
from discord.ext import commands
import datetime
import time
import os
import heroku3

client = commands.Bot(command_prefix="..")

@client.event
async def on_ready():
  print("ready")
  chnl = client.get_channel(579101262893809684) 
  today = datetime.datetime.now()
  switchTime = today + datetime.timedelta(minutes=1)
  sleepTime = (switchTime.timestamp() - today.timestamp())
  heroku_conn = heroku3.from_key(os.getenv("KEY"))
  app = heroku_conn.app('xzbot-0')
  app.process_formation()['worker'].scale(0)
  await chnl.send("xzbot-0 OFF ")
  time.sleep(sleepTime)
  await chnl.send("switch xzbot-1 > xzbot-0")
  app.process_formation()['worker'].scale(1)

@client.event
async def on_message_delete(msg):
  chnl = client.get_channel(579101262893809684)

  await chnl.send(msg.content,files=[await f.to_file() for f in msg.attachments])
  
@client.command()
async def ping(ctx):
  await ctx.reply(f"Pong {client.latecy}")

  
client.run(os.getenv("TOKEN"))
