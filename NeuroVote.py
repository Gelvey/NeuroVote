import discord
from discord import ui
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Permissions, channel, guild, utils
from discord import Embed
from discord.utils import get
import asyncio
import logging

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())
intents = discord.Intents.default() 
intents.message_content = True
intents.guilds = True
intents.members = True
client = discord.Client(intents = intents)

TOKEN = "MTEwNzg3NTQ2Mzk1NjgxMTg2Nw.GbOYO5.FCXc-POosZ0QuGNCQ8tmGU0PcEU2VafuNwpR3c"

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="GamerDads"))
    print("connected") 
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="poll", description="Creates a poll with up to 5 options. (Requires Manage Messages Permission)")
@app_commands.checks.has_permissions(manage_messages=True)
@app_commands.describe(question="What is the question the poll is gonna be asking?", option1="1st option that can be chosen", option2="2nd option that can be chosen", option3="3rd option that can be chosen", option4="4th option that can be chosen",option5="5th option that can be chosen", option6="6th option that can be chosen", option7="7th option that can be chosen", option8="8th option that can be chosen", option9="9th option that can be chosen", option10="10th option that can be chosen", role="Which role to ping in the pole?")
async def poll(interaction: discord.Interaction, question: str, option1: str, option2: str, option3:str=None, option4:str=None, option5:str=None, option6:str=None, option7:str=None, option8:str=None, option9:str=None, option10:str=None, role:discord.Role=None):
    await interaction.response.send_message("Creating poll...", ephemeral=True)
    try:
        listen = [option1, option2, option3, option4, option5, option6, option7, option8, option9, option10]
        list = []
        for i in listen:
            if i != None:
                list.append(i)
        if role == None:
            if len(list) == 2:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}")
                msg=await interaction.channel.send(embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣")
            elif len(list) == 3:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}")
                msg=await interaction.channel.send(embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
            elif len(list) == 4:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}")
                msg=await interaction.channel.send(embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
            elif len(list) == 5:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}")
                msg=await interaction.channel.send(embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
            elif len(list) == 6:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}")
                msg=await interaction.channel.send(embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
            elif len(list) == 7:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}\nOption 7: {list[5]}")
                msg=await interaction.channel.send(embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
                await msg.add_reaction("7️⃣")
            elif len(list) == 8:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}\nOption 7: {list[5]}\nOption 8: {list[7]}")
                msg=await interaction.channel.send(embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
                await msg.add_reaction("7️⃣")
            elif len(list) == 9:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}\nOption 7: {list[5]}\nOption 8: {list[7]}\nOption 9: {list[8]}")
                msg=await interaction.channel.send(embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
                await msg.add_reaction("7️⃣")
                await msg.add_reaction("8️⃣")
                await msg.add_reaction("9️⃣")
            elif len(list) == 10:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}\nOption 7: {list[5]}\nOption 8: {list[7]}\nOption 9: {list[8]}\nOption 10: {list[9]}")
                msg=await interaction.channel.send(embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
                await msg.add_reaction("7️⃣")
                await msg.add_reaction("8️⃣")
                await msg.add_reaction("9️⃣")
                await msg.add_reaction("🔟")
        else:
            if len(list) == 2:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}")
                msg=await interaction.channel.send(f"{role.mention}", embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣")
            elif len(list) == 3:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}")
                msg=await interaction.channel.send(f"{role.mention}", embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
            elif len(list) == 4:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}")
                msg=await interaction.channel.send(f"{role.mention}", embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
            elif len(list) == 5:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}")
                msg=await interaction.channel.send(f"{role.mention}", embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
            elif len(list) == 6:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}")
                msg=await interaction.channel.send(f"{role.mention}", embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
            elif len(list) == 7:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}\nOption 7: {list[6]}")
                msg=await interaction.channel.send(f"{role.mention}", embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
                await msg.add_reaction("7️⃣")
            elif len(list) == 8:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}\nOption 7: {list[6]}\nOption 8: {list[7]}")
                msg=await interaction.channel.send(f"{role.mention}", embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
                await msg.add_reaction("7️⃣")
                await msg.add_reaction("8️⃣")
            elif len(list) == 9:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}\nOption 7: {list[6]}\nOption 8: {list[7]}\nOption 9: {list[8]}")
                msg=await interaction.channel.send(f"{role.mention}", embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
                await msg.add_reaction("7️⃣")
                await msg.add_reaction("8️⃣")
                await msg.add_reaction("9️⃣")
            elif len(list) == 10:
                emb=discord.Embed(color=discord.Colour.blurple(), title=f"{question}", description=f"Option 1: {list[0]}\nOption 2: {list[1]}\nOption 3: {list[2]}\nOption 4: {list[3]}\nOption 5: {list[4]}\nOption 6: {list[5]}\nOption 7: {list[6]}\nOption 8: {list[7]}\nOption 9: {list[8]}\nOption 10: {list[9]}")
                msg=await interaction.channel.send(f"{role.mention}", embed=emb)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣") 
                await msg.add_reaction("3️⃣")
                await msg.add_reaction("4️⃣")
                await msg.add_reaction("5️⃣")
                await msg.add_reaction("6️⃣")
                await msg.add_reaction("7️⃣")
                await msg.add_reaction("8️⃣")
                await msg.add_reaction("9️⃣")
                await msg.add_reaction("🔟")
        await interaction.delete_original_response()
    except Exception as e:
        print(e)
        await interaction.delete_original_response()
        await interaction.followup.send("An error occured, try again later.", ephemeral=True)

bot.run(TOKEN)