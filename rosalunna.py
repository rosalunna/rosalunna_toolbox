import os, subprocess, shutil, winreg, sys, requests, stat, time, ctypes, zipfile
import time
from colorama import Fore, Style
import rich
from Utils.installations import *
from Utils.regedit_services import *
from side_by_side import print_side_by_side
from urllib.request import urlretrieve

# Setups
git_setup()
scoop_setup()
choco_setup()

# Set Column Width for some menus
column_width = 80

# Main menu & loop
def main_menu():

    O1 = "[#78fab2][1] Extremely Recommended[/#78fab2]"
    O2 = "[#5F6E81][2][/#5F6E81] [#0073ff]Brow[/#0073ff][#bd6902]sers[/#bd6902]"
    O3 = "[#7d0137][3] Applications[/#7d0137]"
    O4 = "[#00f4ff][4] Development[/#00f4ff]"
    O5 = "[#fc0345][5] Debloat[/#fc0345]"
    O6 = "[#fc0345][6] Nilesh's ISO Debloat Script[/#fc0345]"
    
         
    clear_screen()
    rich.print("[#7d0137]SCRIPT MUST BE RAN AS[/#7d0137]","[#bf6000]ADMINISTRATOR,[/#bf6000]","[#7d0137]RESTART IF NEEDED[/#7d0137]")
    rich.print("[#7d0137]VERSION:[/#7d0137] [#eb05b5]1.0.0[/#eb05b5]\n")
    rich.print("[#7d0137]|-------------------------------------ROSALUNNA TOOLBOX-------------------------------------|[/#7d0137]\n")
    rich.print(O1.ljust(column_width) + O2)
    rich.print(O3.ljust(column_width) + O4)
    rich.print(O5.ljust(column_width) + O6)
    print(Fore.RED + "\n[0] Exit the application" + Fore.RESET)
    choice = input("\nChoose an option: ")

    while True:
        if choice == "0":
            clear_screen()
            sys.exit()

        elif choice == "1":
            clear_screen()
            rec_menu()

        elif choice == "2":
            clear_screen()
            browsers_menu()

        elif choice == "3":
            clear_screen()
            apps_menu()

        elif choice == "4":
            clear_screen()
            dev_menu()

        elif choice == "5":
            clear_screen()
            debloat_menu()
            
        elif choice == "6":
            clear_screen()
            iso_menu()    

        else:
            print("\nNot known option.")
            time.sleep(1.5)
            main_menu()
                                
