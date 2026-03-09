import discord
from discord.ext import commands
from discord import app_commands

class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Ver latencia del bot")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong {latency}ms")

    @app_commands.command(name="hola", description="Saludo simple")
    async def hola(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"Hola {interaction.user.mention}"
        )

    @app_commands.command(name="server", description="Info del servidor")
    async def server(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(
            title=guild.name,
            description=f"Miembros: {guild.member_count}",
            color=discord.Color.blue()
        )

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Basic(bot))