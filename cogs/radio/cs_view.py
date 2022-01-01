from discord.ui import Button, View
import discord
import requests , json , isodate , urllib.parse, urllib3
from discord import FFmpegPCMAudio
import datetime
urllib3.disable_warnings()

x = open('cogs/radio/radio.json', encoding="utf-8")
ADR = json.load(x)


class csView(View):
    def __init__(self,):
        super().__init__(timeout=None)
    async def handle_click(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        args = button.custom_id
        i = ADR[0]['sub'].index(args)
        if args in ADR[0]['sub'] and args != "csjazz" and args != "csjxmas":
            getjson = requests.get(ADR[0]['cslink'][i], verify=False)
            text = getjson.text
            xcs = json.loads(text)
            songtitle = xcs["m_Item2"]["Title"]
            songpic = xcs["m_Item2"]["Picture"]
            artist = xcs["m_Item2"]["Artist"]
            timestamp = isodate.parse_duration(xcs["m_Item2"]["Duration"])  # need converting -_-
            embed = discord.Embed(title="Now Playing :", color=0x00ffee)
            embed.set_author(name=str(ADR[0]['s'][i]) , url=ADR[0]['slink'][i] ,  icon_url=ADR[0]['logo'][i])
            embed.set_thumbnail(url=songpic)
            embed.add_field(name=artist, value="["+songtitle+"]"+"("+"https://www.google.com/search?q="+urllib.parse.quote_plus(artist+" "+songtitle)+")", inline=True)
            embed.set_footer(text=str(timestamp)[2:7])
            await interaction.response.edit_message(embed=embed)     
        elif args == "csjazz":
            getjson = requests.get(ADR[0]['cslink'][i], verify=False)
            text = getjson.text
            xcs = json.loads(text)
            songtitle = xcs["results"][0]["title"]
            songpic = xcs["results"][0]["img_url"]
            artist = xcs["results"][0]["author"]
            timestamp = str(datetime.timedelta(milliseconds=xcs["results"][0]["length"]))
            embed = discord.Embed(title="Now Playing :", color=0x00ffee)
            embed.set_author(name=str(ADR[0]['s'][i]) , url=ADR[0]['slink'][i] ,  icon_url=ADR[0]['logo'][i])
            embed.set_thumbnail(url=songpic)
            embed.add_field(name=artist, value="["+songtitle+"]"+"("+"https://www.google.com/search?q="+urllib.parse.quote_plus(artist+" "+songtitle)+")", inline=True)
            embed.set_footer(text=str(timestamp)[2:7])
            await interaction.response.edit_message(embed=embed)  
        elif args == "csjxmas":
            embed = discord.Embed(title="-_-", color=0x00ffee)
            await interaction.response.edit_message(embed=embed)  



    @discord.ui.button(
        emoji='<:JapanHits:925911131405553717>',
        style=discord.ButtonStyle.primary , 
        custom_id='csjhits',
        row=0
        )
    async def jhits_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @discord.ui.button(
        emoji='<:JPopPowerplay:925911524969680987>', 
        style=discord.ButtonStyle.primary , 
        custom_id='csjpop',
        row=0
        )     
    async def jpop_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @discord.ui.button(
        emoji='<:JPopPowerplayKawaii:925911698051850300>', 
        style=discord.ButtonStyle.primary , 
        custom_id='csjkawaii',
        row=0
        )
    async def jkawaii_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @discord.ui.button(
        emoji='<:JPopSakura:925911772769189959>', 
        style=discord.ButtonStyle.primary , 
        custom_id='csjsakura',
        row=1
        )
    async def jsakura_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @discord.ui.button(
        emoji='<:JRockPowerPlay:925911862544040036>', 
        style=discord.ButtonStyle.primary , 
        custom_id='csjrock',
        row=1
        )
    async def jrock_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @discord.ui.button(
        emoji='<:JClubPowerplayHipHop:925911962611744778>', 
        style=discord.ButtonStyle.primary , 
        custom_id='csjclub',
        row=1
        )
    async def jclub_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @discord.ui.button(
        emoji='<:JazzSakura:925912050310475817>', 
        style=discord.ButtonStyle.primary , custom_id='jazzs',row=2)
    async def jazzs_button(self, button, interaction):
        await self.handle_click(button, interaction)     
        
    @discord.ui.button(
        emoji='<:JazzClubBandstand:925912245362376775>', 
        style=discord.ButtonStyle.primary , 
        custom_id='csjazz',
        row=2
        )
    async def jazz_button(self, button, interaction):
        await self.handle_click(button, interaction)    

    @discord.ui.button(
        emoji='<:JPopChristmasRadio:925912419698634843>', 
        style=discord.ButtonStyle.primary , 
        custom_id='csjxmas',
        row=2
        )
    async def jxmas_button(self, button, interaction):
        await self.handle_click(button, interaction)

    async def on_error(self, error, Item, Interaction) -> None:
            return await Interaction.response.send_message(str(error),ephemeral = True)
