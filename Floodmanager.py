import discord
import asyncio

TOKEN = 'MTI0MDg3OTk0MzkyMDEyODA3MQ.GIRkDj.EU_rgrHmZYpOtQFTHk_gq6rsKr_7QLhHI4M3_Y'
client = discord.Client()

@client.event
async def on_ready():
    print('Estou pronto para espalhar o caos!')

@client.event
async def on_message(message):
    if message.author == client.user:  # Verifica se a mensagem é do próprio selfbot
        for channel in message.guild.text_channels:  # Percorre todos os canais de texto do servidor
            await channel.send('KAKAKAKAKA')  # Envie sua mensagem de flood
        await asyncio.sleep(1)  # Aguarde um segundo entre os envios para evitar sobrecarga

client.run(TOKEN, bot=False)
  
