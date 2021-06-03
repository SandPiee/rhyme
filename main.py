import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='>')
TOKEN = 'NTg0ODAzMTczMTE0NTc2OTA1.XPQOZQ.BvcIzsjG7sir7plH3Pa-bNoeA2I'

yes = ['да', 'да!', 'да?', 'да.']
a = ['а', 'а!', 'а?', 'а.']

@bot.event
async def on_message(message):
	# FBI only for admin
	# print('Message from {0.author}: {0.content}'.format(message))

	msg = message.content.lower()

	if msg in yes:
		await message.channel.send('Пизда!')
	elif msg in a:
		await message.channel.send('Хуй на!')

bot.run(TOKEN)