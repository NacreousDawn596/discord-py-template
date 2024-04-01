from dependencies.utils import *

@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")
    await client.change_presence(status=disnake.Status.idle, activity=disnake.Activity(type=disnake.ActivityType.playing, name="foo", url="bar"))