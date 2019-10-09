import discord
from discord.ext import commands
import asyncio

#update the variables below with your information
token = "TOKEN"
prefix = "PREFIX"

bot = commands.Bot(command_prefix=prefix, case_insensitive=True)

@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# notify users when they mute themselves
@bot.event
async def on_voice_state_update(before, after):
    print("Voice Status Update!")
    muted_user = after
    str_mention = muted_user.mention
    if muted_user.voice.self_mute:
        await bot.get_channel("157183056413851650").send(f"{str_mention}, you're muted")

# ping when a user comes online
@bot.event
async def on_member_update(before, after):
    if str(before.status) == "offline":
        if str(after.status) == "online" or str(after.status) == "idle":
            await bot.get_channel("157183056413851650").send(f"{after.mention} just came online.")

#made this a command because on_message listeners are resource heavy
@bot.command
async def forsene(ctx):
    #added a description visible in the help command
    """Command to display the forsenE Emoji Quadruplet."""
    await ctx.send("<:forsen1:442133101896925194><:forsen2:442133102131806208>\n<:forsen3:442133101905444864><:forsen4:442133101959970816>")

#made this a command because on_message listeners are resource heavy
@bot.command
async def test(ctx):
    #added a description visible in the help command
    """A command that returns Testing! Can be used to check if the bot is online."""
    await ctx.send("Testing!")

bot.run(token, bot=True, reconnect=True)
