from discord.ext import commands
import discord

class Talks(commands.Cog):
    """ TALKS WITH USER """

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='ajudam', help="O Bot mostra todos os comandos")
    async def ajudam(self, ctx):
        embed_image = discord.Embed(title="PRECISANDO DE AJUDA? ", color=0xFFFFFF)
        embed_image.add_field(name="COMANDOS:", value="""
        *ajudam = Para exibir essa mensagem com os comandos e sua funções.
        *entrar = O Bot entra no canal de voz que você estiver.
        *sair = O Bot sai no canal de voz que você estiver.
        *p = O Bot toca a música (É necessario o nome ou url da musica).
        *fila = O Bot exibe a fila de músicas.
        *pause = O Bot pausa a música.
        *resume = O Bot retoma a música.
        *agora = O Bot diz qual música está sendo tocada agora.
        *next = O Bot passa a música.
        """, inline=False)
        await ctx.send(embed=embed_image)

def setup(bot):
    bot.add_cog(Talks(bot))