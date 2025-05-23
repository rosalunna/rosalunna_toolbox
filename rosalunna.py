# Default Imports
import os
import subprocess
import shutil
import winreg
import sys
import stat
import ctypes
import zipfile
import platform
import time
# 3rd Party Imports
from rich import print
from rich.table import Table
from colorama import Fore, Style
import requests
from urllib.request import urlretrieve
from itertools import zip_longest
# Local Imports
from Utils.tweaks import *
from Utils.installations import *
from Utils.regedit_services import *
from Utils.browsers import *
from Utils.apps import *


# Starting Script Buildup
art = """[#f54284]
 ___ ___ ___ ___| |_ _ ___ ___ ___   | |_ ___ ___| | |_ ___ _ _ 
|  _| . |_ -| .'| | | |   |   | .'|  |  _| . | . | | . | . |_'_|
|_| |___|___|__,|_|___|_|_|_|_|__,|  |_| |___|___|_|___|___|_,_|

|--------------------------------------------------------------|[/#f54284]"""

# Column Width Variable for some menus
column_width = 80

# Main Menu & Main Loop
def main_menu():
    # OS and Script Information
    script_version = ("[#7d0137] Toolbox Version:[/#7d0137] [#eb05b5]2.0.0-alpha[/#eb05b5]")
    OS_VER = platform.platform()
    OS_VER_SHOW = (f"[#7d0137]Current OS Version:[/#7d0137] [#eb05b5]{OS_VER}[/#eb05b5]")
    
    # Names list and Choices Dictionary for Main Menu
    names = ["[#78fab2] [1] Extremely Recommended[/#78fab2] ", "[#5F6E81] [2][/#5F6E81] [#0073ff]Brow[/#0073ff][#bd6902]sers[/#bd6902] ",
             "[#7d0137] [3] Applications[/#7d0137] ", "[#00f4ff] [4] Development[/#00f4ff]", "[#fc0345] [5] Debloat[/#fc0345]",
             "[#5a03fc] [6] Tweaks[/#5a03fc]", "[#fc0345] [7] Windows ISO Debloat[/#fc0345] ", " "
            ]    
    actions = {
    "1": rec_menu,
    "2": browsers_menu,
    "3": apps_menu,
    "4": development_menu,
    "5": debloat_menu,
    "6": tweaks_menu,
    "7": iso_menu,
 }    
    clear_screen()
    rich.print(art)
    rich.print("[#7d0137] SCRIPT MUST BE RAN AS[/#7d0137]","[#bf6000]ADMINISTRATOR,[/#bf6000]","[#7d0137]RESTART IF NEEDED[/#7d0137]")
    rich.print(script_version.ljust(80) + OS_VER_SHOW)
    rich.print("[#f54284]|---------------------------------------------------------------------------------------|[/#f54284]")
    
    # Main Menu Text Display and Input Choices
    leftC = names[:4]
    rightC = names[4:]
    table = Table(show_header=False, show_edge=True, padding=0)
    
    for left, right in zip_longest(leftC, rightC):
        table.add_row(left, right)
    rich.print(table)     
    choice = input("\n Choose an option: ")
    match choice:
        case "0":
            c1 = input(" Do you confirm on exiting the application (Y/N)? ")
            if c1.lower() == "y":
                clear_screen()
                rich.print("[#fc0345]Exiting[/#fc0345] the application.")
                time.sleep(1.5)
                sys.exit()
            elif c1.lower() == "n":
                clear_screen()
                rich.print("Going [#00f4ff]back[/#00f4ff] to main menu.")
                time.sleep(1.2)
                clear_screen()
                main_menu()
            else:
                rich.print("[#fc0345]Not known option. Try again[/#fc0345]")
                time.sleep()
                clear_screen()
                main_menu()
        case _ if choice in actions:
            clear_screen()
            actions[choice]()
        
        case _:
            print("\nNot known option.")
            time.sleep(1.5)
            main_menu()

                               
