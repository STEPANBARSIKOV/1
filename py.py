import discord
import random

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$TEST_BOT,_мы_крутые?'):
        await message.channel.send("да😎")
    else:
        await message.channel.send(message.content)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!смайлик'):
        emojis = ['😃', '😊', '👍', '❤️', '🎉', '🔥']
        random_emoji = random.choice(emojis)
        await message.channel.send(random_emoji)

client.run("MTEwNDQwMDgzODcxMTA2MjY0MA.GJ8foO.hB2TJKVFrDTcmZjL3_ShcFl2KMC5QETXA3vLV0")