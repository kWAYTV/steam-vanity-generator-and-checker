from random import choices
from string import ascii_lowercase
from pystyle import Colors, Colorate, Center
from colorama import Fore, Back, Style  #
from colorama import init  #
import os, time

global count
count = 0 # Don't touch this
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
mode = "" # This is selected on the tool, don't touch.


mainLogo = """
██╗░░░██╗░█████╗░███╗░░██╗██╗████████╗██╗░░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
██║░░░██║██╔══██╗████╗░██║██║╚══██╔══╝╚██╗░██╔╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
╚██╗░██╔╝███████║██╔██╗██║██║░░░██║░░░░╚████╔╝░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
░╚████╔╝░██╔══██║██║╚████║██║░░░██║░░░░░╚██╔╝░░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░╚██╔╝░░██║░░██║██║░╚███║██║░░░██║░░░░░░██║░░░  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝"""

def printMain():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, mainLogo, 1)))


logo = """
██╗░░░██╗░█████╗░███╗░░██╗██╗████████╗██╗░░░██╗  ░██████╗░███████╗███╗░░██╗
██║░░░██║██╔══██╗████╗░██║██║╚══██╔══╝╚██╗░██╔╝  ██╔════╝░██╔════╝████╗░██║
╚██╗░██╔╝███████║██╔██╗██║██║░░░██║░░░░╚████╔╝░  ██║░░██╗░█████╗░░██╔██╗██║
░╚████╔╝░██╔══██║██║╚████║██║░░░██║░░░░░╚██╔╝░░  ██║░░╚██╗██╔══╝░░██║╚████║
░░╚██╔╝░░██║░░██║██║░╚███║██║░░░██║░░░░░░██║░░░  ╚██████╔╝███████╗██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░╚═════╝░╚══════╝╚═╝░░╚══╝"""

def printLogo():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo, 1)))

clear()
def gen():
    global count, amount, end
    os.system(f"title Steam Vanity Generator - Ready!")


    print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "   \nHow many usernames do you want to generate?", 1)))
    amount = int(input())
    print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "   \nHow many characters long?", 1)))
    number = int(input())

    start = time.time()

    three_letter_words = ["".join(choices(ascii_lowercase, k=number)) for _ in range(amount)]

    with open('gen-output.txt', 'a') as f:
        t0 = time.time()
        for row in three_letter_words:
            f.write(''.join(row) + '\n')
            print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}", row)
            count += 1
            remaining = amount - count
            t1 = time.time() - t0
            os.system(f"title Steam Vanity Generator - Generated: {count} - Remaining: {remaining} - Elapsed: {round(t1)} seconds")
    
    end = time.time()
    elapsed = end - start
    os.system(f"title Steam Vanity Generator - Done! - Generated {count} usernames" + f" - Elapsed: {round(elapsed)} seconds")

time.sleep(2)
clear()
import requests, json, os, time
from pystyle import Colors, Colorate, Center
from colorama import Fore, Back, Style
from colorama import init
global count2, free, taken

apiKey = "" # Enter your Steam API Key here
count2 = 0 # Don't touch this
free = 0 # Don't touch this
taken = 0 # Don't touch this

logo2 = """
██╗░░░██╗░█████╗░███╗░░██╗██╗████████╗██╗░░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░
██║░░░██║██╔══██╗████╗░██║██║╚══██╔══╝╚██╗░██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗
╚██╗░██╔╝███████║██╔██╗██║██║░░░██║░░░░╚████╔╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝
░╚████╔╝░██╔══██║██║╚████║██║░░░██║░░░░░╚██╔╝░░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗
░░╚██╔╝░░██║░░██║██║░╚███║██║░░░██║░░░░░░██║░░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝\n\n"""

def printLogo2():
    print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo2, 1)))

