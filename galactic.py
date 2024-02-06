import discord
import asyncio
import sys
import datetime
from discord import File
from discord import app_commands
from discord.ext import commands, tasks
from discord.ext.tasks import loop
from discord.ext.commands import Bot
from discord.utils import get
from easy_pil import Editor, load_image_async, Font
from datetime import timedelta
from itertools import cycle
from myserver import server_on

#Setup :#
intents = discord.Intents.all()
#intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)

bot_status = cycle(
  ["Type '.help' for  Help", "Official Galaktik Discord Bot", ".help"])


@tasks.loop(seconds=3)
async def change_status():
  #await bot.change_presence(activity=discord.Streaming(name= "Type '.help' for  Help", url= "https://www.twitch.tv/duafan"))
  await bot.change_presence(activity=discord.Game(next(bot_status)))


@bot.event
async def on_ready():
  print("Bot is online")
  change_status.start()
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

  #Get Server ID
  guild = bot.get_guild('INSERT-YOUR-GUILD-ID')

  #Get Channel ID for Total User, Member Use, Bot User
  total_users = bot.get_channel('INSERT-YOUR-CHANNEL-ID')
  member_users = bot.get_channel('INSERT-YOUR-CHANNEL-ID')
  bot_users = bot.get_channel('INSERT-YOUR-CHANNEL-ID')

  #Looping for 10 Seconds
  while True:
    print("Getting stats update...")
    user_count = guild.member_count
    member_count = len([m for m in guild.members if not m.bot])
    bot_count = len([m for m in guild.members if m.bot])

    #Log counts for debugging
    print(f"👫🤖Total Users : {user_count}")
    print(f"👫Member Count : {member_count}")
    print(f"🤖Bot Count : {bot_count}")

    #Set Channels Names with newest count
    await total_users.edit(name=f"👫🤖Total Users : {user_count}")
    await member_users.edit(name=f"👫Member Count : {member_count}")
    await bot_users.edit(name=f"🤖Bot Count : {bot_count}")

    #Loop 10 Sec
    await asyncio.sleep(10)


#Welcome Member :#
@bot.event
async def on_member_join(member):

  #add the channel id in which you want to send the card
  #channel = bot.get_channel('INSERT-YOUR-CHANNEL-ID')

  # Get the welcome channel
  welcome_channel = discord.utils.get(member.guild.channels, name='welcome🎉')
  if not welcome_channel:
    return

  #Embed Welcome
  embed = discord.Embed(
    color=discord.Color.random(),
    title="𝙈𝙀𝙈𝘽𝙀𝙍 𝘽𝘼𝙍𝙐!",
    description="(っ◔◡◔)っ 𝙎𝙚𝙡𝙖𝙢𝙖𝙩 𝙙𝙖𝙩𝙖𝙣𝙜 𝙙𝙞 𝙂𝙖𝙡𝙖𝙠𝙩𝙞𝙠 𝘿𝙞𝙨𝙘𝙤𝙧𝙙 𝙎𝙚𝙧𝙫𝙚𝙧 ♥")
  embed.set_thumbnail(url=member.display_avatar.url)
  embed.add_field(name=f"{member.name}#{member.discriminator}",
                  value=f"Selamat bersenang-senang! :slight_smile:",
                  inline=True)
  embed.add_field(name='ID', value=f"{member.id}", inline=True)
  embed.add_field(name="Anda member ke",
                  value=member.guild.member_count,
                  inline=True)
  embed.timestamp = datetime.datetime.now()
  embed.set_footer(
    text='Galactic Bot',
    icon_url=
    "https://cdn.discordapp.com/attachments/762354702687010816/1070987467114680320/MOSHED-2022-12-26-21-22-57.gif"
  )

  pos = sum(m.joined_at < member.joined_at for m in member.guild.members
            if m.joined_at is not None)

  if pos == 1:
    te = "st"
  elif pos == 2:
    te = "nd"
  elif pos == 3:
    te = "rd"
  else:
    te = "th"

  background = Editor("wallpaper.jpg")
  profile_image = await load_image_async(str(member.display_avatar.url))

  profile = Editor(profile_image).resize((450, 450)).circle_image()
  poppins = Font.poppins(size=64, variant="bold")

  poppins_small = Font.poppins(size=64, variant="bold")
  poppins_caption = Font.poppins(size=40, variant="light")

  background.paste(profile, (1050, 290))
  background.ellipse((1050, 290), 450, 450, outline="aqua", stroke_width=4)

  background.text((1300, 200),
                  f"WELCOME TO {member.guild.name}",
                  color="white",
                  font=poppins,
                  align="center")
  background.text((1250, 800),
                  f"{member.name}#{member.discriminator}",
                  color="white",
                  font=poppins_small,
                  align="center")
  background.text((1250, 900),
                  f"You Are The {pos}{te} Member",
                  color="#0BE7F5",
                  font=poppins_caption,
                  align="center")

  file = File(fp=background.image_bytes, filename="wallpaper.jpg")

  #if you want to message more message then you can add like this
  await welcome_channel.send(embed=embed)
  await welcome_channel.send(
    f"Heya {member.mention}! Welcome To **{member.guild.name} For More Information Go To <#'INSERT-YOUR-CHANNEL-ID'>**"
  )

  #for sending the card
  await welcome_channel.send(file=file)


