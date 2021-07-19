from discord.ext import commands
import discord
import asyncio

# DEDUCE EL CODIGO, TODO LO HE MOSTRADO ANTES


class raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)
        await asyncio.sleep(0)
        await ctx.send(f"Se han borrado {amount} mensajes!")
        await ctx.channel.purge(limit=1)





def setup(bot):
    bot.add_cog(raid(bot))
