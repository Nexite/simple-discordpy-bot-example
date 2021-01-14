import asyncio
from os import getenv
import discord
from discord.ext import commands

# Make sure you have the environmental variable BOT_TOKEN
BOT_TOKEN = getenv("BOT_TOKEN", None)

# As of discord.py version 1.5 the discord API now requires intents,
# .default() is good if you don't need anything special.
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents
intents = discord.Intents().default()
bot = commands.Bot(command_prefix="!", intents=intents)

# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
initial_cogs = ['cogs.example']

for cog in initial_cogs:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(str(e))


# an example of an event
# https://discordpy.readthedocs.io/en/latest/api.html#discord-api-events
@bot.event
async def on_ready():
    print('We have logged in as {0.user}! Bot primed and ready.'.format(bot))


# https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=send#discord.ext.commands.Context.send
@bot.command()
async def text_example(ctx: discord.ext.commands.Context):
    string = "this is not an example string"
    string = string.replace(" not", "")
    await ctx.send(string)


# an example of a discord embed
# https://discordpy.readthedocs.io/en/latest/api.html?highlight=embed#discord.Embed
@bot.command()
async def embed_example(ctx: discord.ext.commands.Context):
    embed = discord.Embed(title="Wow and embed!",
                          description="This is an example embed!",
                          color=0xf45642)
    embed.set_footer(text="<-- this is you!!", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


# an example of sending a file
# https://discordpy.readthedocs.io/en/latest/api.html?highlight=file#discord.File
@bot.command()
async def file_example(ctx: discord.ext.commands.Context):
    await ctx.send(file=discord.File('./resources/discord.png'))


# an example of editing a message
# https://discordpy.readthedocs.io/en/latest/api.html?highlight=edit#discord.Message.edit
@bot.command()
async def edit_example(ctx: discord.ext.commands.Context):
    message = await ctx.send("this will be edited in 5 seconds")
    await asyncio.sleep(5)
    await message.edit(content="edited!")


bot.run(BOT_TOKEN, bot=True, reconnect=True)
