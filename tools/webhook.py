import requests
import time
import os
from os import system
from colorama import Fore

title = "EngineOwner | Webhook Deleter"

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def dwebhook(hook):
    system("title " + title)
    requests.delete(hook)
    print(Fore.RED + "Deleted the Webhook.")
    time.sleep(1.00)
    print("if you like the project, give it a star at https://github.com/itssnee/engine-owners")
    clearcmd()
    os.system('python main.py')