# [1] Recommended Installations Menu
def rec_menu():
    clear_screen()
    rich.print("[#ff0066]Extremely Recommended[/#ff0066] Installations on a Stripped Machine/custom ISO\n")
    print(Fore.GREEN+"[1] DirectX, Visual C++, .net, Java 8")
    print("[2] Terminal, Calculator, Paint3D, Camera, Multimedia player, photos, Notepad, Sound Recorder"+Fore.RESET)

    print("\n[0] Back to Main Menu")
    choice = input("\nChoose a tool: ")

    if choice == "0":
        clear_screen()
        main_menu()

    elif choice == "1":
        clear_screen()
        time.sleep(1)
        print("Installations are starting")
        time.sleep(1)
        # DirectX
        winget_silent("Microsoft.DirectX")
        # Visual C++
        winget_silent("Microsoft.VCRedist.2005.x64")
        winget_silent("Microsoft.VCRedist.2005.x86")
        winget_silent("Microsoft.VCRedist.2008.x64")
        winget_silent("Microsoft.VCRedist.2008.x86")
        winget_silent("Microsoft.VCRedist.2010.x64")
        winget_silent("Microsoft.VCRedist.2010.x86")
        winget_silent("Microsoft.VCRedist.2012.x64")
        winget_silent("Microsoft.VCRedist.2012.x86")
        winget_silent("Microsoft.VCRedist.2013.x64")
        winget_silent("Microsoft.VCRedist.2013.x86")
        winget_silent("Microsoft.VCRedist.2015+.x64")
        winget_silent("Microsoft.VCRedist.2015+.x86")
        # Asp Net Core
        winget_silent("Microsoft.DotNet.AspNetCore.3_1")
        winget_silent("Microsoft.DotNet.AspNetCore.6")
        winget_silent("Microsoft.DotNet.AspNetCore.7")
        winget_silent("Microsoft.DotNet.AspNetCore.8")
        winget_silent("Microsoft.DotNet.AspNetCore.9")
        winget_silent("Microsoft.DotNet.AspNetCore.Preview")
        # .net windows desktop runtime
        winget_silent("Microsoft.DotNet.DesktopRuntime.3_1")
        winget_silent("Microsoft.DotNet.DesktopRuntime.6")
        winget_silent("Microsoft.DotNet.DesktopRuntime.7")
        winget_silent("Microsoft.DotNet.DesktopRuntime.8")
        winget_silent("Microsoft.DotNet.DesktopRuntime.9")
        # .net runtime
        winget_silent("Microsoft.DotNet.Runtime.3_1")
        winget_silent("Microsoft.DotNet.Runtime.6")
        winget_silent("Microsoft.DotNet.Runtime.7")
        winget_silent("Microsoft.DotNet.Runtime.8")
        # Java 8
        winget_silent("Oracle.JavaRuntimeEnvironment")

    elif choice == "2":
        clear_screen()
        time.sleep(1)
        print("Installations are starting")
        time.sleep(1)
        winget_ms("9N0DX20HK701") #terminal
        winget_ms("9WZDNCRFJ3PT") #media
        winget_ms("9WZDNCRFHVN5") #calc
        winget_ms("9PCFS5B6T72H") #paint
        winget_ms("9WZDNCRFJBBG") #cam
        winget_ms("9WZDNCRFJBH4") #photos
        winget_ms("9MSMLRH6LZF3") #notepad
        winget_ms("9WZDNCRFHWKN") #sound        

# [2] Browsers menu
def browsers_menu():
    clear_screen()
    O1 = "[#0073ff][1] Chromium-Based[/#0073ff]"
    O2 = "[#bd6902][2] Firefox Based[/#bd6902]"
    rich.print(O1.ljust(60) + O2)
    print("\n[0] Back to main menu")

    choice = input("\nChoose a browser subtype: ")

    if choice == "0":
        clear_screen()
        main_menu()

    elif choice == "1":
        clear_screen()
        chromium_menu()

    elif choice == "2":
        clear_screen()
        firefox_menu()

# Browsers subtype
def chromium_menu():
    clear_screen()
    O1 = "[#a1002e][1] Vivaldi[/#a1002e]"
    O2 = "[#E9500C][2] Brave[/#E9500C]"
    O3 = "[#010380][3] Chromium[/#010380]"
    O4 = "[#b84d00][4] Google Chrome[/#b84d00]"
    O5 = "[#0090b8][5] Ungoogled Chromium [/#0090b8]"
    O6 = "[#2d71b8][6] Microsoft Edge[/#2d71b8]"
    O7 = "[#a3020c][7] Opera[/#a3020c]"
    O8 = "[#a3020c][8] Opera GX[/#a3020c]"
    O9 = "[#fa4929][9] Yandex[/#fa4929]"
    O10 = "[#fa4460][10] Arc[/#fa4460]"
    rich.print(O1.ljust(column_width) + O2)
    rich.print(O3.ljust(column_width) + O4)
    rich.print(O5.ljust(column_width) + O6)
    rich.print(O7.ljust(column_width) + O8)
    rich.print(O9.ljust(column_width) + O10)
    

    print("\n[0] Browsers Subtype Menu\n")
    choice = input("Choose a chromium based option: ")

    if choice == "0":
        clear_screen()
        browsers_menu()
    elif choice == "1":
        winget_install("Vivaldi.Vivaldi")
    elif choice == "2":
        winget_install("Brave.Brave")
    elif choice == "3":
        winget_install("Hibbiki.Chromium")
    elif choice == "4":
        winget_install("Google.Chrome")
    elif choice == "5":
        winget_install("eloston.ungoogled-chromium")
    elif choice == "6":
        winget_install("Microsoft.Edge")
    elif choice == "7":
        winget_install("Opera.Opera")
    elif choice == "8":
        winget_install("Opera.OperaGX")
    elif choice == "9":
        winget_install("Yandex.Browser")
    elif choice == "10":
        winget_install("TheBrowserCompany.Arc")

