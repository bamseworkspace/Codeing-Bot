import discord
from discord.ext import commands
import json

from discord.ext.commands import has_permissions
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix="!v ")
slash = SlashCommand(bot, sync_commands=True)
testmode = True


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


bot.remove_command("help")


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help", description="Use !v ")
    em.add_field(name="VerifiCation", value="!v [Link], !v check, !v givop")

    await ctx.send(embed=em)


@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def adminhelp(ctx):
    em = discord.Embed(title="**ADMIN HELP!**", description="Use !v sudo[cmd] for sudos")
    em.add_field(name="**ADMIN** Channels (Your Own)", value="!v sam (See Private Admin Channel) \r !v stam (Set Private Admin Channel)")


#@slash.slash(description="Setup The Admin Channel")
@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def sam(ctx):
    print(f"{ctx.author.id}")
    with open(f"jsons/{ctx.author.id}.json", "r") as f:
        data = json.load(f)
    await ctx.send(data["channel"])


#@slash.slash(description="Setup The Admin Channel")
@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def stam(ctx, channel):
    with open("jsons/ex.json", "r") as f:
        data = json.load(f)

    data["channel"] = channel
    with open(f"jsons/{ctx.author.id}.json", "w") as f:
        json.dump(data, f)
    await ctx.send("OK")


bot.run([TOKEN])
