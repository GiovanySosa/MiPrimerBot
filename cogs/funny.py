from discord.ext import commands
import discord
import random
import asyncio



class funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.command()
    async def say(self, ctx, *, text):
        message = ctx.message
        await message.delete()
        await ctx.send(f"{text}")



    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")




    @commands.command(name= "8ball")
    async def _8ball(self, ctx, *, question):
        respuesta = [
            'no se', 'pregunta otro dia', 'era bait'
        ]
        ball = discord.Embed(title=" ", description=" ", color= discord.Color.blue())
        ball.add_field(name="comando 8ball | :8ball:", value=f"**pregunta:** {question} \n **respuesta:** {random.choice(respuesta)}")
        await ctx.send(embed=ball)







def setup(bot):
    bot.add_cog(funny(bot))
