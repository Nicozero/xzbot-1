import json
import discord
import asyncio
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands import Bot

x = open('cogs/radio/radio.json', encoding="utf-8")
ADR = json.load(x)
bot = Bot('')
class RadioView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) 
    async def handle_click(
        self, button: discord.ui.Button, interaction: discord.Interaction 
    ):
        global player
        args = button.custom_id
        uservc = interaction.user.voice
        botvc = interaction.message.author.voice
        x = ADR[0]['sub']
        
        if not uservc:
            await interaction.response.send_message("Connect to a Voice Channel to start the radio",ephemeral=True)
        if botvc  is None:
            channel = uservc.channel
            player = await channel.connect()
            botvc = interaction.message.author.voice
        if uservc is not None and botvc.channel is not None:
            if args in x:            
                i = x.index(args)
                if uservc.channel == botvc.channel:
                    if player.is_playing():
                        player.stop()
                    player.play(
                        FFmpegPCMAudio(
                            ADR[0]["rlink"][i]
                        )
                    )
                    embed = discord.Embed(title="Radio Playing", color=0x00ffee)
                    embed.set_author(name=str(ADR[0]['s'][i]) , url=ADR[0]['slink'][i] ,  icon_url=ADR[0]['logo'][i])
                    await interaction.response.edit_message(embed=embed)
                else:
                    await interaction.response.send_message("<:MochaSweat:648458974424858644>",ephemeral=True)
        if args == 'leave':
            if interaction.guild.voice_client is None:
                await interaction.response.send_message("Test 1",ephemeral=True)
                return
            if uservc is not None and botvc.channel is not None:
                if uservc.channel == botvc.channel:
                    player.stop()
                    embed = discord.Embed(title="Radio disconnected", color=0x00ffee)
                    embed.set_author(name=interaction.message.author.name,  icon_url=interaction.message.author.avatar)
                    await interaction.response.edit_message(embed=embed)   
                    await interaction.guild.voice_client.disconnect(force=True)   
            else:
                await interaction.response.send_message("<:MochaSweat:648458974424858644>",ephemeral=True)
                
      
    @discord.ui.button(
        emoji='<:JapanHits:925911131405553717>',
        style=discord.ButtonStyle.primary , 
        custom_id='jhits', 
        row=0
        )
    async def jhits_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @discord.ui.button(
        emoji='<:JPopPowerplay:925911524969680987>', 
        style=discord.ButtonStyle.primary , 
        custom_id='jpop', 
        row=0
        )     
    async def jpop_button(self, button, interaction):
        await self.handle_click(button, interaction)     

    @discord.ui.button(
        emoji='<:JPopPowerplayKawaii:925911698051850300>', 
        style=discord.ButtonStyle.primary , 
        custom_id='jkawaii', 
        row=0
        )
    async def jkawaii_button(self, button, interaction):
        await self.handle_click(button, interaction)     

    @discord.ui.button(
        emoji='<:JPopSakura:925911772769189959>', 
        style=discord.ButtonStyle.primary , 
        custom_id='jsakura',
        row=1
        )
    async def jsakura_button(self, button, interaction):
        await self.handle_click(button, interaction)     

    @discord.ui.button(
        emoji='<:JRockPowerPlay:925911862544040036>', 
        style=discord.ButtonStyle.primary , 
        custom_id='jrock',
        row=1
        )
    async def jrock_button(self, button, interaction):
        await self.handle_click(button, interaction)     

    @discord.ui.button(
        emoji='<:JClubPowerplayHipHop:925911962611744778>', 
        style=discord.ButtonStyle.primary , 
        custom_id='jclub',
        row=1
        )
    async def jclub_button(self, button, interaction):
        await self.handle_click(button, interaction)    

    @discord.ui.button(
        emoji='<:JazzSakura:925912050310475817>', 
        style=discord.ButtonStyle.primary , 
        custom_id='jazzs',
        row=2
        )
    async def jazzs_button(self, button, interaction):
        await self.handle_click(button, interaction)   

    @discord.ui.button(
        emoji='<:JazzClubBandstand:925912245362376775>', 
        style=discord.ButtonStyle.primary , 
        custom_id='jazz',
        row=2
        )
    async def jazz_button(self, button, interaction):
        await self.handle_click(button, interaction)    

    @discord.ui.button(
        emoji='<:JPopChristmasRadio:925912419698634843>', 
        style=discord.ButtonStyle.primary , 
        custom_id='jxmas',
        row=2
        )
    async def jxmas_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @discord.ui.button(
        emoji='<a:nyanleave:805172204525322250>', 
        style=discord.ButtonStyle.primary , 
        custom_id='leave',
        row=2
        )
    async def leave_button(self, button, interaction):
        await self.handle_click(button, interaction)