# [1] Recommended Installations Menu
def rec_menu():
    clear_screen()
    rich.print("[#ff0066]Recommended Installations[/#ff0066] on a Stripped Machine\n")
    rich.print("[#bf046e]These are all the programs that are going to be installed: [/#bf046e]\n")
    list = ["DirectX", "Visual C++", ".NET"]
    for item in list:
            rich.print(f"[#a83256]{item}[/#a83256]")
        
    packages = {"DirectX": ["directx"],
                "Visual C++": ["vcredist-140", "vcredist-all", "microsoft-vclibs"],
                ".NET": ["dotnet-8.0-runtime", "dotnetcore-runtime", "dotnet-runtime", "dotnet-desktopruntime",
                         "aspnetcore-runtimepackages", "dotnetcore-desktopruntime", "dotnetfx"]                
    }
    
    a = rich.print("\n[#326ba8]Do you want to proceed the installations (Y/N)?[/#326ba8]")
    
    b = input(a)
    if b == "y".lower():
        for names, package in packages.items():
            print(f"Installing {names}")
            for package in packages:
                choco_install(package)
    elif b == "n".lower():
        rich.print("Going [#00f4ff]back[/#00f4ff] to main menu.")
        time.sleep(1.2)
        clear_screen()
        main_menu() 
    else:
        rich.print("[#a83246]INVALID OPTION[/#a83246]")
        time.sleep(2)
        clear_screen()
        rec_menu()
          
# [2] Browsers Menu Stated in browsers.py

# [3]Apps Menu
def apps_menu():
    print("[#7d0137]Applications Menu[/#7d0137]\n")
    names = {
        
        "1": {"label": "[#7307a8]Gaming Platforms[/#7307a8]", "action": platform_menu},
        "2": {"label": "[#006bff]Common Applications and Utilities[/#006bff]", "action": apps_utils},
        "3": {"label": "[#006bff]Hardware Monitoring and Benchmarking[/#006bff]", "action": monitoring_overclocking},
        "4": {"label": "[#006bff]Peripheals[/#006bff]", "action": peripheals_apps},
        "5": {"label": "[#800080]PC Modding/Customizing[/#800080]", "action": custom_mod}
    }
    for number, details in names.items():
        rich.print(f"[{number}] {details ['label']}")
    choice = input("\nChoose an option: ")
    if choice in names:
        clear_screen()
        names[choice]["action"]()
    elif choice == "0":
        main_menu()
    else:
        print("Invalid Option!")    

# [4] Development Menu Stated in apps.py

