import os
from os import system
from colorama import Fore
from tools.webhook import dwebhook

title = "EngineOwner"
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
                     ║ [2] Leave Servers             ║   ║ [11] Token Info               ║
                     ║ [3] Delete Friends            ║   ║ [12] Token Checker            ║
                     ║ [4] Delete Servers            ║   ║ [13] Fuck Account             ║
                     ║ [5] Mass Dm                   ║   ║ [14] Delete Webhook           ║
                     ║ [6] Close DMs                 ║   ║                               ║
                     ║ [7] Create Servers            ║   ║ [15] CREDITS                  ║
                     ║ [8] Block All Friends         ║   ║ [17] EXIT                     ║
                     ║ [9] Token Grabber             ║   ║                               ║
                     ╚═══════════════════════════════╝   ╚═══════════════════════════════╝
"""
option = Fore.RED + "    [>] "

def owner():
    lmao = input(banner + option)
    if lmao == "17":
        quit()
    elif lmao == "14":
        link = input("Enter the Webhook you want to delete.")
        dwebhook(link)
    elif lmao == "15":
        print("made by Snee")
        print("https://github.com/itssnee/engine-owner")
        print("To close this credit scene, press enter.")
        input("")
owner()
