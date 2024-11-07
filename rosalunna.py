import os, subprocess, shutil, winreg, ctypes, sys, time
from os import system
from stat import *
from side_by_side import print_side_by_side
from colorama import Fore, Style
import wget
import requests
import tkinter as tk
from Utils.installations import *
from Utils.regedit import *
from Utils.servicesmsc import *

# Needed 
is_admin() #admin check
subprocess.run(["python.exe","-m","pip","install","--upgrade", "pip"], 
               shell=True, capture_output=True,text=True
               )

# Install Git on system
try:
    wingit = winget_install("Git.Git")
except subprocess.CalledProcessError as e:
    print(e.stderr, e.stdout)

# Install chocolatey if not
try:
    # Check if Chocolatey is installed
    choco = subprocess.run(["powershell", "-Command", "choco"], shell=True, capture_output=True, text=True)
    if choco.returncode != 0:
        print("Chocolatey is not installed. Installing Chocolatey...")
        winget_silent("Chocolatey.Chocolatey")
    else:
        print("Chocolatey is already installed.")
except subprocess.CalledProcessError as e:
    print("An error occurred while checking Chocolatey:", e.stderr, e.stdout)      
        
        
winget_silent("Chocolatey.Chocolatey")
scoop_setup() # Install Scoop Package Manager

# Display the main menu
def main_menu():
    clear_screen()
    print(Fore.MAGENTA)
    print("\nScript is running with Admin Privileges\n", "\n//------------------ ROSALUNNA DEBLOAT/INSTALL SCRIPT ------------------//\n")
    print(f"[1] EXTREMELY RECOMMENDED       [2] Browsers")
    print(f"[3] Applications                [4] Development")
    print(f"[5] Debloat")
    print(f"[0] Exit")
    choice = input(Fore.WHITE + "\nType option: ")

    while True:
        if choice == "1":
            clear_screen()
            tools_menu()
        elif choice == "2":
            clear_screen()
            browsers_menu()
        elif choice == "3":
            clear_screen()
            apps_menu()
        elif choice == "4":
            dev_menu()    
        elif choice == "5":
            clear_screen()
            debloat_menu()
        elif choice == "0":
            clear_screen()
            print("Exiting the script")
            sys.exit()                

#Tools Menu [1]
def tools_menu():
    clear_screen()
    print(Fore.LIGHTRED_EX)
    print("Extremely Recommended Installations on a Stripped Machine/custom ISO\n")
    print("[1] DirectX, Visual C++, .NET")
    print("[2] Java 8")
    print("[3] Windows Terminal")
    print("[4] Calculator, Paint3D, Camera, Photos, MultiMedia Player, Notepad, Voice Recorder")
    print(Fore.WHITE + "\n[0] Back to Main Menu")

    choice = input(Fore.WHITE + "\nChoose a tool: ")

    if choice == "0":
        clear_screen()
        main_menu()

    elif choice == "1":
        print("Installations are starting")
        winget_silent("Microsoft.DirectX")
        winget_silent("Microsoft.VCRedist.2013.x64")
        winget_silent("Microsoft.VCRedist.2013.x86")
        winget_silent("Microsoft.VCRedist.2012.x64")
        winget_silent("Microsoft.VCRedist.2012.x86")
        winget_silent("Microsoft.VCLibs.Desktop.14")
        winget_silent("Microsoft.VCRedist.2005.x64")
        winget_silent("Microsoft.VCRedist.2005.x86")
        winget_silent("Microsoft.VCRedist.2008.x64")
        winget_silent("Microsoft.VCRedist.2008.x86")
        winget_silent("Microsoft.VCRedist.2010.x64")
        winget_silent("Microsoft.VCRedist.2010.x86")
        winget_silent("Microsoft.VCRedist.2015+.x64")
        winget_silent("Microsoft.VCRedist.2015+.x86")
        winget_silent("Microsoft.DotNet.AspNetCore.3_1")
        winget_silent("Microsoft.DotNet.AspNetCore.6")
        winget_silent("Microsoft.DotNet.AspNetCore.7")
        winget_silent("Microsoft.DotNet.AspNetCore.8")
        winget_silent("Microsoft.DotNet.AspNetCore.Preview")
        winget_silent("Microsoft.DotNet.DesktopRuntime.3_1")
        winget_silent("Microsoft.DotNet.DesktopRuntime.6")
        winget_silent("Microsoft.DotNet.DesktopRuntime.7")
        winget_silent("Microsoft.DotNet.DesktopRuntime.8")
        winget_silent("Microsoft.DotNet.DesktopRuntime.Preview")
        winget_silent("Microsoft.DotNet.Runtime.3_1")
        winget_silent("Microsoft.DotNet.Runtime.6")
        winget_silent("Microsoft.DotNet.Runtime.7")
        winget_silent("Microsoft.DotNet.Runtime.8")
        winget_silent("Microsoft.DotNet.Runtime.Preview")


    elif choice == "2":
        winget_install("Oracle.JavaRuntimeEnvironment")
    elif choice == "3":
        winget_install("Microsoft.WindowsTerminal")
    elif choice == "4":
        winget_ms("9NBLGGH5FV99")#paint
        winget_ms("9WZDNCRFHVN5")#calc
        winget_ms("9WZDNCRFJBBG")#cam
        winget_ms("9WZDNCRFJBH4")#photos
        winget_ms("9WZDNCRFJ3PT")#media
        winget_ms("9MSMLRH6LZF3")#notepad
        winget_ms("9WZDNCRFHWKN")#voice recorder
    else:
        print("Invalid Choice")
            
        
