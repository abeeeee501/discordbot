#招待するときはこのURL
# https://discord.com/api/oauth2/authorize?client_id=949467065708859432&permissions=0&scope=bot

# インストールした discord.py を読み込む
import os
import traceback
from re import A

import discord
from discord.ext import commands

from modules.grouping import MakeTeam

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'OTQ5NDY3MDY1NzA4ODU5NDMy.YiKyHA.PC5ihGKkOJYCfRX5FXmWqK4HgVY'

# 接続に必要なオブジェクトを生成
bot = commands.Bot(command_prefix='/')


# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@bot.command()
async def team(ctx,specified_num=2):
    make_team = MakeTeam()
    remainder_flag = 'true'
    msg = make_team.make_party_num(ctx,specified_num,remainder_flag)
    await ctx.channel.send("チーム分け")
    await ctx.channel.send(msg)

@bot.command()
async def group(ctx,specified_num=1):
    make_team = MakeTeam()
    msg = make_team.make_specified_len(ctx,specified_num)
    await ctx.channel.send("チーム分け(人数指定)")
    await ctx.channel.send(msg)

# メッセージ受信時に動作する処理

@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 特定のコマンドに対して返信
    if message.content == '!hanketsu':
        await message.channel.send('https://clips.twitch.tv/LivelyIncredulousMoonWholeWheat-nxT6BhW9jYPLCtD0')

    if message.content == '!judge':
        await message.channel.send('https://www.twitch.tv/jasper7se/clip/CheerfulLongTroutRiPepperonis-MPsoMZ0qeW8ciZjB')

    if message.content == '!shortchinko':
        await message.channel.send('https://www.twitch.tv/fps_shaka/clip/GentleKitschyPoxPMSTwin-YXEX0lRl3C29nv4o')

    if message.content == '!manko':
        await message.channel.send('https://www.twitch.tv/jasper7se/clip/HelplessSmokyMooseHeyGuys-_9aGisrDy1oIXrWC')

    if message.content == '!help':
        await message.channel.send('!team[チーム数] → 均等に分ける　!group[メンバー数] → 指定したメンバー数で作成')



# Botの起動とDiscordサーバーへの接続
bot.run(TOKEN)