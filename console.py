"""
A basic TriggerCreater in Python
It is used with an EventLogger from an executor, like redENGINE. You'll need to know how to use an event logger before you can take advantage of this script. 
"""

import os 
from colorama import Fore

os.system("title Trigger Creater && cls")

def create_trigger(parem1, parem2):
    cleaned_parem2 = parem2.strip('[]')
    if ',' in cleaned_parem2:
        values = ','.join(value.strip() for value in cleaned_parem2.split(','))
        trigger = f"TriggerServerEvent('{parem1.strip('"')}', {values})"
    else:
        numeric_value = float(cleaned_parem2)
        if numeric_value.is_integer():
            numeric_value = int(numeric_value)
            trigger = f"TriggerServerEvent('{parem1.strip('"')}', {numeric_value})"
        else:
            trigger = f"TriggerServerEvent('{parem1.strip('"')}', {numeric_value})"

        # trigger = f"TriggerServerEvent('{parem1.strip('[]"')}', '{cleaned_parem2}')"

    print(f"{Fore.RED}[!]{Fore.RESET}Trigger --> {trigger}")

if __name__ == "__main__":
    parem1 = input(f"{Fore.GREEN}[?]{Fore.RESET}Enter the first parameter (parem1): ")
    parem2 = input(f"{Fore.GREEN}[?]{Fore.RESET}Enter the second parameter (parem2): ")

    create_trigger(parem1, parem2)