# Browsers menu [2]
def browsers_menu():
    clear_screen()
    print(Fore.LIGHTBLACK_EX)
    print("Browsers Installation Options\n")
    print(Fore.BLUE + "[1] Chromium Based")
    print(Fore.LIGHTYELLOW_EX + "[2] Firefox Forks/Engine")
    print(Fore.WHITE + "[0] Back to Main Menu")
    choice = input(Fore.WHITE + "\nChoose a browser to install: ")
    if choice == "0":
        clear_screen()
        main_menu()

    elif choice == "1":
        clear_screen()
        chromium_menu()
    elif choice == "2":
        clear_screen
        firefox_menu()

# [3] Applications                
def apps_menu():
    width = 50
    gaming = [
    Fore.LIGHTMAGENTA_EX + "\n|------------------------ GAMING ------------------------|",
    " [1] Steam                        [2] Epic Games",
    " [3] GOG Galaxy                   [4] Itch.io",
    " [5] Bethesda Launcher            [6] Battle.net",
    " [7] EA App                       [8] Origin",
    " [9] Ubisoft Connect              [10] Geforce NOW",
    " [11] Rockstar Games Launcher     [12] Playnite\n"
 ]
    peripherals = ["\n|----------------------- PERIPHEALS -----------------------|",
    " [13] Razer Synapse 3                  [14] Razer Synapse 4",
    " [15] Steelseries GG                   [16] Logitech GHUB",
    " [17] Corsair ICUE3                    [18] Corsair ICUE4",
    " [19] Corsair ICUE5                    [20] HyperX NGENUITY"
 ]
    emulators = [Fore.BLUE + "\n|----------------------------- EMULATORS -----------------------------|",
    " [21] Ryujinx (SWITCH)                    [22] Dolphin (GAMECUBE/WII)",
    " [23] Duckstation (PS1)                   [24] PCSX2 (PS2)",
    " [25] RPCS3 (PS3)                         [26] PPSSPP (PSP)",
    " [27] SNES9X (SNES)                       [28] CEMU (WIIU)",
    " [29] MELONDS (NDS)                       [30] LIME3DS (3DS)",
    " [31] XEMU (XBOX)                         [32] XENIA (XBOX360)",
    " [33] FLYCAST (DREAMCAST)",
    "\n\n|------------------------------- UTILITIES -------------------------------|"
    "\n- UNINSTALLING AND PERFORMANCE TESTING -",
    " [53] Display Driver Uninstaller   [54] REVO Uninstaller",
    " [55] IOBIT Uninstaller            [56] CCleaner",
    " [57] BleachBit",
    "\n- (DE)COMPRESSION/FILE-MANAGER -",
    " [58] 7zip                         [59] NanaZip",
    " [60] PeaZip                       [61] WinRAR\n",
    "- DISK MANAGING -",
    " [62] Macrium Reflect              [63] Minitool Partition Wizard",
    " [64] Defraggler\n",
    "- OS INSTALL -",
    " [65] Ventoy                       [66] Rufus",
    "- VIRTUALIZATION -",
    " [67] VMWare Workstation Player    [68] Oracle VirtualBox",
    " ",
    "- OTHER -",
    " [69] Dual Monitor Tools           [70] IOBIT Unlocker",
    " [71] Notepad++\n"
 ]
    hardware = ["\n|--------------------------------- HARDWARE ---------------------------------|",
    "- HARDWARE MONITORING AND INFORMATION -          ",
    " [34] CPU-Z                                 [35] GPU-Z",
    " [36] Speccy                                [37] HWMonitor",
    " [38] HWInfo                                [39] Core Temp",
    " [40] AIDA64                                [41] Intel Processor ID Utility",
    "\n- OVERCLOCKING AND TUNING -",
    " [42] MSI Afterburner                       [43] Intel Extreme Tuning Utility",
    " [44] NVIDIA Inspector                      [45] AMD Ryzen Master",
    " [46] OCCT (Overclocking Stress Utility)    [47] QuickCPU",
    " [48] Process Lasso                                        ",
    "\n- BENCHMARKING AND PERFORMANCE TESTING -",
    " [49] 3DMark                                [50] Cinebench",
    " [51] UNIGINE Heaven                        [52] UNIGINE Superposition",
 ]

    left_gaming = [item.ljust(width) for item in gaming]
    right_peripheals = [item.rjust(width) for item in peripherals]
    left_emulators = [item.ljust(width) for item in emulators]
    right_hardware = [item.rjust(width) for item in hardware]
    #normal utilities
    print_side_by_side("\n".join(left_gaming),"\n".join(right_peripheals))
    print_side_by_side("\n".join(left_emulators),"\n".join(right_hardware))
    print(Fore.WHITE + " [0] Back to main menu\n")
    choice = input(Fore.WHITE + " Choose an application: ")
    if choice == "0":
        clear_screen()
        main_menu()
    elif choice == "1":
        choco_install("steam")
    elif choice == "2":
        choco_install("epicgameslauncher")
    elif choice == "3":
        choco_install("goggalaxy")
    elif choice == "4":
        choco_install("itch")
    elif choice == "5":
        winget_install("Bethesda.Launcher")
    elif choice == "6":
        scoop_install("games/battlenet")
    elif choice == "7":
        choco_install("ea-app")
    elif choice == "8":
        choco_install("origin")
    elif choice == "9":
        choco_install("ubisoft-connect")
    elif choice == "10":
        choco_install("nvidia-geforce-now")
    elif choice == "11":
        choco_install("rockstar-launcher")
    elif choice == "12":
        choco_install("playnite")
    elif choice == "13":
        winget_install("RazerInc.RazerInstaller")
    elif choice == "14":
        url = "https://rzr.to/synapse-4-pc-download"
        filename = "Razer Synapse 4.exe"
        download_file(url,filename) 
    elif choice == "15":
        choco_install("steelseries-engine") 
    elif choice == "16":
        winget_install("Logitech.GHUB")
    elif choice == "17":
        winget_install("Corsair.iCUE.3")
    elif choice == "18":
        winget_install("Corsair.iCUE.4")
    elif choice == "19":
        winget_install("Corsair.iCUE.5")
    elif choice == "20":
        winget_install("9P1TBXR6QDCX")
    elif choice == "21":
        choco_install("ryujinx")
    elif choice == "22":
        choco_install("dolphin")
    elif choice == "23":
        scoop_install("games/duckstation")    
    elif choice == "24":
        winget_install("PCSX2Team.PCSX2")
    elif choice == "25":
        scoop_install("games/rpcs3")
    elif choice == "26":
        scoop_install("games/ppsspp")    
    elif choice == "27":
        choco_install("snes9x")
    elif choice == "28":
        choco_install("cemu")
    elif choice == "29":
        scoop_install("games/melonds")
    elif choice == "30":
        scoop_install("games/lime3ds")
    elif choice == "31":
        scoop_install("games/xemu")
    elif choice == "32":
        scoop_install("games/xenia")
    elif choice == "33":
        scoop_install("games/flycast")
    elif choice == "34":
        scoop_install("extras/cpuz")
    elif choice == "35":
        scoop_install("extras/gpuz")
    elif choice == "36":
        scoop_install("extras/speccy")
    elif choice == "37":
        scoop_bucket_add("extras")
        scoop_install("extras/hwmonitor")
    elif choice == "38":
        scoop_install("extras/hwinfo")
    elif choice == "39":
        scoop_install("extras/coretemp")
    elif choice == "40":
        scoop_install("extras/aida64extreme")
    elif choice == "41":
        choco_install("intel-processor-identification-utility")
    elif choice == "42":
        winget_install("Guru3D.Afterburner")
    elif choice == "43":
        choco_install("intel-xtu")
    elif choice == "44":
        scoop_install("extras/nvidia-profile-inspector")
    elif choice == "45":
        choco_install("amd-ryzen-master")
    elif choice == "46":
        winget_install("OCBase.OCCT.Personal")
    elif choice == "47":
        scoop_bucket_add("extras")
        scoop_install("extras/quickcpu")
    elif choice == "48":
        choco_install("plasso")
    elif choice == "49":
        choco_install("3dmark")
    elif choice == "50":
        winget_install("Maxon.CinebenchR23")
    elif choice == "51":
        choco_install("heaven-benchmark")
    elif choice == "52":
        choco_install("superposition-benchmark")
    elif choice == "53":
        choco_install("ddu")
    elif choice == "54":
        scoop_install("extras/revouninstaller")
    elif choice == "55":
        winget_install("IObit.Uninstaller")
    elif choice == "56":
        winget_install("Piriform.CCleaner")
    elif choice == "57":
        winget_install("BleachBit.BleachBit")
    elif choice == "58":
        choco_install("7zip")
    elif choice == "59":
        choco_install("nanazip")
    elif choice == "60":
        choco_install("peazip")
    elif choice == "61":
        winget_install("RARLab.WinRAR")
    elif choice == "62":
        choco_install("reflect-free")
    elif choice == "63":
        choco_install("partitionwizard")
    elif choice == "64":
        scoop_install("extras/defraggler")
    elif choice == "65":
        winget_install("ventoy.Ventoy")
    elif choice == "66":
        winget_install("Rufus.Rufus")
    elif choice == "67":
        scoop_install("nonportable/vmware-workstation-player-np")
    elif choice == "68":
        choco_install("virtualbox")
    elif choice == "69":
        choco_install("dual-monitor-tools")
    elif choice == "70":
        choco_install("io-unlocker")
    elif choice == "71":
        choco_install("notepadplusplus")    
    
    else:
        print("Unknown option.")
        clear_screen()
        main_menu()         

