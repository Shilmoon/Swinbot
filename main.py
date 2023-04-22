import discord
from discord.ext import commands

config = dict(token='MTAyMTM2NjYyMDA0MTUxNTA2OA.G33w59.lOGpTngXfKXp22Tw4c9_OQ-THfI06uwhrRU4EA', prefix='prefix')

bot = discord.Bot(intents=discord.Intents.all())

roles = {'☠️': 942117291900944394,
         '👻': 976409119017824286,
         '👾': 953719227217485834,
         '🚘': 942117126498557953,
         '🚀': 950070092522209360,
         '😈': 998660226607759543,
         '🥳': 980959958852046849,
         '🔫': 977543627402276944,
         '💠': 980495984704495647,
         '💫': 1003039412961165442,
         '🌎': 1014901390063194132,
         '💀': 998658455483187311,
         '👹': 1004073297220214825,
         '🧸': 1084977520769769563,
         '🐱': 1084976428229066752,
         '🗡': 1084994366684274818,
         '🐴': 1084972128538988626,
         '🌿': 1062486181239074867,
         '🧔‍♂️': 1084975724198367305}



@bot.event
async def on_raw_reaction_add(reaction):
    if reaction.message_id == 1021406791621414942:
        print(reaction.emoji.name)
        if reaction.emoji.name in roles.keys():
            print('да')
            role = discord.utils.get(reaction.member.guild.roles, id=roles[reaction.emoji.name])
            await reaction.member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(reaction):
    if reaction.message_id == 1021406791621414942:
        if reaction.emoji.name in roles.keys():
            guild = await bot.fetch_guild(reaction.guild_id)
            member = await guild.fetch_member(reaction.user_id)
            role = discord.utils.get(member.guild.roles, id=roles[reaction.emoji.name])
            await member.remove_roles(role)


@bot.slash_command(name='borov', description='1')
async def borov(ctx):
    await ctx.respond('Ya ne borov')


bot.run(config['token'])