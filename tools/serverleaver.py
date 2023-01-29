import requests
from colorama import Fore

title = "EngineOwner | Server Leaver"

def leaveServer(token):
    system("title " + title)
    headers = {'Authorization': token}
    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
            print(f"{Fore.RED}[ C ] Left Server: "+guild['name'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
