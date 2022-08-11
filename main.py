# Coded by kWAY#1701 - discord.gg/kws - kwayservices.top
# Steam Vanity Generator & Checker

import os
try:
    import requests, os, json, time, webbrowser, colorama, pystyle, xml
    print("\nImports successful!")
except:
    print("\nImports failed! Trying to install...")
    z = "python -m pip install "; os.system('%srequests' % (z)); os.system('%sos-sys' % (z)); os.system('%sjsonlib' % (z)); os.system('%stime' % (z)); os.system('%swebbrowser' % (z)); os.system('%scolorama' % (z)); os.system('%spystyle' % (z)); os.system('%sxml' % (z))
    print("\nImports successful!")

# ------------ IMPORTS -----------
import requests, os, json, time, webbrowser, colorama, pystyle, xml
from random import choices
from string import ascii_lowercase
from pystyle import Colors, Colorate, Center
from colorama import Fore, Back, Style
from colorama import init

# -----------  CODE  -------------
# Generator & General Settings
global count
count = 0 # Don't touch this
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
mode = "" # This is selected on the tool, don't touch.

# Tool Logo
mainLogo = """
██╗░░░██╗░█████╗░███╗░░██╗██╗████████╗██╗░░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
██║░░░██║██╔══██╗████╗░██║██║╚══██╔══╝╚██╗░██╔╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
╚██╗░██╔╝███████║██╔██╗██║██║░░░██║░░░░╚████╔╝░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
░╚████╔╝░██╔══██║██║╚████║██║░░░██║░░░░░╚██╔╝░░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░╚██╔╝░░██║░░██║██║░╚███║██║░░░██║░░░░░░██║░░░  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝"""

def printMain():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, mainLogo, 1)))


# Vanity Generator Logo
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

# Vanity Generator
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
from pystyle import Colors, Colorate, Center
from colorama import Fore, Back, Style
from colorama import init
from xml.etree import ElementTree
global count2, free, taken

# Steam API Key
apiKey = "" # Enter your Steam API Key here

# User Vanity Settings
count2 = 0 # Don't touch this
free = 0 # Don't touch this
taken = 0 # Don't touch this

# Group Vanity Settings
freeGroups = 0 # Don't touch this
takenGroups = 0 # Don't touch this
count3 = 0 # Don't touch this

# Vanity Checker logo
logo2 = """
██╗░░░██╗░█████╗░███╗░░██╗██╗████████╗██╗░░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░
██║░░░██║██╔══██╗████╗░██║██║╚══██╔══╝╚██╗░██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗
╚██╗░██╔╝███████║██╔██╗██║██║░░░██║░░░░╚████╔╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝
░╚████╔╝░██╔══██║██║╚████║██║░░░██║░░░░░╚██╔╝░░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗
░░╚██╔╝░░██║░░██║██║░╚███║██║░░░██║░░░░░░██║░░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝\n\n"""

def printLogo2():
    print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo2, 1)))


# Steam User Vanity Checker
def vCheck():
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
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}The id {line} is taken.")
                with open('taken-user.txt', 'a') as takenList:
                    takenList.write(f"{line}\n")
                    taken += 1
            if success == 42:
                count2 += 1
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}The id {line} is free.")
                with open('free-user.txt', 'a') as freeList:
                    freeList.write(f"{line}\n")
                    free += 1
            remaining = amount - count2
            t4 = time.time() - t3
            os.system(f"title Steam User Vanity Checker - Free: {free} - Taken: {taken} - Checked: {count2} - Remaining: {remaining} - Elapsed: {round(t4)} seconds")

# Steam Group Vanity Checker
def gCheck():
    global count3, freeGroups, takenGroups
    os.system(f"title Steam Group Vanity Checker - Ready!")
    with open("gen-output.txt","r") as f:
        content = f.read()
        lines = content.split("\n")
        with open(r"gen-output.txt", 'r') as fp:
                amount = len(fp.readlines())
        print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Found {amount} group vanity's to check.")
        t5 = time.time()
        for line in lines:
            line = line.rstrip('\r\n')
            if line == "":
                continue
            global success
            response = requests.get(f"https://steamcommunity.com/actions/AvailabilityCheck?&type=groupLink&value={line}").text
            if f"The group link, {line}, is already in use by another group" in response:
                count3 += 1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}The group vanity {line} is taken.")
                with open('taken-groups.txt', 'a') as tgList: 
                    tgList.write(f"{line}\n")
                    freeGroups += 1
            elif f"The group link, {line}, is available!" in response:
                count3 += 1
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}The group vanity {line} is free.")
                with open('free-groups.txt', 'a') as fgList:
                    fgList.write(f"{line}\n")
                    takenGroups += 1
            remainingGroups = amount - count3
            t6 = time.time() - t5
            os.system(f"title Steam Group Vanity Checker - Free: {freeGroups} - Taken: {takenGroups} - Checked: {count3} - Remaining: {remainingGroups} - Elapsed: {round(t6)} seconds")

# Open Website
import webbrowser
def openWebsite():
    webbrowser.open("https://kwayservices.top/")

