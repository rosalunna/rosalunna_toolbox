import subprocess, os, shutil, winreg

def regedit():
    #Disable Regedit Telemetry
    key_path = r"SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection"
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    location = winreg.HKEY_LOCAL_MACHINE
    winreg.OpenKeyEx(location, r"SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection")
    winreg.SetValueEx(key,"AllowTelemetry",0, winreg.REG_DWORD, 0)
    winreg.CloseKey(key)

    #Regedit GPU Tweak
    key_path = r"SOFTWARE\\Microsoft\\Microsoft\\DirectX\\UserGpuPreferences"
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
    location = winreg.HKEY_CURRENT_USER
    winreg.OpenKeyEx(location, r"SOFTWARE\\Microsoft\\Microsoft\\DirectX\\UserGpuPreferences")
    winreg.SetValueEx(key,"GpuPreference",0, winreg.REG_DWORD, 2)
    winreg.CloseKey(key)

    #Regedit GameDVR
    key_path = r"System\\GameConfigStore"
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
    location = winreg.HKEY_CURRENT_USER
    winreg.OpenKeyEx(location, r"System\\GameConfigStore")
    winreg.SetValueEx(key,"GameDVR_DSEBehavior",0, winreg.REG_DWORD, 2)
    winreg.CloseKey(key)

    #Regedit Current Control Set
    key_path = r"SYSTEM\\CurrentControlSet\\Control"
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    location = winreg.HKEY_LOCAL_MACHINE
    winreg.OpenKeyEx(location, r"SYSTEM\\CurrentControlSet\\Control")
    winreg.SetValueEx(key,"SvcHostSplitThresholdInKB",0, winreg.REG_DWORD, 0x04000000)
    winreg.CloseKey(key)

    #NDU
    key_path = r"SYSTEM\\ControlSet001\\Services\\Ndu"
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    location = winreg.HKEY_LOCAL_MACHINE
    winreg.OpenKeyEx(location, r"SYSTEM\\ControlSet001\\Services\\Ndu")
    winreg.SetValueEx(key,"Start",0, winreg.REG_DWORD, 0x00000004)
    winreg.CloseKey(key)

    #RAM and Mitigations
    key_path = r"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management"
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    location = winreg.HKEY_LOCAL_MACHINE
    winreg.OpenKeyEx(location, r"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management")
    winreg.SetValueEx(key,"LargeSystemCache",0, winreg.REG_DWORD, 0x00000000)
    winreg.SetValueEx(key,"FeatureSettings",0, winreg.REG_DWORD, 0x00000000)
    winreg.SetValueEx(key,"FeatureSettingsOverrideMask",0, winreg.REG_DWORD, 3)
    winreg.SetValueEx(key,"FeatureSettingsOverride",0, winreg.REG_DWORD, 3)
    winreg.CloseKey(key)

    #PowerThrottling
    key_path = r"SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling"
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    location = winreg.HKEY_LOCAL_MACHINE
    winreg.OpenKeyEx(location, r"SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling")
    winreg.SetValueEx(key,"PowerThrottlingOff",0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

    # Standby Memory
    key_path = r"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management"
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    loc = winreg.HKEY_LOCAL_MACHINE
    
    winreg.OpenKeyEx(loc, r"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management")
    winreg.SetValueEx(key, "ClearPageFileAtShutdown", 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

    # Network Throttling
    key_path = r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile"
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    loc = winreg.HKEY_LOCAL_MACHINE
    
    winreg.OpenKeyEx(loc, r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile")
    winreg.SetValueEx(key, "NetworkThrottlingIndex", 0, winreg.REG_DWORD, 0x0000000a)
    winreg.SetValueEx(key, "SystemResponsiveness", 0, winreg.REG_DWORD, 0x00000014)
    winreg.CloseKey(key)

import subprocess

# Stop and Disable Services

def SD_Service(service_name):
    command = [
        "powershell", "-Command",
        f"Stop-Service -Name '{service_name}' -Force; Set-Service -Name '{service_name}' -StartupType Disabled"
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Service '{service_name}' stopped and disabled successfully.")
    else:
        print(f"Error: {result.stderr}")

def remove_services():
    SD_Service("SysMain")
    SD_Service("BDESVC")
    SD_Service("DiagTrack")
    SD_Service("WerSVC")
    SD_Service("RemoteRegistry")
    SD_Service("SCardSvr")
    SD_Service("PhoneSvc")
    SD_Service("lfsvc")
    SD_Service("RmSvc")
    SD_Service("SensrSvc")
    SD_Service("WalletService")
    SD_Service("MicrosoftEdgeElevationService")
    SD_Service("edgeupdate")
    SD_Service("edgeupdatem")
    SD_Service("pla")
    #xbox
    SD_Service("XboxGipSvc")
    SD_Service("XblAuthManager")
    SD_Service("XblGameSave")
    SD_Service("XboxNetApiSvc")