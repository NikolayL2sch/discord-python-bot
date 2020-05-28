import discord
import math
import random
from discord.ext import commands

TOKEN = 'NzE0NTg0MzUwNTA2NzQ1ODc2.Xsw2Eg.992z6mKK_GQtJYq06F9WYZ94n3c'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready ():
    print("READY!!!......")

@client.event
async def on_member_join(member):
    print (f'{member} has joined the server.')

@client.event
async def on_member_removed(member):
    print (f'{member} has left the server.')

@client.command(aliases = ['easytask','etask','e_task','easy_t','easyt'])
async def easy_task (ctx):
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,100)
    out = str(a)+"+"+str(b)+"*"+str(c)
    await ctx.send (out)

@client.command(aliases = ['inf','infa','info','i','probability','if'])
async def _8ball(ctx,*,question):
    responses = ['Бесспорно',
    'Однозначно',
    'Никаких сомнений',
    'Определённо да',
    'Можешь быть уверен в этом',
    'Мне кажется — «да»',
    'Вероятнее всего',
    'Хорошие перспективы',
    'Знаки говорят — «да»',
    'Да',
    'Пока не ясно, попробуй снова',
    'Спроси позже',
    'Лучше не рассказывать',
    'Сейчас нельзя предсказать',
    'Сконцентрируйся и спроси опять',
    'Даже не думай',
    'Мой ответ — «нет»',
    'По моим данным — «нет»',
    'Перспективы не очень хорошие',
    'Весьма сомнительно']
    await ctx.send(f'Вопрос: {question}\nAnswer : {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=6):
	await ctx.channel.purge(limit=amount)

@client.command()
async def kick (ctx, member: discord.Member, *, reason = None):
    await member.kick(reason=reason)

@client.command()
async def ban (ctx, member: discord.Member, *, reason = None):
    await member.ban(reason=reason)
client.run(TOKEN)
