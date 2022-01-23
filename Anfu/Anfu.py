import discord
from discord.ext import commands

client = discord.Client()
client.run("OTM0NzU2Mzg5ODgzMDg0ODcw.Ye0tug.RNR2RdTbvQzvklxkG8eLvw6kSM8")

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    pass
    
@client.event
async def on_message(message):
    print(message.content)

@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_member_join(member):
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(934758644451536919)
    general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")

@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for each_message in messages:
        await each_message.delete()

class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

  async def on_ready(self):
        print("Le bot est prêt.")

bot = DocBot()
bot.run("OTM0NzU2Mzg5ODgzMDg0ODcw.Ye0tug.RNR2RdTbvQzvklxkG8eLvw6kSM8")

