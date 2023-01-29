import requests
from os import system
from colorama import Fore

title = "EngineOwner ║ TokenInfo"

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def information(token):
    system("title " + title)
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''
    [{Fore.RED}User ID]         {userID}
    [{Fore.RED}User Name]       {userName}
    [{Fore.RED}2 Factor]        {mfa}
    [{Fore.RED}Email]           {email}
    [{Fore.RED}Phone number]    {phone if phone else "None"}
    [{Fore.RED}Token]           {token}
                ''')
        input('Press any key to continue...')
        clearcmd()
        os.system('python main.py')