# [5] Debloat Menu
def debloat_menu():
    rich.print("This option is meant for [#d67200]ADVANCED[/#d67200] USERS")
    time.sleep(2)
    rich.print("\nProceed with [#d60000]EXTREME[/#d60000] Caution!\nEnsure you know what [#d60000]EVERY[/#d60000] option means.")
    time.sleep(2)
    rich.print("This application is not responsible for any possible [#250052]DAMAGE[/#250052] in your OS or Computer.")
    time.sleep(1)
    print("\n")
    O1 = "[#fc0345][1][/#fc0345] Auto Debloat [#fc0345]REMOVING[/#fc0345] Windows Security"
    O2 = "[#0039ab][2][/#0039ab] Auto Debloat [#0039ab]KEEPING[/#0039ab] Windows Security"
    O3 = "[#fc0345][3][/#fc0345] [#fc0345]PAUSE[/#fc0345] Windows Updates"
    O4 = "[#0039ab][4][/#0039ab] [#0039ab]UNPAUSE[/#0039ab] Windows Updates"
    O5 = "[#fc0345][5][/#fc0345] Auto Debloat [#fc0345]REMOVING[/#fc0345] Windows Security and Updates"
    
    rich.print(O1.ljust(100) + O2)
    rich.print("\n[#4a00ab]WINDOWS UPDATE SECTION[/#4a00ab]")
    rich.print(O3.ljust(100) + O4)
    rich.print("\n[#fc0345]MAXIMUM DEBLOAT OPTION[/#fc0345]")
    rich.print(O5)
    rich.print("\n[#fc0345][0] Back to main menu[/#fc0345]")
    
    choice = input("\nSelect an option: ")
    match choice:
        case "0":
            clear_screen()
            main_menu()
        case "1":
            clear_screen()
            rich.print("[#fc0345]Debloat Removing Security is starting![/#fc0345]")
            time.sleep(3)
        
            # Regedit
            rich.print("\n01.Modifying Regedit Keys")
            time.sleep(2)
            regedit()
        
            # Services.msc
            rich.print("\n02.Modifying Windows Services")
            time.sleep(2)
            remove_services()
        
            # Remove Security and MS EDGE
            rich.print("\n03.Removing Windows Security")
            time.sleep(2)
            defender_total_removal()
        
            rich.print("\n04.Removing MS EDGE")
            time.sleep(2)
            ms_edgeR()
        
            # Raphire
            rich.print("\n05.Modifying and Executing Raphire Script")
            time.sleep(2)
            raphire_install_txt_change()
            raphire_execute_modscript()
        
            # Tweaking RAM
            rich.print("\n06.Tweaking RAM with RAMMAP")
            time.sleep(2)
        
            choco_install("rammap")
            ram_map()
            schedule_rammap()
        
            rich.print("\n07.Downloading O&O SHUTUP and Executing")
            time.sleep(2)
            download_file("https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe", "OOSU10.exe")
        case "2":
            clear_screen()
            rich.print("Debloat keeping Security is starting!")
            time.sleep(3)
        
            # Regedit
            rich.print("\n01.Modifying Regedit Keys")
            time.sleep(2)
            regedit()
        
            # Services.msc
            rich.print("\n02.Modifying Windows Services")
            time.sleep(2)
            remove_services()
        
            # Remove MS EDGE        
            rich.print("\n03.Removing MS EDGE")
            time.sleep(2)
            ms_edgeR()
        
            # Raphire
            rich.print("\n04.Modifying and Executing Raphire Script")
            time.sleep(2)
            raphire_install_txt_change()
            raphire_execute_modscript()
        
            # Tweaking RAM
            rich.print("\n05.Tweaking RAM with RAMMAP")
            time.sleep(2)
        
            choco_install("rammap")
            ram_map()
            schedule_rammap()
        
            rich.print("\n06.Downloading O&O SHUTUP and Executing")
            time.sleep(2)
            download_file("https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe", "OOSU10.exe")                                                
        case "3":
            rich.print("\n[#fc0345]Pausing Windows Updates Until 2051[/#fc0345]")
            time.sleep(2)
            user_profile = os.environ.get('USERPROFILE')
            windowsUPK = os.path.join(user_profile, "windows-update-killer")
            windowsUPD = os.path.join(user_profile, "windows-update-disabler")
            # Clean if already exists

            force_clean_directory(windowsUPK)
            force_clean_directory(windowsUPD)
            # Clone W-Update repos

            git_clone("https://github.com/Aetherinox/windows-update-killer/")
            git_clone("https://github.com/tsgrgo/windows-update-disabler.git")
            try:
                subprocess.run(["powershell", "-Command", "%USERPROFILE%\\windows-update-disabler\\disable updates.bat"],text=True, shell= True
                           )
                subprocess.run(["powershell", "-Command", "regedit", "/s", "%USERPROFILE%\\windows-update-killer\\windows-updates-pause.reg"], text=True, shell= True
                           )
            except subprocess.CalledProcessError as e:
                print(f"An error has occurred: {e}")
            
            time.sleep(1)
            rich.print("[#00ff91]Operation Was Succesful[/#00ff91]")
            time.sleep(1)     
        case "4":
            print("[#0039ab]RE-ENABLING/ENABLING Windows Updates[/#0039ab]")
            force_clean_directory(windowsUPK)
            force_clean_directory(windowsUPD)

            git_clone("https://github.com/Aetherinox/windows-update-killer/")
            git_clone("https://github.com/tsgrgo/windows-update-disabler.git")
            try:
                subprocess.run(["powershell", "-Command", "%USERPROFILE%\\windows-update-disabler\\enable updates.bat"],capture_output=True, shell= True
                           )
                subprocess.run(["powershell", "-Command", "regedit", "/s", "%USERPROFILE%\\windows-update-killer\\windows-updates-unpause.reg"],capture_output=True, shell= True
                           )
            except subprocess.CalledProcessError as e:
                print(f"An error has occurred: {e}")
        case "5":
            clear_screen()
            rich.print("[#fc0345]Debloat Removing Security and Updates is starting![/#fc0345]")
            time.sleep(3)
        
            # Regedit
            rich.print("\n01.Modifying Regedit Keys")
            time.sleep(2)
            regedit()
        
            # Services.msc
            rich.print("\n02.Modifying Windows Services")
            time.sleep(2)
            remove_services()
        
            # Remove Security and MS EDGE
            rich.print("\n03.Removing Windows Security")
            time.sleep(2)
            defender_total_removal()
        
            rich.print("\n04.Removing MS EDGE")
            time.sleep(2)
            ms_edgeR()
        
            # Raphire
            rich.print("\n05.Modifying and Executing Raphire Script")
            time.sleep(1)
            rich.print("[#900C3F]This step may take TIME[/#900C3F]")
            time.sleep(3)
            raphire_install_txt_change()
            raphire_execute_modscript()
        
            # Tweaking RAM
            rich.print("\n06.Tweaking RAM with RAMMAP")
            time.sleep(2)
        
            choco_install("rammap")
            ram_map()
            schedule_rammap()
            # OO SHUTUP
            rich.print("\n07.Downloading O&O SHUTUP and Executing")
            time.sleep(2)
            download_file("https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe", "OOSU10.exe")
        
            # WUPDATE
            rich.print("\n08.Removing Windows Update")
            time.sleep(2)
            user_profile = os.environ.get('USERPROFILE')
            windowsUPK = os.path.join(user_profile, "windows-update-killer")
            windowsUPD = os.path.join(user_profile, "windows-update-disabler")
            # Clean if already exists

            force_clean_directory(windowsUPK)
            force_clean_directory(windowsUPD)
            # Clone W-Update repos

            git_clone("https://github.com/Aetherinox/windows-update-killer/")
            git_clone("https://github.com/tsgrgo/windows-update-disabler.git")
            try:
                subprocess.run(["powershell", "-Command", "%USERPROFILE%\\windows-update-disabler\\disable updates.bat"],capture_output=True, shell= True
                           )
                subprocess.run(["powershell", "-Command", "regedit", "/s", "%USERPROFILE%\\windows-update-killer\\windows-updates-pause.reg"],capture_output=True, text=True, shell= True
                           )
            except subprocess.CalledProcessError as e:
                print(f"An error has occurred: {e}")
        case _:
            print("Not known option.")
            time.sleep(2)        

