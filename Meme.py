# ---------------------------------------------------------------------------------
# Name: Meme
# Description: Continuation
# Author: @hikka_mods
# Commands:
# ---------------------------------------------------------------------------------

# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hikka_mods
# scope: Meme
# scope: Meme 0.0.1
# ---------------------------------------------------------------------------------

import asyncio
from urllib.parse import quote_plus
from datetime import datetime
from bs4 import BeautifulSoup
import logging

import aiohttp
import random
import urllib.request
import json
from telethon.tl.types import Message

from .. import loader, utils

@loader.tds
class MemesMod(loader.Module):
    """continuation """

    strings = {
              "name": "Memes",
              "done": "☄️ Catch the meme",
              "still": "🔄 Update",
              "dell": "❌ Close",
    }

    strings_ru = {
              "done": "☄️ Лови мем",
              "still": "🔄 Обновить",
              "dell": "❌ Закрыть",
    }

    async def memscmd(self, message: Message):
        random_site = random.randint(1, 2857)
        url = f"https://www.memify.ru/memes/{random_site}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, "html.parser")
                items = soup.find_all("div", {"class": "infinite-item card"})
                random_item = random.choice(items)
                second_a = random_item.find_all("a")[1]
                img = second_a.get("href")

        await self.inline.form(
            text=self.strings("done"),
            photo=img,
            message=message,
            reply_markup=[
                    [{
                        "text": self.strings("still"),
                        "callback": self.ladno,
                    }],
                    [{
                        "text": self.strings("dell"),
                        "callback": self.dell,
                    }]
            ],
            silent=True,
        )

    async def ladno(self, call):
        # Do some stuff
        random_site = random.randint(1, 2857)
        url = f"https://www.memify.ru/memes/{random_site}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, "html.parser")
                items = soup.find_all("div", {"class": "infinite-item card"})
                random_item = random.choice(items)
                second_a = random_item.find_all("a")[1]
                img = second_a.get("href")

        await call.edit(
            text=self.strings("done"),
            photo=img,
            reply_markup=[
                    [{
                        "text": self.strings("still"),
                        "callback": self.ladno,
                    }],
                    [{
                        "text": self.strings("dell"),
                        "callback": self.dell,
                    }]
            ],
        )

    async def dell(self, call):
        """Callback button"""
        await call.delete()
