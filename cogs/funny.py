# Recuerda que cargaremos los modulos que usaremos
from discord.ext import commands
import discord
import random


"""
Aca crearemos la clase:
1- La clase normalmente es el nombre del archivo:
Class funny(commands.Cog):

2- Una vez escrita le agregamos un def:
class funny(commands.Cog):
    def __init__(self, bot):
    
3- por ultimo creamos una variable con igualdad a nuestro bot
class funny(commands.Cog): <-- 1
    def __init__(self, bot): <-- 2
        self.bot = bot <-- 3

IMPORTANTE. En este archivo deberas respetar muy bien el formato. o mejor conocido como: identacion
"""
class funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

"""
1- Para poner comandos aca. debes sustituir la palabra bot de @bot.commmand() por @commands.command()
2- tambien debemos agregar self, al lado de las funciones ejemplo: "async def say(ctx, *, text):" cambio a async def say(self, ctx, *, text)
3- Recuerda respetar la identacion de lo contrario podria dar error.
"""


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



"""
con lo que sabes, trate de explicarte como funciona y trata de replicar los codigos pero con otros comandos. te aclaro que aca use el modulo "random" , ¿puedes deducir para que sirve?
"""




def setup(bot):
    bot.add_cog(funny(bot))
    
"""
Por ultimo escribimos estas lineas de codigo, que son para cerrar nuestra classe y poder cargarla en el main.py
1- De esta forma iniciamos la configuracion

def setup(bot):

2- Le añadimos el cog al bot, de esta forma bot.add_cog(classecreada(bot))

def setup(bot):
    bot.add_cog(funny(bot))

"""

# Listo ya puedes cargar tu extencion.
