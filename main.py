from os import system
from colorama import Fore
from tools.webhook import dwebhook
from tools.massdm import massdmer
from tools.tokeninfo import information
from tools.serverleaver import leaver
from tools.unfriend import unfriender
from tools.closedm import dmcloser

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
                     ║ [9] Token Grabber             ║   ║                               ║
                     ╚═══════════════════════════════╝   ╚═══════════════════════════════╝
"""
option = Fore.RED + "     [>] "

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
        input(Fore.RED + "By using this project, you agree to not use it for illegal activites, we(Snee, github.com/itssnee/) ARE NOT responsible for the user's actions.")
owner()