#Goodbye Member :#
@bot.event
async def on_member_remove(member):

  #add the channel id in which you want to send the card
  #channel = bot.get_channel('INSERT-YOUR-CHANNEL-ID')

  # Format the joined at time to GMT+7
  joined_at_gmt7 = member.joined_at + timedelta(hours=7)

  # Get the goodbye channel
  goodbye_channel = discord.utils.get(member.guild.channels, name='goodbye👋')
  if not goodbye_channel:
    return

  # Create the embed
  embed = discord.Embed(
    title="𝙈𝙀𝙈𝘽𝙀𝙍 𝙆𝙀𝙇𝙐𝘼𝙍!",
    color=discord.Color.random(),
  )
  embed.set_thumbnail(url=member.display_avatar.url)
  embed.add_field(
    name="Sampai jumpa",
    value=f"{member.name}#{member.discriminator}! Terima kasih. :upside_down:",
    inline=True)
  embed.add_field(name="ID", value=member.id, inline=True)
  embed.add_field(name="Tanggal Join",
                  value=joined_at_gmt7.strftime("%c"),
                  inline=True)
  embed.timestamp = datetime.datetime.now()
  embed.set_footer(
    text='Galactic Bot',
    icon_url=
    "https://cdn.discordapp.com/attachments/762354702687010816/1070987467114680320/MOSHED-2022-12-26-21-22-57.gif"
  )
  await goodbye_channel.send(embed=embed)


#Slash Command
@bot.tree.command(name="ping", description="Ping the user")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(f"Pong {interaction.user.mention}!")


@bot.tree.command(name="say", description="Things to say")
@app_commands.describe(thing_to_say="What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
  await interaction.response.send_message(
    f"{interaction.user.name} said: `{thing_to_say}`")


@bot.command(aliases=['uinfo', 'ui'])
async def userinfo(ctx: commands.context, member: discord.Member = None):
  if member == None:
    member = ctx.message.author

  roles = []
  for role in member.roles:
    if role.name != "@everyone":
      roles.append(str(role.mention))

  embed = discord.Embed(
    title="User Info",
    description=f"Here's the user info on the user {member.mention}",
    color=discord.Color.random(),
    timestamp=ctx.message.created_at)
  embed.set_thumbnail(url=member.avatar)
  embed.add_field(name='ID', value=member.id)
  embed.add_field(name='Nickname', value=member.display_name)
  embed.add_field(name="Status", value=member.status)
  embed.add_field(
    name="Created at",
    value=member.created_at.strftime("%a, %B, %#d, %Y, %I:%M %p "))
  embed.add_field(
    name="Joined at",
    value=member.joined_at.strftime("%a, %B, %#d, %Y, %I:%M %p "))
  embed.add_field(name=f"Roles ({len(member.roles)})", value=" | ".join(roles))
  await ctx.send(embed=embed)


class InviteButtons(discord.ui.View):

  def __init__(self, inv: str):
    super().__init__()
    self.inv = inv
    self.add_item(discord.ui.Button(label="Invite Link", url=self.inv))

  @discord.ui.button(label="Invite Button", style=discord.ButtonStyle.blurple)
  async def inviteBtn(self, interaction: discord.Interaction,
                      button: discord.ui.Button):
    await interaction.response.send_message(self.inv, ephemeral=True)


@bot.command()
async def invite(ctx: commands.Context):
  inv = await ctx.channel.create_invite()
  await ctx.send("Click the buttons below to invite someone!",
                 view=InviteButtons(str(inv)))


@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")


server_on()
bot.run('INSERT-YOUR-TOKEN')