#Debloat Menu [4]
def debloat_menu():
    clear_screen()
    print(Fore.RED)
    print("DEBLOAT MENU for " + Fore.YELLOW + "ADVANCED " + Fore.RED + "users\nProceed with " + Fore.YELLOW + "CAUTION!\n" + Fore.RED)
    print_side_by_side("[1] Automated Debloat removing Defender", "[2] Automated Debloat keeping Defender")
    print_side_by_side("[3] Pause Windows Updates until 2051","[4] Re-enable Windows Updates")
    print("[5] Automated debloat, disabling defender and updates")
    print("\nINFO:The debloat options" + Fore.YELLOW + " WILL " + Fore.RED + "remove MS-EDGE, you may reinstall using the Applications Menu if needed.")
    print(Fore.WHITE + "\n[0] Back to main menu")
    

    choice = input(Fore.WHITE + "\nChoose an option: ")
    if choice == "0":
        clear_screen()
        main_menu()
    
    elif choice == "1": # Automated -Defender
        # Regedit and Services Tweaks
        regedit()
        remove_services()

        # Remove Defender and Edge
        ms_edgeR()
        defender_total_removal()

        # Raphire script install, change txt and execute
        raphire_install_txt_change()
        raphire_execute_modscript()

        # RAM Tweaks
        choco_install("rammap") #Install
        ram_map() #First Execution
        schedule_rammap() #Schedule for 30min-30min

        #OO SHUTUP
        download_file("https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe", "OOSU10.exe")


    elif choice == "2": #Automated Keeping Defender
        # Regedit and Services Tweaks
        regedit()
        remove_services()

        ms_edgeR()

        # Raphire script install, change txt and execute
        raphire_install_txt_change()
        raphire_execute_modscript()

        # RAM Tweaks
        choco_install("rammap") #Install
        ram_map() #First Execution
        schedule_rammap() #Schedule for 30min-30min

        #OO SHUTUP
        download_file("https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe", "OOSU10.exe")

    elif choice == "3": # Disable UPDATE
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
    
    elif choice == "4": # RE-ENABLE UPDATES
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

    elif choice == "5": # Automated remove -def -UP

        # Regedit, services tweaks
        regedit()
        remove_services()

        # Raphire script install, change txt and execute
        raphire_install_txt_change()
        raphire_execute_modscript()

        # Defender and Edge Removal
        ms_edgeR()
        defender_total_removal()
        
        # OO SHUTUP
        download_file("https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe", "OOSU10.exe")

        # RAM Tweaks
        choco_install("rammap") #Install
        ram_map() #First Execution
        schedule_rammap() #Schedule for 30min-30min

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
            
