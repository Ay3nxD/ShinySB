import os
def install(package):
  os.system(f"{sys.executable} -m pip install {package}")
try:
    import discord
except ModuleNotFoundError:
    install('discord')
try:
    import aiohttp
except ModuleNotFoundError:
    install('aiohttp')
try:
    import bs4
except ModuleNotFoundError:
    install('bs4')
try:
    import dpy
except ModuleNotFoundError:
    install('dpy')
try:
    import time
except ModuleNotFoundError:
    install('time')
try:
    import json
except ModuleNotFoundError:
    install('json')
try:
    import colorama
except ModuleNotFoundError:
    install('colorama')
try:
    import random
except ModuleNotFoundError:
    install('random')
try:
    import requests
except ModuleNotFoundError:
    install('requests') 
try:
    import ctypes
except ModuleNotFoundError:
    install('ctypes')
try:
    import sys
except ModuleNotFoundError:
    install('sys')
try:
    import urllib
except ModuleNotFoundError:
    install('urllib')
try:
    import asyncio
except ModuleNotFoundError:
    install('asyncio')
try:
    import shutup
except ModuleNotFoundError:
    install ('shutup')




from discord import permissions
from discord import channel
from time import sleep
from discord import integrations, message, Message , colour , user , Permissions
from discord.ext import commands
from colorama import Fore,Back,Style
from rich.console import Console
import shutup;shutup.please()
from random import randint



#config thingy
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

Shinysb = commands.Bot(command_prefix=f'{prefix}', self_bot=True,help_command=None)
Shinysb.remove_command('help')
Shinysb_version = "BETA 1.0"


Shinysb.copycat = None
Shinysb.msgsniper = True
console = Console(
        color_system="auto", 
        legacy_windows=True,
    )


#DEFINE
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def avatarUrl(id, avatar):
    url = ""
    if not str(avatar).startswith("http"):
            if str(avatar).startswith("a_"):
                url =  f"https://cdn.discordapp.com/avatars/{id}/{avatar}.gif?size=1024"
            else:
                url =  f"https://cdn.discordapp.com/avatars/{id}/{avatar}.png?size=1024"

            return url
    else:
            return avatar


#EVENTS

@Shinysb.event
async def on_ready():
        print(f"""
    {Fore.CYAN}███████╗██╗  ██╗██╗███╗   ██╗██╗   ██╗
    ██╔════╝██║  ██║██║████╗  ██║╚██╗ ██╔╝
    ███████╗███████║██║██╔██╗ ██║ ╚████╔╝ 
    ╚════██║██╔══██║██║██║╚██╗██║  ╚██╔╝  
    ███████║██║  ██║██║██║ ╚████║   ██║   
    ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝                                                                         
        {Fore.RESET}""")
ctypes.windll.kernel32.SetConsoleTitleW(f'SHINY SELFBOT {Shinysb_version}')

#
#COMMANDS
#

@Shinysb.command(aliases=['spamchangegc'])
async def loopchangegc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "SHINY SB"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)

@Shinysb.command()
async def reverseav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}",color = discord.Colour.blue())
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

@Shinysb.command(name="avatar", description="Get the mentioned user's avatar.", usage="avatar [@user]", aliases=["pfp", "profilepicture"])
async def avatar(ctx, *, user: discord.User):
    await ctx.message.delete()
    await ctx.send(avatarUrl(user.id, user.avatar))

@Shinysb.command(name='leet', aliases=['leetspeak','1337','hackerspeak'])
async def leet(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '@').replace('A', '@').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')

@Shinysb.command()
async def shlong(ctx,user: discord.Member = None):
    await ctx.message.delete()
    if user == None:
        user = ctx.author
    size = random.randint(1,15)
    penis = ""
    for _i in range(0,size):
        penis += "="
    await ctx.send(f'{user}\' Dick size \n8{penis}D')

@Shinysb.command()
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.WHITE}{e}" + Fore.RESET)

@Shinysb.command(aliases=["copyguild", "copyserver"])
async def servercopy(ctx):  
    await ctx.message.delete()
    await Shinysb.create_guild(f'{ctx.guild.name}')
    sleep(5)
    for g in Shinysb.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Shinysb.command()
