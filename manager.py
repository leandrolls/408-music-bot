from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
from discord.ext import commands

class Manager(commands.Cog):
    """ MANEGING """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou pronto e usando o nome de {self.bot.user}')

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Preencha todos os argumentos. Digite *ajudam para exibir os argumentos dos comandos")
        elif isinstance(error, CommandNotFound):
            await ctx.send("Comando não encontrado. Digite !ajudam para exibir os comandos")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))