# [6] Tweaks Menu
def tweaks_menu():
    rich.print("Proceed with [#d60000]CAUTION[/#d60000]")
    time.sleep(1)
    rich.print("Be aware of every [#250052]option[/#250052] that you choose and the possible [#250052]outcome[/#250052].")
    time.sleep(2)
    rich.print("This application is not responsible for any possible [#250052]DAMAGE[/#250052] in your OS or Machine\n")
    O1 = ("[#5a03fc][1][/#5a03fc] Restore [#5a03fc]Old[/#5a03fc] Right Click Context Menu")
    O2 = ("[#fc03b6][2][/#fc03b6] Restore [#fc03b6]Modern[/#fc03b6] Right Click Context Menu")
    O3 = ("[#f54284][3] Disable[/#f54284] Windows Recall")
    O4 = ("[#2c0066][4] Enable[/#2c0066] Windows Recall")
    O5 = ("[#f54284][5] Disable[/#f54284] all Windows Background Apps")
    rich.print(O1.ljust(100) + O2)
    rich.print(O3.ljust(81) + O4)
    rich.print(O5)
    
    rich.print("\n[#fc0345][0] Exit to main menu[/#fc0345]")
    
    choice = input("\nChoose an option: ")
    match choice:
        case "0":
            clear_screen()
            main_menu()
        case "1":
            clear_screen()
            time.sleep(1)
            rich.print("[#0339fc]Restoring[/#0339fc] Old Right Click Menu")
            time.sleep(1.5)
            restore_oldright_menu()    
        case "2":
            clear_screen()
            time.sleep(1)
            rich.print("[#0339fc]Restoring[/#0339fc] Modern Right Click Menu")
            time.sleep(1.5)
            restore_modernright_menu()
        case "3":
            rich.print("[#f54284]Disabling[/#f54284] Windows Recall.")
            time.sleep(2)
            try:
                subprocess.run(["powershell", "-Command", "DISM /Online /Disable-Feature /FeatureName:Recall"],
                               check=True, shell=True
                               )
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr}\n{e.stdout}")    
            
        case "4":
            rich.print("[#2c0066]Re-enabling[/#2c0066] Windows Recall")
            time.sleep(2)        
            try:
                subprocess.run(["powershell", "-Command", "DISM /Online /Disable-Feature /FeatureName:Recall"],
                               check=True, shell=True
                               )
                time.sleep(2)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr}\n{e.stdout}")
                time.sleep(2)
                
        case "5":
            rich.print("[#f54284]Disabling[/#f54284] Windows Background Apps")
            time.sleep(2)
            try:
                command = 'REG ADD "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" /V GlobalUserDisabled /T REG_DWORD /D 1 /F'
                subprocess.run(command,
                               shell=True,check=True
                               )
                command = 'REG ADD "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search" /V BackgroundAppGlobalToggle /T REG_DWORD /D 0 /F'
                subprocess.run(command,
                               shell=True,check=True
                               )
                command = 'REG ADD "HKLM\\Software\\Policies\\Microsoft\\Windows\\AppPrivacy" /V LetAppsRunInBackground /T REG_DWORD /D 2 /F'
                subprocess.run(command,
                               shell=True,check=True
                               )
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr}\n{e.stdout}")
                time.sleep(2)    
                                    
                         
        case _:
            print("Not known option.")
            time.sleep(2)
                            
