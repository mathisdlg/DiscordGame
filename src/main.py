import discord
from discord.ext import commands
import time
from Game import *



if __name__ == "__main__":
    
    config = {
        'token': open("token.key", 'r').read(),
        'prefix': '$',
        'intents': discord.Intents.all(),
        'name': 'Sparky gamers',
        'discriminator': '1852',
    }
    
    bot = commands.Bot(command_prefix=config['prefix'], intents=config['intents'])

    @bot.event
    async def on_ready():
        print("Prêt!")
        config["members"] = bot.get_all_members()
        user = discord.utils.get(bot.users, name = config['name'], discriminator = config['discriminator'])
        config['bot_id'] = user
        channel = bot.get_channel(config['ch_acc'])
        await channel.send(f"{config['bot_id'].mention} est en ligne!")

    @bot.event
    async def on_member_join(member):   
        channel = bot.get_channel()
        embed=discord.Embed(title="Welcome!",description=f"Bienvenue {member.mention}, fais toi plaise on est juste entre gens du G4!\nVa quand même check les {bot.get_channel(config['regles']).mention}")
        await channel.send(embed=embed)


    @bot.command()
    async def ping(message):
        if message.channel.id == config['ch_bot']:
            await message.channel.send("pong")
            time.sleep(1)
            await message.message.delete()

    @bot.command(pass_context=True, name='del')
    async def delete(ctx, ammount):
        if ctx.author.roles[-1].id == config['admin']:
            tmp = await ctx.channel.send("Clearing messages...")
            time.sleep(1)
            await tmp.delete()
            print(f"Clearing {ctx.channel}")
            async for message in ctx.history(limit=int(ammount)+1):
                await message.delete()
        else:
            await ctx.message.delete()
            tmp = await ctx.channel.send(f"{ctx.author.mention} you don't have the permissions")

    """
    @bot.command()
    async def test(ctx):
        
        print(f"{ctx.author.roles[-1].id}")
        
        #msg = await discord.utils.get(ctx.channel.history(), author__name='Sparky')
        #messages = [message async for message in ctx.history(limit=123)]
        #async for m in bot.logs_from(channel):
        #    print(m.clean_content)

    """
    bot.run(config['token'])
