from dependencies.utils import *

@client.command(name="foo", description="testing function")
async def foo(ctx, *args):
    return await ctx.send("bar")