def firefox_menu():
    O1 = "[#FF3D40][1] Mozilla Firefox[/#FF3D40]"
    O2 = "[#5A08E8][2] Floorp[/#5A08E8]"
    O3 = "[#00ACFF][3] Librewolf[/#00ACFF]"
    O4 = "[#00ACFF][4] Waterfox[/#00ACFF]"
    O5 = "[#FEF9FE][5] Zen[/#FEF9FE]"
    O6 = "[#E6A216][6] Mullvad[/#E6A216]"
    O7 = "[#9C3EEB][7] TOR[/#9C3EEB]"
    O8 = "[#1B3563][8] Pale Moon[/#1B3563]"
    
    rich.print(O1.ljust(column_width) + O2)
    rich.print(O3.ljust(column_width) + O4)
    rich.print(O5.ljust(column_width) + O6)
    rich.print(O7.ljust(column_width) + O8)
    
    print("\n[0] Browsers Subtype Menu")
    choice = input("\nChoose a FireFox based option: ")

    if choice == "0":
        clear_screen()
        browsers_menu()
    elif choice == "1":
        winget_install("Mozilla.Firefox")
    elif choice == "2":
        winget_install("Ablaze.Floorp")
    elif choice == "3":
        winget_install("LibreWolf.LibreWolf")
    elif choice == "4":
        winget_install("Waterfox.Waterfox")
    elif choice == "5":
        winget_install("Zen-Team.Zen-Browser")
    elif choice == "6":
        winget_install("MullvadVPN.MullvadBrowser")
    elif choice == "7":
        winget_install("TorProject.TorBrowser")
    elif choice == "8":
        winget_install("MoonchildProductions.PaleMoon")                    

# [3]Apps Menu
def apps_menu():
    GAMING = [Fore.LIGHTMAGENTA_EX + "|-------------------------GAMING-------------------------|",
              " [1] Steam                          [2] Epic Games",
              " [3] GOG Galaxy                     [4] Battle.net",
              " [5] Rockstar Games Launcher        [6] EA App",
              " [7] Origin                         [8] Ubisoft Connect",
              " [9] Itch.io                        [10] Bethesda Launcher",
              " [11] Playnite                      [12] Geforce NOW"+Fore.LIGHTRED_EX      
    ]
    COMMON = ["     |--------COMMON APPLICATIONS--------|",
              " [13] Discord          [14] Spotify", 
              " [15] WhatsApp         [16] Telegram\n",
              "|----------ARCHIVE MANAGERS----------|",
              " [17] 7Zip             [18] NanaZip",
              " [19] WinRar           [20] WinZip"    
    ]
    HARDWAREMON = ["\n|------------------------------------------------------------HARDWARE------------------------------------------------------------|",
               " /HARDWARE MONITORING AND INFO/",
               " [21] CPU-Z               [22] GPU-Z",
               " [23] Speccy              [24] HWMonitor",
               " [25] HWInfo              [26] AIDA64",
    ]
    OVERCLOCKBENCH = ["",
                " /OVERCLOCKING AND BENCHMARKING",
                " [27] MSI Afterburner    [28] Intel Extreme Tuning Utility",
                " [29] AMD Ryzen Master   [30] OCCT",
                " [31] QuickCPU           [32] NVIDIA Inspector",
                " [33] Process Lasso      [34] CineBench",
                " [35] 3DMark"             
    ]
    UTILITIES = [Fore.CYAN+"\n|----------------------------UTILITIES----------------------------|",
                " [36] Ventoy                      [37] Rufus",
                " [38] VMware Workstation Player   [39] Oracle VirtualBox",
                " [40] Macrium Reflect             [41] Minitool Partition Wizard",
                " [42] Display Driver Uninstaller  [43] Revo Uninstaller" + Fore.RESET
                 
    ]
    
    
    
    max_length = max(len(GAMING), len(COMMON))
    GAMING.extend([""] * (max_length - len(GAMING)))
    COMMON.extend([""] * (max_length - len(COMMON)))
    
    max_length = max(len(HARDWAREMON), len(OVERCLOCKBENCH))
    HARDWAREMON.extend([""] * (max_length - len(HARDWAREMON)))
    OVERCLOCKBENCH.extend([""] * (max_length - len(OVERCLOCKBENCH)))

