import discord
import asyncio
client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith("!test"):
        await client.send_message(message.channel, "test")

# notify users when they mute themselves
@client.event
async def on_voice_state_update(before, after):
    print("voice state changed")
    muted_user = after
    str_mention = muted_user.mention
    if muted_user.voice.self_mute:
        await client.send_message(client.get_channel("157183056413851650"), "{}, you're muted".format(str_mention))

# ping when a user comes online
@client.event
async def on_member_update(before,after):
    if str(before.status) == "offline":
        if str(after.status) == "online" or str(after.status) == "idle":
            await client.send_message(client.get_channel("157183056413851650"), "{} just came online.".format(after.mention))


@client.event
async def on_message(message):
    if message.content.startswith("forsenE"):
        await client.send_message(message.channel, "<:forsen1:442133101896925194><:forsen2:442133102131806208>\n<:forsen3:442133101905444864><:forsen4:442133101959970816>")
client.run("NTEwNTY5ODMwNzQzODAxODk1.DseRCA.qMJpNtao5jFXGXrG0RusByeqFGY")
