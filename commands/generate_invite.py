import re

from shared import clear


class GenerateInvite:
    command = "generate invite (.*)"

    def __init__(self, bot):
        self.bot = bot

    async def call(self, command):
        clear()
        print(f"#{self.command}")
        regex = re.search(self.command, command)

        try:
            guild = self.bot.guilds[int(regex.group(1).strip()) - 1]
            invite = await guild.text_channels[0].create_invite(max_age=60, max_uses=1, temporary=False)
            print(f"https://discord.gg/{invite.code}")
        except Exception as e:
            print(e)
