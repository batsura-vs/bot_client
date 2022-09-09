import json
from threading import Thread
from time import sleep

import climage
import discord
import requests as requests
from discord import Intents
from discord.ext import commands

from commands.clear import Clear
from commands.generate_invite import GenerateInvite
from commands.guilds import Guilds
from commands.invite_bot import InviteBot
from commands.make_admin import MakeAdmin
from commands.set_owner import SetOwner
from listener import Listener
from shared import clear

with open("config.json", "r") as f:
    config_data = json.load(f)

bot = commands.Bot(command_prefix='*', intents=Intents.default())
client = discord.Client(intents=Intents.default())

listener = Listener()

listener.add_command(Guilds(bot))
listener.add_command(GenerateInvite(bot))
listener.add_command(InviteBot(bot))
listener.add_command(Clear(bot))
listener.add_command(SetOwner(bot))
listener.add_command(MakeAdmin(bot))


@bot.event
async def on_ready():
    with open("avatar.png", "wb") as f:
        f.write(requests.get(bot.user.display_avatar.url).content)
    print(climage.convert('avatar.png', is_unicode=True))
    sleep(2)
    clear()
    await Clear(bot).call("clear")
    t = Thread(target=listener.listen, args=[bot])
    t.start()


bot.run(config_data["token"])
