from discord.ext import commands
import DiscordUtils
import discord

music = DiscordUtils.Music()

class MusicBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='entrar')
    async def join(self, ctx):
        voicetrue = ctx.author.voice
        if voicetrue is None:
            embed_image = discord.Embed(title="AVISO", color=0xFFFFFF)
            embed_image.add_field(name="Alerta:", value="Você tem que entrar em um canal de voz!", inline=False)
            return await ctx.send(embed=embed_image)
        await ctx.author.voice.channel.connect()

    @commands.command(name='sair')
    async def leave(self, ctx):
        voicetrue = ctx.author.voice
        myvoicetrue = ctx.guild.me.voice
        if voicetrue is None:
            embed_image = discord.Embed(title="AVISO", color=0xFFFFFF)
            embed_image.add_field(name="Alerta:", value="Você tem que entrar em um canal de voz!", inline=False)
            return await ctx.send(embed=embed_image)
        if myvoicetrue is None:
            embed_image = discord.Embed(title="AVISO", color=0xFFFFFF)
            embed_image.add_field(name="Alerta:", value="Ainda não entrei em um canal de voz!", inline=False)
            return await ctx.send(embed=embed_image)
        await ctx.voice_client.disconnect()

    @commands.command(name='p')
    async def play(self, ctx, *, url):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()

            embed_image = discord.Embed(title="COMEÇANDO A TOCAR:", color=0xFFFFFF)
            embed_image.add_field(name="MÚSICA:", value=f"{song.name}", inline=False)
            await ctx.send(embed=embed_image)
        else:
            song = await player.queue(url, search=True)
            await ctx.send(f"{song.name} foi adicionado na fila")

    @commands.command(name='fila')
    async def queue(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        if [song.name for song in player.current_queue()] == []:
            await ctx.send("Não há mais músicas na fila!\nPara tocar uma música basta colocar *play, seguido do link do youtube ou nome da música que você deseja reproduzir.")
        else:
            i = 0
            embed_image = discord.Embed(title="FILA DE MÚSICAS", color=0xFFFFFF)

            for song in player.current_queue():
                print(song.name)
                i =+ 1
                embed_image.add_field(name=f"{i}.", value=f"{song.name}", inline=False)

            await ctx.send(embed=embed_image)

    @commands.command(name='pause')
    async def pause(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send("Pausado")

    @commands.command(name='resume')
    async def resume(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()

    @commands.command(name='agora')
    async def nowplauing(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = player.now_playing()
        embed_image = discord.Embed(title="TOCANDO AGORA", color=0xFFFFFF)
        embed_image.add_field(name="MÚSICA:", value=f"{song.name}", inline=False)
        await ctx.send(embed=embed_image)

    @commands.command(name='next')
    async def next_song(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        await player.remove_from_queue(int(0))

def setup(bot):
    bot.add_cog(MusicBot(bot))
