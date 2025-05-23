import rich
from rich.table import Table
from Utils.installations import*
from itertools import zip_longest

def browsers_menu():
    options = ["[#1703fc](01) Chromium-based menu[/#1703fc]", "[#fc7f03](02) Firefox-based/forks menu[/#fc7f03]\n",
               "[#ffffff](0) Back to main menu[/#ffffff]"]
    clear_screen()
    rich.print("[#fc0366]Browsers Subtype menu\n [/#fc0366]")
    for option in options:
        rich.print(option)
    
    question = input("Choose an option: ")
    match question:
        case "1":
            clear_screen()
            chromium_menu()
        case "2":
            clear_screen()
            firefox_menu()
        case "0":
            clear_screen()
            from rosalunna import main_menu
            main_menu()        
        case _:
            rich.print("[#fc0307]Not known option[/#fc0307]")
            clear_screen()
            browsers_menu()
            

browsersC = ["[#8a0b33](01) Vivaldi[/#8a0b33]", "[#91002c](02) Opera Types[/#91002c]", "[#ff3012](03) Brave[/#ff3012]",
            "[#37cab3](04) Microsoft Edge[/#37cab3]  ", "[#ff536a](05) Arc[/#ff536a]", "[#1c997b](06) Basilisk[/#1c997b]",
            "[#e34036](07) Google Chrome[/#e34036]", "[#e34036](08) Chromium[/#e34036]", "[#e34036](09) Cromite[/#e34036]",
            "  [#e34036](10) DuckDuckGo[/#e34036]", "  [#08dbb7](11) Naver Whale[/#08dbb7]", "  [#b58749](12) Otter Browser[/#b58749]",
            "  [#27467b](13) Pale moon[/#27467b]", "  [#216bd5](14) Thorium[/#216bd5]"]

browsersF = ["[#ff4c43](01) Mozilla Firefox[/#ff4c43]  ", "[#4a12e9](02) Floorp[/#4a12e9]", "[#08afff](03) LibreWolf[/#08afff]",
             "[#08bcf9](04) WaterFox[/#08bcf9]", "[#39b7c2](05) Maxthon[/#39b7c2] ", "[#8d7a83](06) Mercury[/#8d7a83] ", "[#fcd20e](07) Mullvad[/#fcd20e] ",
             "[#a948f0](08) Tor[/#a948f0] ", "[#bbb3b2](09) Zen[/#bbb3b2]"]

def chromium_menu():
    rich.print("[#1c0b8a]|-----------CHROMIUM MENU-----------|[/#1c0b8a]\n")
    left_column = browsersC[:9]
    right_column = browsersC[9:]
    table = Table(show_header=False, show_edge =False, padding=0)
    table.add_column(style="#8a0b33")
    table.add_column(style="#e34036")

    for left, right in zip_longest(left_column, right_column):
        table.add_row(left,right)    
    rich.print(table)
    print("\n(0) Back to subtype menu")
    choice = input("\nChoose an option: ")
    pkgwinget = {"1": "Vivaldi.Vivaldi", "4": "Microsoft.Edge",
                 "5": "TheBrowserCompany.Arc", "6": "Basilisk.Basilisk", "7": "Google.Chrome",
                 "8": "Hibbiki.Chromium", "9": "uazo.cromite", "10": "DuckDuckGo.DesktopBrowser",
                 "11": "NAVER.Whale", "12": "OtterBrowserTeam.OtterBrowser", "13": "MoonchildProductions.PaleMoon",
                }
    pkgchoco = {"3": "brave", "14": "thorium"}
    
    if choice in pkgwinget:
        winget_install(pkgwinget[choice])
    elif choice in pkgchoco:
        choco_install(pkgchoco[choice])
    elif choice == "2":
        opera = ["[#ff1b2d](01) Opera[/#ff1b2d]", "[#fa1e4e](02) Opera GX[/#fa1e4e]",
                "[#3b6e63](03) Opera Air[/#3b6e63]", "\n(0) Back to chromium menu"]
        clear_screen()
        for names in opera:
            rich.print(names)
        choice2 = input("\nChoose an opera option: ")    
        operawinget = {"1": "Opera.Opera", "2": "Opera.OperaGX",
                      "3": "Opera.OperaAir"}
        if choice2 in operawinget:
            winget_install(operawinget[choice2])
        elif choice2 == "0":
            clear_screen()
            chromium_menu()
        else:
            rich.print("[#ff1b2d]Invalid option, try again.[/#ff1b2d]")
            time.sleep(1)
            clear_screen()
            chromium_menu()
    elif choice == "0":
        clear_screen()
        browsers_menu()

       
def firefox_menu():
    rich.print("[#fc7f03]|-------------FIREFOX MENU-------------|[/#fc7f03]\n")
    left_column = browsersF[:5]
    right_column = browsersF[5:]
    table = Table(show_header=False, show_edge =True, padding=0)
    table.add_column(style="#8a0b33")
    table.add_column(style="#e34036")
    
    for left, right in zip_longest(left_column, right_column):
        table.add_row(left,right)
    rich.print(table)
    print("\n(0) Back to subtype menu")
    choice = input("\nChoose an option: ")
    pkgwinget = {"1": "Mozilla.Firefox", "2": "Ablaze.Floorp",
                 "3": "LibreWolf.LibreWolf", "4": "Waterfox.Waterfox",
                 "5": "Maxthon.Maxthon", "7": "MullvadVPN.MullvadBrowser"
                 }
    pkgchoco = {"6": "mercury", "8":"tor-browser"}
    
    if choice in pkgwinget:
        winget_install(pkgwinget[choice])
    elif choice in pkgchoco:
        choco_install(pkgchoco[choice])
    elif choice == "0":
        clear_screen()
        browsers_menu()    
    else:
        rich.print("[#af0606]Invalid option. Try again![/#af0606]")
        time.sleep(1.2)
        clear_screen()
        firefox_menu()
        
                    
                