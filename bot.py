import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot ist online!')
    await bot.change_presence(activity=discord.Game(name="Example Made by TheTF"))

@bot.command()
async def support(ctx):
    embed = discord.Embed(
        title="Support",
        description="Klicke auf die Reaktion, um einen Support-Channel zu erstellen.",
        color=0x3498db  
    )
    sent_embed = await ctx.send(embed=embed)
    await sent_embed.add_reaction('🆘')

    def check(reaction, user):
        return str(reaction.emoji) == '🆘' and user != bot.user

    reaction, user = await bot.wait_for('reaction_add', check=check)
    await sent_embed.remove_reaction('🆘', bot.user)

    category = ctx.channel.category
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        user: discord.PermissionOverwrite(read_messages=True)
    }
    new_channel = await category.create_text_channel('support-channel', overwrites=overwrites)

    support_embed = discord.Embed(
        title="Willkommen im Support-Channel!",
        description=f"Bitte erkläre dein Anliegen. Der Support wird sich bald bei dir melden.",
        color=0x2ecc71 
    )
    support_embed.set_footer(text=f"Support-Anfrage von {user.display_name}", icon_url=user.avatar.url)
    await new_channel.send(embed=support_embed)

@bot.command()
async def rollen(ctx, channel_id: int, *roles: discord.Role):
    channel = bot.get_channel(channel_id)
    if ctx.channel.id == channel_id:
        overwrites = channel.overwrites
        for role in roles:
            overwrites[role] = discord.PermissionOverwrite(read_messages=True)
        await channel.edit(overwrites=overwrites)

@bot.command()
async def close(ctx):
    if ctx.channel.name.startswith('support-channel'):
        await ctx.channel.delete()
    else:
        await ctx.send("Dieser Befehl kann nur in Support-Kanälen verwendet werden.")

@bot.event
async def on_command_error(ctx, error):
    print(f"Fehler beim Ausführen des Befehls '{ctx.command}': {error}")
    
bot.run('')
