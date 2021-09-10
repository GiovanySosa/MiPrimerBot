""" 
1- Para iniciar nuestro bot debemos tener instalado los modulos. te los deje en el archivo InstalaModulos. como este es un bot para que aprendas a hacer uno tu,
inclui modulos sencillos y principales para cada funcion.
"""

import discord
from discord.ext import commands
from dotenv import load_dotenv

"""
2- Luego empezaremos cargando el archivo .env, lo que hace dicho archivo es proteger el TOKEN de nuestro Bot, el siguiente codigo es para establecer dicha funcion 
"""

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


"""
3- Ahora empezaremos creando en si nuestro bot, crearemos una variable con cualquiere nombre, en mi caso se llama: "bot" y lo igualamos como el siguiente codigo

"""

bot = commands.Bot(command_prefix="!", help_command=None) # <-- aca removi el comando help para crear uno nuevo. en el segundo ejemplo lo veras, te sugiero hacer esto en tus futuros proyectos 
                                                          # <-- tambien creamos nuestro prefix

"""
3- Listo despues de haber echo lo anterior, estamos listos para nuestro primer codigo. siempre para crear un comando vas iniciar con, "@variable.command()", recuerda que la variable
nosotros la nombramos. en caso de que sea evento se establece asi: "@variable.event" aca te dejo dos ejemplos; uno de evento y uno de comando

"""


@bot.event  # <---- como es evento lo iniciamos de esta forma
async def on_ready():  # <--- todos los comandos o eventos inician de la misma forma: "async def nombredelevento:/nombredelcomando():", los comandos llevan (): al final.
    status = discord.Game("Soy el primer bot creado") # <-- en esta parte creamos una variable llamada "status"  o el nombre que tu prefieras
                                                      # Le damos una igualdad o lo que incluira, nuestra variable en este caso: discord.Game("aca el status que quieras que salga")
                                                      # importante. siempre que uses "discord.", la palabra despues del punto iniciara con mayuscula
    await bot.change_presence(status=discord.Status.idle, activity=status) # <-- el await ya es en si la funcion. en este caso le damos una presencia al bot
                                                      #tambien hacemos el uso de la variante "status" 
print("en servicio") #<-- Esto es para comprobar que tu bot sirvicio en la consola de python

#FELICIDADES TIENES TU PRIMER EVENTO. Ahora hagamos un comando simple


@bot.command() # <-- los comandos suelen iniciar de esta forma. solo el nombre de la variable puede cambiar segun el usuario. el nuestro es "bot"
async def help(ctx): # <-- usamos el mismo procedimiento, solo que esta vez incluimos el nombre de el comando, en nuestro caso es el "help" y establecemos el (ctx)  
"""
Aca crearemos nuestro primer embed. todos se crean asi:
1- creamos una variable en nuestro caso se llama "embed"
2- le damos una funcion en este caso es: discord.Embed(title = "", description = "", color = discord.Color.blue())
3- todos los embeds siguen el mismo formato, solo la variable cambia.
"""
    embed = discord.Embed(title = "Lista de comandos", description = "Estos son todos los comandos disponibles", color = discord.Color.blue())
"""
4- Le añadiremos un field a nuestro embed. para hacerlo es asi: variable.add_field(name="", value=""), recuerda que la variable es la que creamos anteriormente. la cual es "embed"
5- En el apartado incluiremos el nombre de nuestra categoria seguido de una coma: (name ="Funny",
6- Despues de a ver hecho lo anterior, añadiremos un value y en este seguiremos el formato '`nombre del comando`', nos quedaria asi: (name = "Funny", value='`say`,`help`')

"""   
    embed.add_field(name = "Funny", value='`say`,`help`')
    await ctx.send(embed=embed) # <-- por ultimo pondremos el await para que nuestro bot envie el embed al usar el comando !help: ctx.send(embed=nombredelavariable)


# FELICIDADES ESTE ES TU PRIMER COMANDO




bot.load_extension("cogs.raid") # todas las extenciones que creemos dentro la carpeta cogs se cargan asi, bot.load_extension("cogs.nombredelarchivo") se ignora el .py
bot.load_extension("cogs.funny")




bot.run(TOKEN) # <-- Esto ponlo asi, la palabra TOKEN cambia si al principio cambiaste el nombre de la funcion: variable = os.getenv('DISCORD_TOKEN')

