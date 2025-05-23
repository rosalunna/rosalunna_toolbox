from rich import print
import time
from Utils.installations import clear_screen

def generic_menu(title, options_dict, back_func=None):
    print(f"\n{title}\n")
    for key, value in options_dict.items():
        print(f"[{key}] {value['label']}")
    print("[0] Voltar")
    
    choice = input("\nEscolha uma opção: ")
    if choice == "0":
        if back_func:
            clear_screen()
            back_func()
        return

    if choice in options_dict:
        clear_screen()
        options_dict[choice]["action"]()
    else:
        print("[#fc0345]Opção inválida![/#fc0345]")
        time.sleep(1)
        clear_screen()
        generic_menu(title, options_dict, back_func)   
    