# [7] ISO Debloat Menu
def iso_menu():
    
    user_profile = os.environ.get('USERPROFILE')
    toolbox = os.path.join(user_profile, "rosalunna_toolbox")
    nilesh = toolbox = os.path.join(user_profile, "Windows-ISO-Debloater")
    
    # Tiny11
    tiny11 = os.path.join(user_profile, "tiny11builder")
    tiny11core = os.path.join(tiny11, "tiny11Coremaker.ps1")
    tiny11maker = os.path.join(tiny11, "tiny11maker.ps1")
    
    # Nilesh
    script = os.path.join(nilesh, "isoDebloaterScript.ps1")
    
    rich.print("This option is meant for [#d67200]ADVANCED[/#d67200] USERS")
    time.sleep(2)
    rich.print("\nProceed with [#d60000]EXTREME[/#d60000] Caution! And ensure you know what [#d60000]EVERY[/#d60000] option means.")
    time.sleep(2)
    rich.print("\nThis application is not responsible for any possible [#250052]DAMAGE[/#250052] in your OS or Computer.")
    time.sleep(1)
    
    rich.print("[1] Nilesh's ISO Debloat Script")
    rich.print("[2] Tiny11 Core ISO Maker")
    choice1 = input("Choose an option: ")
    
    match choice1:
        case "1":
            choice = input("Do you wish to proceed to Nilesh's ISO Debloat Script (Y/N)? ")
            match choice:
                
                case "N" | "n":
                    clear_screen()
                    main_menu()
            
                case "Y" | "y":
                    force_clean_directory(script)
                    git_clone("https://github.com/itsNileshHere/Windows-ISO-Debloater/")
                    try:
                        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script],shell=True, check=True)
                        print("ISO Debloat script executed successfully.")
                    except subprocess.CalledProcessError as e:
                        print(f"Error running the ISO Debloat script: {e}")
                case _:
                    print("Not Known Option")
                    time.sleep(3)
                    clear_screen()
                    iso_menu()
        case "2":
            force_clean_directory(tiny11)    
            git_clone("https://github.com/ntdevlabs/tiny11builder/")
            
            rich.print("[1] Tiny11 Core Maker (Smallest)")
            rich.print("[2] Tiny11 Maker")
            
            choice = input("Which option is more suited for you? ")
            match choice:
                case "1":
                    #Safe Check
                    a = input("Do you want to proceed to Tiny11 CoreMaker? ")
                    match a:
                        case "Y" | "y":
                            try:
                                subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", tiny11core],shell=True, check=True)
                
                            except subprocess.CalledProcessError as e:
                                print(f"Error running the Tiny11 CoreMaker script: {e}")
                                
                        case "N" | "n":
                            clear_screen()
                            main_menu()        
                            
                case "2":
                    #Safe Check
                    a = input("Do you want to proceed to Tiny11 CoreMaker? ")
                    match a:
                        case "Y" | "y":
                            try:
                                subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", tiny11maker],shell=True, check=True)
                
                            except subprocess.CalledProcessError as e:
                                print(f"Error running the Tiny11 Maker script: {e}")
                                
                        case "N" | "n":
                            clear_screen()
                            main_menu()       
                    
            
            
                        
    
    

        
    

                
                    
        
main_menu()