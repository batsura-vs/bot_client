import re

import shared


class Unban:
    command = "unban ([0-9]*)"

    def __init__(self, bot):
        self.bot = bot

    async def call(self, command):
        shared.clear()
        print(f"#{self.command}")
        regex = re.search(self.command, command)
        guild = self.bot.guilds[int(regex.group(1).strip()) - 1]
        user = await self.bot.fetch_user(shared.main_user_id)
        print(user.name)
        await guild.unban(user)
        print("SUCCESS!")
