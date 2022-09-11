from os import system
from colorama import *
from rich import *
import time
import os
import json
from requests import get

url = "http://ipinfo.io/json"
resp = get(url)
json = resp.json()
IP = json['ip']
banner = f"""
 
 
                        ▄▄▄       ███▄ ▄███▓ ███▄    █ ▓█████   ██████  ██▓ ▄▄▄         
                        ▒████▄    ▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒████▄       
                        ▒██  ▀█▄  ▓██    ▓██░▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒▒██  ▀█▄     
                        ░██▄▄▄▄██ ▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░░██▄▄▄▄██    
                        ▓█   ▓██▒▒██▒   ░██▒▒██░   ▓██░░▒████▒▒██████▒▒░██░ ▓█   ▓██▒   
                        ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░   
                        ▒   ▒▒ ░░  ░      ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░   
                        ░   ▒   ░      ░      ░   ░ ░    ░   ░  ░  ░   ▒ ░  ░   ▒      
                            ░  ░       ░            ░    ░  ░      ░   ░        ░  ░   
                                                                    
                                    ------------------------------------
                                    -      YOUR IP : {IP}     -
                                    ------------------------------------
    
    """
while True:
    url = "http://ipinfo.io/json"
 
    os.system(f'Title - IP Pinger - BKS#1958')
    console = get_console()
    console.print(banner, style="bold blue")

    ip = console.input("{[blue]?[/blue]} Enter IP: ")
    system(f'ping {ip}')
    time.sleep(2)
    os.system('cls||clear')
