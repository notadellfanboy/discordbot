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


@client.event
async def on_voice_state_update(before, after):
    print("voice state changed")
    muted_user = after
    str_mention = muted_user.mention
    if muted_user.voice.self_mute:
        await client .send_message(client.get_channel("157183056413851650"), "{}, you're muted".format(str_mention))


client.run("NTEwNTY5ODMwNzQzODAxODk1.DseRCA.qMJpNtao5jFXGXrG0RusByeqFGY")
