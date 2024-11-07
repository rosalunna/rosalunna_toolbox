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

