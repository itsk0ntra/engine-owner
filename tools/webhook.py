import requests
import time
import os
from colorama import Fore

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def dwebhook(hook):
    requests.delete(hook)
    print(Fore.RED + "Deleted the Webhook.")
    time.sleep(1.00)
    print("if you like the project, give it a star at https://github.com/itssnee/engine-owners")
    clearcmd()
    os.system('python main.py')