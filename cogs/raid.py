from discord.ext import commands
import discord
import asyncio



class raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.has_permissions(administrator=True)
    @commands.command()
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            await ctx.send("No has mencionado un canal")
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Nuked Activado!")
            await nuke_channel.delete()
            await new_channel.send("este canal ha sido Nukeado!")
            await ctx.send("Nuke completado!")

        else:
            await ctx.send(f"nombre de canal {channel.name} no existe!")




    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)
        await asyncio.sleep(0)
        await ctx.send(f"Se han borrado {amount} mensajes!")
        await ctx.channel.purge(limit=1)





def setup(bot):
    bot.add_cog(raid(bot))