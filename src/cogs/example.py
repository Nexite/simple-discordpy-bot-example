import discord
from discord.ext import commands


class ExampleCog(commands.Cog, name="Example Cog"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def example_cog_command(self, ctx):
        await ctx.send("this message was send from ExampleCog")

    # an example of a group
    # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=group#discord.ext.commands.Group
    @commands.group(name="example")
    async def example(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid badge command passed...')

    @example.command()
    async def group_command(self, ctx: discord.ext.commands.Context):
        await ctx.send("this message was send under the example group from ExampleCog")


def setup(bot):
    bot.add_cog(ExampleCog(bot))
