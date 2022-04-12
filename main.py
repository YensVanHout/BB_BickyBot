import discord
import os
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name="voor meer informatie gebruik !bb help"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bb help'):
      msg = """Bicky Bot ondersteunt momenteel de volgende commands:
`!bb socials`: Krijg de huidige social media links van Bickychips.
`!bb welk`: probeer deze maar eens uit voor jezelf"""
      await message.channel.send(msg)
    
    if message.content.startswith('!bb hallo'):-=
      msg = 'Helaba {0.author.mention}'.format(message)
      await message.channel.send(msg)

    if message.content.startswith('!bb socials'):
      msg = """Hier zijn alle social media link van BickyChips:
Instagram: https://www.instagram.com/bickychips/
Twitch: https://www.twitch.tv/bickychips_
Twitter: https://twitter.com/KellGraphy
Discord: https://discord.gg/uBDTGuMhqQ
Tiktok: https://www.tiktok.com/@bickychips
"""
      await message.channel.send(msg)

    if message.content.startswith("!bb welk"):
      msg = "das hier wel in het antwaarps he"
      await message.channel.send(msg)

    if message.content.startswith("!bb support"):
      msg = "Ping @Bulletje, Hij zal het wel regelen, waarschijnlijk..."
      await message.channel.send(msg)

keep_alive()
client.run(os.getenv('TOKEN'))