def dev_menu():
    devmenuL = [Fore.CYAN + " |------------ CODE EDITORS/IDEs ------------| ",
               " [1] Visual Studio Code      [2] IntelliJ IDEA",
               " [3] PyCharm                 [4] Eclipse",
               " [5] NetBeans                [6] Atom",
               " [7] Sublime Text            [8] VIM",
               " [9] BlueJ                   [10] Emacs",
               " [11] Arduino IDE            [12] Code::Blocks",
               " [13] Jupyter Notebook       [14] Spyder",
               " [15] Geany", " ",
               "|---------------- BUILD TOOLS ----------------|",
               " [16] Maven                   [17] Gradle",
               " [18] Ant                     [19] CMake",
               " [20] Make                    [21] Bazel",
               " [22] MSBuild                 [23] Jenkins",
               " [24] GitLab Runner           [25] CircleCI CLI",
               " [26] Vagrant"
               ]
    
    devmenuR = ["|-------------- DATABASE MANAGEMENT --------------|",
                " [27] DBeaver                [28] TablePlus",
                " [29] Robo 3T                [30] Redis DE",
                " ",
                "|---------------- WEB-DEV ----------------|",
                " [31] XAMPP                  [32] MAMP",
                " [33] Postman                [34] Insomnia",
                " [35] Apache JMeter", " ",
                "|-------------- LANGUAGES-ETC --------------|",
                " [36] Anaconda               [37] Python",
                " [38] Java 8                 [39] Rust",
                " [40] Pulsar                 [41] Yarn",
                " [42] Go                     [43] Pixi",
                " [44] NodeJS                 [45] Helix",
                " [46] Godot                  [47] Neovim",
                Fore.WHITE
                ]
    clear_screen()
    print_side_by_side("\n".join(devmenuL),"\n".join(devmenuR))
    print("\n [0] Back to main menu ")
    choice = input("\n Choose an option: ")

    if choice == "0":
        clear_screen()
        main_menu()
    elif choice == "1":
        scoop_install("extras/vscode")
    elif choice == "2":
        choco_install("intellijidea-community")
    elif choice == "3":
        choco_install("pycharm")
    elif choice == "4":
        choco_install("eclipse")
    elif choice == "5":
        choco_install("netbeans")
    elif choice == "6":
        choco_install("atom")
    elif choice == "7":
        scoop_install("extras/sublime-text")
    elif choice == "8":
        scoop_install("main/vim")
    elif choice == "9":
        choco_install("bluej")
    elif choice == "10":
        choco_install("emacs")
    elif choice == "11":
        scoop_install("extras/arduino")
    elif choice == "12":
        choco_install("codeblocks")
    elif choice == "13":
        winget_install("ProjectJupyter.JupyterLab")
    elif choice == "14":
        scoop_install("extras/spyder")
    elif choice == "15":
        choco_install("geany")
    elif choice == "16":
        choco_install("maven")
    elif choice == "17":
        choco_install("gradle")
    elif choice == "18":
        choco_install("ant")
    elif choice == "19":
        choco_install("cmake")
    elif choice == "20":
        choco_install("make")
    elif choice == "21":
        choco_install("bazel")
    elif choice == "22":
        scoop_install("extras/msbuild-structured-log-viewer")
    elif choice == "23":
        choco_install("jenkins")
    elif choice == "24":
        choco_install("gitlab-runner")
    elif choice == "25":
        choco_install("circleci-cli")
    elif choice == "26":
        choco_install("vagrant")
    elif choice == "27":
        choco_install("dbeaver")
    elif choice == "28":
        scoop_install("extras/tableplus")
    elif choice == "29":
        choco_install("robo3t.install")
    elif choice == "30":
        choco_install("redis")
    elif choice == "31":
        scoop_install("extras/xampp")
    elif choice == "32":
        choco_install("mamp")
    elif choice == "33":
        scoop_install("extras/postman")
    elif choice == "34":
        scoop_install("extras/insomnia")
    elif choice == "35":
        choco_install("jmeter")
    elif choice == "36":
        choco_install("anaconda3")
        choco_install("anaconda2")
    elif choice == "37":
        scoop_install("main/python")
    elif choice == "38":
        winget_install("Oracle.JavaRuntimeEnvironment")
    elif choice == "39":
        scoop_install("main/rust")
    elif choice == "40":
        scoop_install("extras/pulsar")
    elif choice == "41":
        scoop_install("main/yarn")
    elif choice == "42":
        winget_install("GoLang.Go.1.18")
    elif choice == "43":
        winget_install("prefix-dev.pixi")
    elif choice == "44":
        winget_install("OpenJS.NodeJS") 
    elif choice == "45":
        scoop_install("main/helix")
    elif choice == "46":
        choco_install("godot")
    elif choice == "47":
        choco_install("neovim")    
    else:
        print("Unknown option. Try again: ")
        dev_menu()                                                                  
    
