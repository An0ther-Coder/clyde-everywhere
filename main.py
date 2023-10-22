import discord
from discord.ext import commands
from math import ceil

reclyde = commands.Bot(command_prefix="<<")
# Consts
CLYDE_ID = 
CLYDE_GUILD_ID = 
CLYDE_CHANNEL_ID = 

queue = []


@reclyde.event
async def on_ready():
	global CLYDE_CHANNEL
	print(f"Logged in as {reclyde.user} (ID: {reclyde.user.id})")
	print("-"*120)
	# Setting online status
	await reclyde.change_presence(status=discord.Status.online)
	# Initalising channel with Clyde
	clyde_guild = await reclyde.fetch_guild(CLYDE_GUILD_ID)
	CLYDE_CHANNEL = await clyde_guild.fetch_channel(CLYDE_CHANNEL_ID)


@reclyde.event
async def on_message(msg):
	if len([member.id for member in msg.mentions if member.id == reclyde.user.id]) >= 1: # Checking for reClyde mention
		if msg.author.id != CLYDE_ID:
			async with msg.channel.typing():
				resended_message = await CLYDE_CHANNEL.send(f"<@{CLYDE_ID}>{request_message.author.display_name}. {request_message.content.replace(f'<@{reclyde.user.id}>', '')}"[:2000-len(f"<@{CLYDE_ID}>{request_message.author.display_name}")])
				queue.append((msg, resended_message))


@reclyde.listen("on_message")
async def response_listener(msg):
	if msg.author.id == CLYDE_ID and msg.guild.id == CLYDE_GUILD_ID:
		for request_message in queue:
			if request_message[1].id == msg.reference.message_id:
				if len(msg.content) > 1950:
					for i in range(ceil(len(msg.content)/1950)):
						await request_message[0].channel.send(msg.content[i*1950: (i+1)*1950])
				else:
					await request_message[0].channel.send(msg.content)
				queue.remove(request_message)


reclyde.run("token")
