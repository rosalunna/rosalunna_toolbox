import subprocess, rich, time
def restore_oldright_menu():
    command = [
        "reg.exe", "add",
        "HKCU\\Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\\InprocServer32",
        "/f", "/ve"
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        rich.print("[#fc03b6]Old[/#fc03b6] Right Click Context Menu [#0339fc]Restored[/#0339fc]")
        time.sleep(1)
        rich.print("[#0339fc]Restarting[/#0339fc] Windows Explorer")
        time.sleep(1.5)
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=True)
        subprocess.run(["start", "explorer.exe"], shell=True, check=True)
        rich.print("Explorer restarted successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to restart Windows Explorer")
        print("Error: ", e)    
        
def restore_modernright_menu():
    command = [
        "reg.exe", "delete",
        "HKCU\\Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\\InprocServer32",
        "/f"
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        rich.print("[#fc03b6]Modern[/#fc03b6] Right Click Context Menu [#0339fc]Restored[/#0339fc]")
        time.sleep(1)
        rich.print("[#0339fc]Restarting[/#0339fc] Windows Explorer")
        time.sleep(1.5)
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=True)
        subprocess.run(["start", "explorer.exe"], shell=True, check=True)
        rich.print("Explorer restarted [#0339fc]successfully[/#0339fc].")
    except subprocess.CalledProcessError as e:
        print("Failed to restart Windows Explorer")
        print("Error: ", e)        