#Chromium menu
def chromium_menu():
    clear_screen()
    print(Fore.BLUE + "[1] Google Chrome")
    print("[2] Brave")
    print("[3] Vivaldi")
    print("[4] Chromium")
    print("[5] Ungoogled Chromium")
    print("[6] Microsoft Edge")
    print("[7] Opera")
    print("[8] Opera GX")
    print("[9] Arc")
    print("[10] Yandex")
    print(Fore.WHITE + "\n[0] Browser subtype menu")
    choice = input("\nChoose an option: ")  

    if choice == "0":
        clear_screen
        browsers_menu()
    elif choice == "1":
        winget_install("Google.Chrome")
    elif choice == "2":
        winget_install("Brave.Brave")
    elif choice == "3":
        winget_install("Vivaldi.Vivaldi")
    elif choice == "4":
        winget_install("Hibbiki.Chromium")
    elif choice == "5":
        scoop_install("extras/ungoogled-chromium")
    elif choice == "6":
        winget_install("Microsoft.Edge")
    elif choice == "7":
        winget_install("Opera.Opera")
    elif choice == "8":
        winget_install("Opera.OperaGX")
    elif choice == "9":
        winget_install("TheBrowserCompany.Arc")
    elif choice == "10":
        winget_install("Yandex.Browser")
    else:
        print("Invalid option. Returning to Browsers Menu.")
        input("Press Enter to continue...")

