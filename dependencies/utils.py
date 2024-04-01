from dependencies.client import *

class EmbedNav:
    class section:
        class field:
            def __init__(self, name="\u200B", value="\u200B", inline=False):
                self.name = name
                self.value = value
                self.inline = inline

        @staticmethod
        def Create(title="\u200B", description="\u200B", color=disnake.Color.random(), fields=False, data=[], image=None, url=None):
            embed = disnake.Embed(title=title, description=description, color=color) if not url else disnake.Embed(title=title, description=description, color=color, url=url)
            if fields:
                for field in data:
                    embed.add_field(name=field.name, value=field.value, inline=field.inline)
            if image:
                embed.set_image(url=image)
            return embed
        
    def __init__(self, embeds=[], select=None, select_content='Select'):
        self.embeds = embeds
        self.index = 0
        self.embed = self.embeds[self.index]
        self.length = len(self.embeds) - 1
        self.view = View(timeout=None)
        self.selectb = Button(label=select_content, style=disnake.ButtonStyle.green) if select else None
        self.previousb = Button(label='Previous', style=disnake.ButtonStyle.primary)
        self.nextb = Button(label='Next', style=disnake.ButtonStyle.primary)
        
        for button in [self.previousb, self.selectb, self.nextb] if select else [self.previousb, self.nextb]:
            self.view.add_item(button)
        
        self.previousb.callback = self.on_previous
        self.nextb.callback = self.on_next

        if select:
            self.selectb.callback = select

    async def update_message(self):
        self.embed.set_footer(text=f"{self.index + 1} of {self.length + 1} pages")
        await self.message.edit(embed=self.embed, view=self.view)

    async def on_previous(self, interaction):
        await interaction.response.defer()
        if self.index == 0:
            self.index = self.length
        else:
            self.index -= 1
        self.embed = self.embeds[self.index]
        await self.update_message()

    async def on_next(self, interaction):
        await interaction.response.defer()
        if self.index == self.length:
            self.index = 0
        else:
            self.index += 1
        self.embed = self.embeds[self.index]
        await self.update_message()