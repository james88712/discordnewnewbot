import discord, asyncio
import random
import datetime
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print(client.user.id)
    print("봇이 시작되었습니다")
    Game = discord.Game('유저들과 소통 중')
    await client.change_presence(status=discord.Status.online, activity=Game)


@client.event
async def on_message(message):
    if message.content.startswith('!스마트 인증'):
        author = message.guild.get_member(int(message.author.id))
        role = discord.utils.get(message.guild.roles, name="인증시민")
        await author.add_roles(role)
        #await message.channel.send('대고양 인증 완료')
        #my_name = discord.utils.get(message.guild.members, name='Asus')
        #await message.channel.send(':white_check_mark: 인증이 완료되었습니다\n\n인증 담당:{}'.format(my_name.mention))

    if message.content.startswith('!스마트 인증'):
        embed=discord.Embed(title=':white_check_mark: 인증이 완료되었습니다', description='', color=0x00ff56)
        embed.add_field(name='Welcome To Smart Server', value='고유번호ㅣ직업ㅣ닉네임 형식으로 닉네임 바꿔주세요!', inline=False)
        await message.channel.send(embed=embed)


client.run('NzE1ODg0OTEwMzg0MjUwODgw.XtDvYQ.wl6GNDXe8t14wk6CK69Cy8-vNFo')
         