#Firefox menu
def firefox_menu():
    clear_screen()
    print(Fore.LIGHTYELLOW_EX + "[1] Mozilla Firefox")
    print("[2] Floorp")
    print("[3] Zen")
    print("[4] LibreWolf")
    print("[5] WaterFox")
    print("[6] Mullvad")
    print("[7] TOR")
    print("[8] Pale Moon")
    print(Fore.WHITE + "\n[0] Browser subtype menu")
    choice = input("\nChoose a browser to install: ")
    
    if choice == "0":
        clear_screen()
        browsers_menu()  
    elif choice == "1":
        winget_install("Mozilla.Firefox")
    elif choice == "2":
        winget_install("Ablaze.Floorp")
    elif choice == "3":
        winget_install("Zen-Team.Zen-Browser")
    elif choice == "4":
        winget_install("LibreWolf.LibreWolf")
    elif choice == "5":
        winget_install("WaterFox.WaterFox")
    elif choice == "6":
        winget_install("MullvadVPN.MullvadBrowser")
    elif choice == "7":
        winget_install("TorProject.TorBrowser")    
    elif choice == "8":
        winget_install("MoonchildProductions.PaleMoon")    
    else:
        print("Invalid option. Returning to Browsers Menu.")
        input("Press Enter to continue...")

os.system("mode con: cols=190 lines=66")

main_menu()