import re
import shared as sh
from shared import clear


class SetOwner:
    command = "set owner (.*)"

    def __init__(self, bot):
        self.bot = bot

    async def call(self, command):
        regex = re.search(self.command, command)
        owner_id = regex.group(1)
        sh.main_user_id = owner_id
        print(f"Owner has been changed {sh.main_user_id}")
