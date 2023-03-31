import nextcord #модуль nextcord.py
from nextcord.ext import commands
import asyncio

#.help
bot = commands.Bot( command_prefix = "." ) #Знак с помощью которого будут работать команды бота
#переменные

#---------------------Events----------------------#
@bot.event
#подключение
async def on_ready():
	print( 'Бот подключен by Rall' )

	await bot.change_presence( status = nextcord.Status.online )
#----------------Команды----------------------------------#
#userinfo
@bot.command()
async def userinfo(ctx, Member: nextcord.Member = None ):
    if not Member:
        Member = ctx.author
    roles = (role for role in Member.roles )
    emb = nextcord.Embed(title='Информация о пользователе.'.format(Member.name), description=f"Имя дискорда: {Member.name}\n\n"
		f"Никнейм на сервере: {Member.nick}\n\n"
		f"Статус: {Member.desktop_status}\n\n"
		f"ID: {Member.id}\n\n"
		f"Игрок присоединился к серверу: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
		f"Аккаунт создан: {Member.created_at.strftime('%b %#d, %Y')}", 
		color=0xff0000, timestamp=ctx.message.created_at)
    emb.set_thumbnail(url= Member.display_avatar)
    emb.set_footer(icon_url= Member.display_avatar)
    emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.display_avatar)
    await ctx.send(embed=emb)
#avatar
@bot.command()
async def avatar(ctx, member : nextcord.Member = None):
	if not Member:
		Member = ctx.author
	roles = (role for role in Member.roles)
	user = ctx.message.author if (member == None) else member
	embed = nextcord.Embed(title=f'Аватар пользователя {user}', color= 0x0c0c0c)
	embed.set_image(url=user.display_avatar)
	await ctx.send(embed=embed)
#serverinfo
@bot.command()
async def serverinfo(ctx, member: nextcord.Member = None):
    if not member:
        member = ctx.author

    guild = ctx.guild
    embed = nextcord.Embed(title=f"{guild.name}", description=f"Сервер создали {guild.created_at.strftime('%b %#d, %Y')}\n\n"
	f"Всего пользователей: {guild.member_count}\n\n",  color=0xff0000,timestamp=ctx.message.created_at)

    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=f"ID: {guild.id}")
    embed.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.display_avatar)
    await ctx.send(embed=embed)
#ping 
@bot.command()
async def ping(ctx, member: nextcord.Member = None ):
    await ctx.channel.purge(limit = 1)

    await ctx.send(embed = nextcord.Embed(
        title = '**🔴 Пинг бота**',
        description = f'**{bot.ws.latency * 1000:.0f} мс**'
    ))

#connect (всегда в конце)
token = open ( 'token.txt', 'r' ).readline()

bot.run ( token )