async def poll(ctx,arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(arguments[str.find(arguments, "msg:"):str.find(arguments, "1:")]).replace(
        "msg:", "")
    option1 = discord.utils.escape_markdown(arguments[str.find(arguments, "1:"):str.find(arguments, "2:")]).replace(
        "1:", "")    
    option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
    message = await ctx.send(f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
    await message.add_reaction('🅰️')
    await message.add_reaction('🅱️')

@Shinysb.command(aliases=['logout'])
async def fuckoff(ctx):
    await ctx.message.delete()
    await Shinysb.logout()

@Shinysb.command()
async def rolecolor(ctx,role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f'{role.name} : {role.color} ')

@Shinysb.command()
async def italicize(ctx,message):
    await ctx.message.delete()
    await ctx.send('*'+message+'*')

@Shinysb.command()
async def strike(message,ctx):
    await ctx.message.delete()
    await ctx.send("~~"+message+'~~')

@Shinysb.command()
async def underline(ctx,message):
    await ctx.message.delete()
    await ctx.send('__'+message+'__')

@Shinysb.command()
async def hide(ctx,message):
    await ctx.message.delete()
    await ctx.send('||'+ message +'||')

@Shinysb.command()
async def bold(ctx,message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')

@Shinysb.command()
async def unflip(ctx):
    await ctx.message.delete()
    await ctx.send('┬─┬ ノ( ゜-゜ノ)')

@Shinysb.command()
async def tableflip(ctx):
    await ctx.message.delete()
    await ctx.send('(╯°□°）╯︵ ┻━┻')

@Shinysb.command()
async def lenny(ctx):
    await ctx.message.delete()
    await ctx.send('( ͡° ͜ʖ ͡°)')

@Shinysb.command()
async def shrug(ctx):
    await ctx.message.delete()
    await ctx.send('¯\_(ツ)_/¯')

@Shinysb.command()
async def reversetext(ctx,message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Shinysb.command()
async def stopactivity(ctx,message):
    await ctx.message.delete()
    await Shinysb.change_presence(activity=None,status=discord.Status.online)

@Shinysb.command()
async def watching(ctx,message):
    await ctx.message.delete()
    await Shinysb.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        )
    )

@Shinysb.command()
async def listening(ctx,message):
    await ctx.message.delete()
    await Shinysb.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@Shinysb.command()
async def playing(ctx,message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Shinysb.user.change_presence(activity=game)

@Shinysb.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/shinysb",
    )
    await Shinysb.change_presence(activity=stream)

@Shinysb.command()
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == Shinysb.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Shinysb.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass

@Shinysb.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

@Shinysb.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')

@Shinysb.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Shinysb.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)

@Shinysb.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)

@Shinysb.command()
async def ping(ctx):
    await ctx.send('Pong!')

@Shinysb.command(name="lamar",description="Lamar being Lamar", usage="lamar")
async def lamar(ctx):
    await ctx.message.delete()
    await ctx.send("Ah, nigga, don't hate me 'cause I'm beautiful, nigga")
    sleep(1)
    await ctx.send("Maybe if you got rid of that old yee-yee ass haircut you got you'd get some bitches on your dick")
    sleep(3)
    await ctx.send("Oh, better yet, maybe Tanisha'll call your dog-ass if she ever stop fuckin' with that brain surgeon or lawyer she fucking with")
    sleep(3)
    await ctx.send("N")
    sleep(0.5)
    await ctx.send("NI")
    sleep(0.5)
    await ctx.send("NIG")
    sleep(0.5)
    await ctx.send("NIGG")
    sleep(0.5)
    await ctx.send("NIGGE")
    sleep(0.5)
    await ctx.send("NIGGER")
    sleep(0.5)
    await ctx.send("NIGGER.")
    sleep(0.5)
    await ctx.send("NIGGER..")
    sleep(0.5)
    await ctx.send("NIGGER...")

@Shinysb.command()
async def clap(ctx, sentence: str):
        await ctx.message.delete() 
        await ctx.send(sentence.replace(' ', ' :clap: '))

@Shinysb.command()
async def insult(ctx, user: discord.User=None):
        await ctx.message.delete()
        if user is None:
            member = ctx.author
        else:
            member = user
        insult = requests.get(f'https://insult.mattbas.org/api/insult')
        embed = discord.Embed(description = f'{insult.text}',color=discord.Colour.blue()) 
        await ctx.send(embed=embed,delete_after=15)

@Shinysb.command()
async def ascii(ctx, text): 
    sleep(0.5)    
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```",delete_after=15)

@Shinysb.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): 
    await ctx.message.delete()
    os.system('cls')
    print(f"""
    {Fore.CYAN}███████╗██╗  ██╗██╗███╗   ██╗██╗   ██╗
    ██╔════╝██║  ██║██║████╗  ██║╚██╗ ██╔╝
    ███████╗███████║██║██╔██╗ ██║ ╚████╔╝ 
    ╚════██║██╔══██║██║██║╚██╗██║  ╚██╔╝  
    ███████║██║  ██║██║██║ ╚████║   ██║   
    ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝                                                                         
        {Fore.RESET}
    """)   

@Shinysb.command()
async def meme(ctx):
    sleep(0.5)
    await ctx.message.delete()    

    memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
    memeData = json.load(memeApi)

    memeUrl = memeData['url']
    memeName = memeData['title']
    memePoster = memeData['author']
    memeSub = memeData['subreddit']
    memeLink = memeData['postLink']

    embed = discord.Embed(title=memeName,colour = discord.Colour.blue())
    embed.set_image(url=memeUrl)
    embed.set_footer(text=f"Meme by: {memePoster} | Subreddit {memeSub} | Post: {memeLink}")
    await ctx.send(embed = embed, delete_after=15)

Shinysb.run(token, bot=False)    