# Print side-by-side
    for left, right in zip(GAMING, COMMON):
        print(f"{left.ljust(70)} {right}")
    for left, right in zip(HARDWAREMON, OVERCLOCKBENCH):
        print(f"{left.ljust(70)} {right}")
    print("\n".join(UTILITIES))    
    rich.print("\n [0] Back to main menu")        
              
    applications = {
        "1": ("Valve.Steam", "winget_install"),
        "2": ("EpicGames.EpicGamesLauncher", "winget_install"),
        "3": ("GOG.Galaxy", "winget_install"),
        "4": ("Blizzard.BattleNet", "winget_install"),
        "5": ("rockstar-launcher", "choco_install"),
        "6": ("ElectronicArts.EADesktop", "winget_install"),
        "7": ("ElectronicArts.Origin", "winget_install"),
        "8": ("Ubisoft.Connect", "winget_install"),
        "9": ("ItchIo.Itch", "winget_install"),
        "10": ("Bethesda.Launcher", "winget_install"),
        "11": ("Playnite.Playnite", "winget_install"),
        "12": ("Nvidia.GeForceNow", "winget_install"),
        "13": ("Discord.Discord", "winget_install"),
        "14": ("Spotify.Spotify", "winget_install"),
        "15": ("9NKSQGP7F2NH", "winget_ms"),  # WhatsApp
        "16": ("telegram", "choco_install"),
        "17": ("7zip.7zip", "winget_install"),
        "18": ("M2Team.NanaZip", "winget_install"),
        "19": ("RARLab.WinRAR", "winget_install"),
        "20": ("Corel.WinZip", "winget_install"),
        "21": ("CPUID.CPU-Z", "winget_install"),
        "22": ("gpu-z", "choco_install"),
        "23": ("Piriform.Speccy", "winget_install"),
        "24": ("CPUID.HWMonitor", "winget_install"),
        "25": ("hwinfo", "choco_install"),
        "26": ("FinalWire.AIDA64.Extreme", "winget_install"),
        "27": ("Guru3D.Afterburner", "winget_install"),
        "28": ("intel-xtu", "choco_install"),
        "29": ("amd-ryzen-master", "choco_install"),
        "30": ("OCBase.OCCT.Personal", "winget_install"),
        "31": ("CoderBag.QuickCPUx64", "winget_install"),
        "32": ("nvidia-profile-inspector", "choco_install"),
        "32": ("nvidia-profile-inspector", "choco_install"),
   
    }    

    choice = input("\nChoose an application: ")
    if choice == "0":
        clear_screen()
        main_menu()
    else:
        # Fetch the command and function name from the dictionary
        app_info = applications.get(choice)
        if app_info:
            app_name, install_function = app_info
            # Dynamically call the appropriate function
            globals()[install_function](app_name)
        else:
            print("Invalid choice. Please try again.")    

