import requests
from colorama import Fore
from os import system

title = "EngineOwner | Delete Friends"
system("title " + title)

def unfriender(token):
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(token))
            print(f"[ {Fore.RED}C] Removed Friend: "+friend['user']['username']+"#"+friend['user']['discriminator'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