def check():
    global count2, free, taken
    os.system(f"title Steam Vanity Checker - Ready!")
    with open("gen-output.txt","r") as f:
        content = f.read()
        lines = content.split("\n")
        with open(r"gen-output.txt", 'r') as fp:
                amount = len(fp.readlines())
        print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Found {amount} vanity's to check.")
        t3 = time.time()
        for line in lines:
            line = line.rstrip('\r\n')
            if line == "":
                continue
            global success
            response = requests.get(f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={apiKey}&vanityurl={line}")
            json_data = response.json()
            json.dumps(json_data, indent=4)
            print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Checking vanity: {line}")
            if not "response" in json_data:
                print(f"{Fore.RED}[{Fore.RESET}X{Fore.RED}] {Fore.RESET}{line} is not a valid Steam ID.")
                continue
            if "message" in json_data["response"]:
                message = json_data["response"]["message"]
            if "success" in json_data["response"]:
                success = json_data["response"]["success"]
            if "steamid" in json_data["response"]:
                steamId64 = json_data["response"]["steamid"]
            if success == 1:
                count2 += 1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}The id {line} is taken by user {steamId64}. Link: https://steamcommunity.com/id/{line}\n")
                with open('taken.txt', 'a') as takenList:
                    takenList.write(f"{line}\n")
                    taken += 1
            if success == 42:
                count2 += 1
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}The id {line} is free.\n")
                with open('free.txt', 'a') as freeList:
                    freeList.write(f"{line}\n")
                    free += 1
            remaining = amount - count2
            t4 = time.time() - t3
            os.system(f"title Steam Vanity Checker - Free: {free} - Taken: {taken} - Checked: {count2} - Remaining: {remaining} - Elapsed: {round(t4)} seconds")

def start():
    clear()
    os.system("title Steam Vanity Checker - Main Menu")
    print()
    printMain()
    print()
    print("> discord.gg/kws")
    print()
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_white, " Welcome!", 1)))
    print()
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [1] Generator - Only generate vanity's", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [2] Checker - Only check vanity's", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [3] Both - Do both of the tasks", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [4] Exit - Go away", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_green, "\n Choose a number", 1)))
    mode = input("\n > ")
    print(mode)

    if mode == "1":
        clear()
        printLogo()
        gen()
        os.system(f"title Steam Vanity Checker - Done! - Generated {count} usernames")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Generated {count} usernames", 1)))
        time.sleep(1)
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   \nPress any key to exit", 1)))
        input()
    if mode == "2":
        clear()
        printLogo2()
        check()
        os.system(f"title Steam Vanity Checker - Done! - Free: {free} - Taken: {taken} - Checked: {count2}")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Free: {free} - Taken: {taken} - Checked: {count2}", 1)))
        time.sleep(1)
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   \nPress any key to exit", 1)))
        input()
    if mode == "3":
        clear()
        printLogo()
        gen()
        time.sleep(1)
        clear()
        printLogo2()
        start2 = time.time()
        check()
        end2 = time.time()
        elapsed2 = end2 - start2
        os.system(f"title Steam Vanity Checker - Done! - Free: {free} - Taken: {taken} - Checked {count2} usernames - " + "Elapsed: {}".format(round(elapsed2)) + " seconds")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Free: {free} - Taken: {taken} - Generated: {count} - Checked: {count2} usernames - " + "Elapsed: {}".format(round(elapsed2)) + " seconds", 1)))
        time.sleep(1)
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   \nPress any key to exit", 1)))
        input()
    if mode == "4":
            clear()
            print()
            print(Center.XCenter(Colorate.Horizontal(
                Colors.white_to_red, " Goodbye...", 1)))
            time.sleep(2)
            exit()
    if mode != "1" and mode != "2" and mode != "3" and mode != "4":
            clear()
            print()
            print(Center.XCenter(Colorate.Horizontal(
                Colors.white_to_red, " Invalid Option!", 1)))
            time.sleep(2)
try:
    start()
except KeyboardInterrupt:
    clear()
    print()
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_red, " Goodbye...", 1)))
    time.sleep(2)
    exit()