# [4] Development Menu
def dev_menu():
    rich.print("Welcome to the [#00f4ff]Development[/#00f4ff] Menu\n")
    
    LANG = [Fore.CYAN + "|--------------------LANGUAGES--------------------|",
            " [1] Python         [2] Java",
            " [3] Ruby           [4] Kotlin",
            " [5] Go             [6] TypeScript",
            " [7] Rust           [8] PHP",
            " [9] Lua           [10] Ada" + Fore.RESET
            ]
    EDITORIDE = ["    |------------CODE EDITORS/IDEs------------|",
                 " [11] VS Code           [12] VS Codium",
                 " [13] IntelliJ IDEA     [14] PyCharm",
                 " [15] Arduino IDE       [16] Eclipse",
                 " [17] Jupyter Notebook  [18] Code::Blocks"       
    ]
    
    max_length = max(len(LANG), len(EDITORIDE))
    LANG.extend([""] * (max_length - len(LANG)))
    EDITORIDE.extend([""] * (max_length - len(EDITORIDE)))
    
    for left, right in zip(LANG, EDITORIDE):
        print(f"{left.ljust(70)} {right}")
    print("\n [0] Back to main menu")    
    
    development = {
        "1": ("Python.Python.3.13", "winget_install"),
        "2": (["Oracle.JavaRuntimeEnvironment", "Oracle.JDK.23"], "winget_install_multiple"),
        "3": ("RubyInstallerTeam.Ruby.3.2", "winget_install"),
        "4": ("ojdkbuild.openjdk.14.jdk", "winget_install"),
        "5": ("GoLang.Go", "winget_install"),
        "6": ("Nodejs.LTS", "winget_install"),
        "7": ("Rust.Rust", "winget_install"),
        "8": ("PHP.PHP", "winget_install"),
        "9": ("Lua.Lua", "winget_install"),
        "10": ("AdaCore.GNAT", "winget_install"),
        "11": ("Microsoft.VisualStudioCode", "winget_install"),
        "12": ("VSCodium.VSCodium", "winget_install"),
        "13": ("JetBrains.IntelliJIDEA.Community", "winget_install"),
        "14": ("JetBrains.PyCharm.Community", "winget_install"),
        "15": ("ArduinoSA.IDE.stable", "winget_install"),
        "16": (["EclipseAdoptium.Temurin.23.JDK", "EclipseAdoptium.Temurin.23.JRE"], "winget_install_multiple"),
        "17": ("ProjectJupyter.JupyterLab", "winget_install"),
        "18": ("Codeblocks.Codeblocks", "winget_install"),        
    }
    
    choice = input("\nChoose an development option: ")
    if choice == "0":
        clear_screen()
        main_menu()
    else:
        # Fetch the command and function name from the dictionary
        dev_info = development.get(choice)
        if dev_info:
            app_name, install_function = dev_info
            # Dynamically call the appropriate function
            globals()[install_function](app_name)
        else:
            print("Invalid choice. Please try again.")

# [5] Debloat Menu
def debloat_menu():
    rich.print("This option is meant for [#d67200]ADVANCED[/#d67200] USERS")
    time.sleep(2)
    rich.print("\nProceed with [#d60000]EXTREME[/#d60000] Caution!\nEnsure you know what [#d60000]EVERY[/#d60000] option means.")
    time.sleep(2)
    rich.print("This application is not responsible for any possible [#250052]damage[/#250052] in your OS or Computer.")
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
    
    
    
    print("\n[0] Back to main menu")
    
    choice = input("\nSelect an option: ")
    
    if choice == "0":
        clear_screen()
        main_menu()
    # AUTO W/O SEC    
    elif choice == "1":
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
    # AUTO W SEC    
    elif choice == "2":
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
        
    elif choice == "3":
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
            
    elif choice == "4":
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
            
    elif choice == "5":
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
                
# [6] ISO Debloat Menu
def iso_menu():
    user_profile = os.environ.get('USERPROFILE')
    toolbox = os.path.join(user_profile, "rosalunna_toolbox")
    ISO = os.path.join(toolbox, "Windows-ISO-Debloater-1.3.2")
    script = os.path.join(ISO, "isoDebloaterScript.ps1")
    
    rich.print("This option is meant for [#d67200]ADVANCED[/#d67200] USERS")
    time.sleep(2)
    rich.print("\nProceed with [#d60000]EXTREME[/#d60000] Caution! And ensure you know what [#d60000]EVERY[/#d60000] option means.")
    time.sleep(2)
    rich.print("\nThis application is not responsible for any possible [#250052]damage[/#250052] in your OS or Computer.")
    time.sleep(1)
    
    choice = input("Do you wish to proceed to Nilesh's ISO Debloat Script (Y/N)? ")
    
    if choice == "n" or choice == "N":
        clear_screen()
        main_menu()
        
    elif choice == "y" or choice == "Y":                
        force_clean_directory(toolbox)
        git_clone_branch_txt()
        
        try:
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script],shell=True, check=True)
            print("ISO Debloat script executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error running the ISO Debloat script: {e}")
    else:        
        print("Not Known Option")
        time.sleep(3)
        clear_screen()
        iso_menu()        
        
main_menu()