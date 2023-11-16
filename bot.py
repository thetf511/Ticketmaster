import discord

from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event

async def on_ready():

print('Bot ist online!')

@bot.command()

async def support(ctx):

embed = discord.Embed(title="Support", description="Klicke auf die Reaktion, um einen Support-Channel zu erstellen.")

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

await user.send(f'Dein Support-Channel wurde erstellt: {new_channel.mention}')

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

if ctx.channel.name == 'support-channel':

await ctx.channel.delete()

bot.run('') 
