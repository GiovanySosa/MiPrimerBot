import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", help_command=None)






@bot.event
async def on_ready():
    status = discord.Game("Soy el primer bot creado")
    await bot.change_presence(status=discord.Status.idle, activity=status)
print("en servicio")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "Lista de comandos", description = "Estos son todos los comandos disponibles", color = discord.Color.blue())
    embed.add_field(name = "Funny", value='`say`,`help`')
    await ctx.send(embed=embed)






bot.load_extension("cogs.raid")
bot.load_extension("cogs.funny")
bot.run(TOKEN)