# Define the main menu
def start():
    clear()
    os.system("title Steam Vanity Checker - Main Menu")
    print()
    printMain()
    print()
    print(" > kwayservices.top")
    print()
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_white, " Welcome!", 1)))
    print()
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [1] Vanity Generator.", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [2] User Vanity Checker.", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [3] Gen & User Vanity Checker.", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [4] Group Vanity Checker.", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [5] Gen & Group Vanity Checker.", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [6] Generate & Check both users and group vanity's.", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [7] Wipe Data - Wipe all your txt files.", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [8] Open the website (discord there).", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [9] Exit - Close the tool.", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_green, "\n Choose a number", 1)))
    mode = input("\n > ")

# Only generate vanity's
    if mode == "1":
        clear()
        printLogo()
        gen()
        os.system(f"title Steam Vanity Checker - Done! - Generated {count} usernames")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Generated {count} usernames", 1)))
        time.sleep(1)
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   \nPress any key to go back to main menu", 1)))
        start()
# Only check user vanity's
    if mode == "2":
        clear()
        printLogo2()
        vCheck()
        os.system(f"title Steam Vanity Checker - Done! - Free: {free} - Taken: {taken} - Checked: {count2}")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Free: {free} - Taken: {taken} - Checked: {count2}", 1)))
        time.sleep(1)
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   \nPress any key to go back to main menu", 1)))
        start()
# Generate and check user vanity's
    if mode == "3":
        clear()
        printLogo()
        gen()
        time.sleep(1)
        clear()
        printLogo2()
        start2 = time.time()
        vCheck()
        end2 = time.time()
        elapsed2 = end2 - start2
        os.system(f"title Steam Vanity Checker - Done! - Free: {free} - Taken: {taken} - Checked {count2} usernames - " + "Elapsed: {}".format(round(elapsed2)) + " seconds")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Free: {free} - Taken: {taken} - Generated: {count} - Checked: {count2} usernames - " + "Elapsed: {}".format(round(elapsed2)) + " seconds", 1)))
        time.sleep(1)
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   \nPress any key to go back to main menu", 1)))
        start()
# Only check group vanity's
    if mode == "4":
        clear()
        printLogo2()
        gCheck()
        os.system(f"title Steam Group Vanity Checker - Done! - Free: {free} - Taken: {taken} - Checked: {count3}")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Free: {free} - Taken: {taken} - Checked: {count3}", 1)))
        time.sleep(1)
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   \nPress any key to go back to main menu", 1)))
        start()
# Generate and check group vanity's
    if mode == "5":
        clear()
        printLogo()
        gen()
        time.sleep(1)
        clear()
        printLogo2()
        start3 = time.time()
        gCheck()
        end3 = time.time()
        elapsed3 = end3 - start3
        os.system(f"title Steam Vanity Checker - Done! - Free: {free} - Taken: {taken} - Checked {count2} usernames - " + "Elapsed: {}".format(round(elapsed3)) + " seconds")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Free: {free} - Taken: {taken} - Generated: {count} - Checked: {count3} usernames - " + "Elapsed: {}".format(round(elapsed3)) + " seconds", 1)))
        time.sleep(1)
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   \nPress any key to go back to main menu", 1)))
        start()
# Generate and check user & group vanity's
    if mode == "6":
        clear()
        printLogo()
        gen()
        time.sleep(1)
        clear()
        printLogo2()
        start2 = time.time()
        vCheck()
        end2 = time.time()
        elapsed2 = end2 - start2
        os.system(f"title Steam Vanity Checker - Done! - Free: {free} - Taken: {taken} - Checked {count2} usernames - " + "Elapsed: {}".format(round(elapsed2)) + " seconds")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Free: {free} - Taken: {taken} - Generated: {count} - Checked: {count2} usernames - " + "Elapsed: {}".format(round(elapsed2)) + " seconds", 1)))
        time.sleep(1)
        clear()
        printLogo2()
        gCheck()
        os.system(f"title Steam Group Vanity Checker - Done! - Free: {free} - Taken: {taken} - Checked: {count3}")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, f"   \nDone! - Free: {free} - Taken: {taken} - Checked: {count3}", 1)))
        time.sleep(1)
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "   \nPress any key to go back to main menu", 1)))
        start()
# Delete all of the .txt in the directory (data wipe)
    if mode == "7":
        print(Center.XCenter(Colorate.Horizontal(
                Colors.white_to_red, " Wiping data...", 1)))
        time.sleep(2)
        mydir = os.getcwd()
        txt = [ f for f in os.listdir(mydir) if f.endswith(".txt") ]
        for f in txt:
            os.remove(os.path.join(mydir, f))
        print(Center.XCenter(Colorate.Horizontal(
                Colors.white_to_green, " Done! Going back to main menu...", 1)))
        time.sleep(0.3)
        start()
# Open website
    if mode == "8":
        openWebsite()
        print(Center.XCenter(Colorate.Horizontal(
                Colors.white_to_green, " Done! Going back to main menu...", 1)))
        time.sleep(0.3)
        start()
# Exit the program
    if mode == "9":
        clear()
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_red, " Goodbye...", 1)))
        time.sleep(1)
        exit()
    if mode != "1" and mode != "2" and mode != "3" and mode != "4" and mode != "5" and mode != "6" and mode != "7" and mode != "8" and mode != "9":
            clear()
            print()
            print(Center.XCenter(Colorate.Horizontal(
                Colors.white_to_red, " Invalid Option!", 1)))
            time.sleep(0.85)
            start()

# Start the program with KeyboardInterrupt exception
try:
    start()
except KeyboardInterrupt:
    clear()
    print()
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_red, " Goodbye...", 1)))
    time.sleep(2)
    exit()