import requests
from os import system
from colorama import Fore

title = "EngineOwner | Close All Dm's"
system("title " + title)

def dmcloser(token):
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
    for channel in close_dm_request:
        print(f"{Fore.RED}[ C ] ID: "+channel['id'] +)
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers)
