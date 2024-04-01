from dependencies.utils import *

@client.slash_command(name="slash_foo", description="testing function")
async def slash_foo(interaction):
    await interaction.response.defer()
    return await interaction.send(content=f"bar")