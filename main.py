# bot.py
import os
import discord
from discord.ext.commands import Bot
import random

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = Bot(command_prefix='donut')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Game(name='baking dofnuts'))

    print(f'{client.user} is connected to the following guilds:')
    for guild in client.guilds:
        print(f'-{guild.name}(id: {guild.id})')


# list of all donut gifs
donutgifs = [
    'https://media.giphy.com/media/H21AQys677CJa/giphy.gif',
    'https://media.giphy.com/media/tx8emQv1s5AtO/giphy.gif',
    'https://media.giphy.com/media/gpZsmrh1eXUXK/giphy.gif',
    'https://media.giphy.com/media/26gsf19j60Wh8GlcQ/giphy.gif',
    'https://media.giphy.com/media/nQxAUnnkBuve0/giphy.gif',
    'https://media.giphy.com/media/xUA7b3PacjKdugYSY0/giphy.gif',
    'https://cdn.discordapp.com/attachments/663078827559485440/751074592587513946/donut.png',
    'https://media.giphy.com/media/3o7abqPKlcPasOJGBG/giphy-downsized.gif',
    'https://media.giphy.com/media/QNEOp2iwL2vBK/giphy.gif',
    'https://media.giphy.com/media/l0Iy47Iotb2nSvz7W/giphy.gif',
    'https://media.giphy.com/media/o9ngTPVYW4qo8/giphy.gif',
    'https://media.giphy.com/media/l4FGHzb9sBnQmYjyU/giphy.gif',
    'https://media.giphy.com/media/l0Ex70JtCTlJju9ag/giphy.gif',
    'https://media.giphy.com/media/fp1wbNlFeSJ20/giphy.gif',
    'https://media.giphy.com/media/570ib2lp8v3Gw/giphy.gif',
    'https://media.giphy.com/media/gKwX7LPlrvOdcXN89k/giphy.gif',
    'https://media.giphy.com/media/bd4td7PlhYY9i/giphy.gif',
    'https://media.giphy.com/media/m7CK3OXVqzYwE/giphy.gif',
    'https://media.giphy.com/media/VgvG23g9HPspa/giphy.gif',
    'https://media.giphy.com/media/26BncfNdy3JsIVgmQ/giphy.gif',
    'https://media.giphy.com/media/l3q2B4Mlsw4HFpVE4/giphy.gif',
    'https://media.giphy.com/media/26gsi3ERLWoTGjpHa/giphy.gif',
    'https://media.giphy.com/media/rGTcp3k79Tu8w/giphy.gif',
    'https://media.giphy.com/media/3oKIPCBcZs82sv9nsQ/giphy.gif',
    'https://media.giphy.com/media/l4KhY0teBwlTWKTra/giphy.gif',
    'https://media.giphy.com/media/zOMS8OvDMRvOM/giphy.gif',
    'https://media.giphy.com/media/g0delle0tz7AH4nXex/giphy.gif',
    'https://media.giphy.com/media/4JWjgdvchEo0jrSERA/giphy.gif',
    'https://media.giphy.com/media/57LwtRGoPTDVu/giphy.gif',
    'https://media.giphy.com/media/l3q2JPDUpIYB1D9M4/giphy.gif'
]


@client.event
async def on_message(message):
    # keine Bots
    if message.author == client.user:
        return

    # Bot Erwähnung -> donut
    if '<@!750728974304411648>' in message.content:
        await message.channel.send('donut')
        print('mentioned by ' + str(message.author))

    # zufälliges donut gif senden
    if 'donut' in message.content:
        embed = discord.Embed(title="", url="",
                              description="", color=0xe73887)
        embed.add_field(name="Here is your Donut", value="DONUT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", inline=False)
        donut = random.choice(donutgifs)
        embed.set_image(url=donut)
        embed.set_footer(text="donut requested by and delivered to " + str(message.author))
        await message.channel.send(embed=embed)
        print('donut requested by and delivered to ', message.author)

    # do not nut -> ok
    if message.content == 'do not nut':
        await message.channel.send('🍩k')
        print('not nut')

    if message.content == 'pls beg':
        afk = random.randint(1, 1000)
        print(afk)
        if afk == 1:
            embed = discord.Embed(title="", url="",
                                  description="", color=0xe73887)
            embed.add_field(name="I have no coins but you can have a donut.", value="!very rare event!", inline=False)
            donut = random.choice(donutgifs)
            embed.set_image(url=donut)
            embed.set_footer(text="donut requested by and delivered to " + str(message.author))
            await message.channel.send(embed=embed)
            await message.channel.pin_message(client)
            print('!very rare event occured! triggered by ', str(message.author))

    if message.content == 'members':
        count = len(message.author.guild.members)
        await message.channel.send(f'```{count} members in this guild```')
        print(f'members counted by {message.author}')

    if message.content == 'member list':
        members = '\n - '.join([member.name for member in message.author.guild.members])
        count = len(message.author.guild.members)
        await message.channel.send(f'```{count} members in this guild: \n - s{members}```')
        print(f'members listed by {message.author}')


client.run(TOKEN)
