import discord, os

bot = discord.Client()

@bot.event
async def on_ready():
  print("123 gogo")


my_secret = os.environ['token']
bot.run(my_secret)