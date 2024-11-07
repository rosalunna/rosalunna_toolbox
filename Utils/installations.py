import os,subprocess, shutil, requests, winreg, stat, time, ctypes, zipfile
import sys
from urllib.request import urlretrieve
import clr
import subprocess
import os

def install_winget_if_needed():
    # Check if winget exists
    try:
        result = subprocess.run(['winget', '--version'], capture_output=True, shell=True, text=True)
        if result.returncode == 0:
            print("Winget is already installed")
            return
        else:
            print("Winget not found. Installing winget...")
    except FileNotFoundError:
        print("Winget is not installed. Proceeding with installation...")
        try:
        # Run the command to install winget through Microsoft Store
            subprocess.run(['start', 'ms-windows-store://pdp/?productid=9NBLGGH4NNS1'], shell=True)
            print("Microsoft Store opened. Please complete the installation there.")
        except Exception as e:
            print(f"Error launching Microsoft Store: {e}")
            try:
                # Attempt to update Winget after opening the store
                subprocess.run(["powershell", "-Command", "winget upgrade"], capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                print("Error has occurred while trying to update Winget")
                print(e.stderr)    

# Use Winget To install stuff
def winget_install(package_name):
    try:
        # Run Winget install command
        subprocess.run(["winget", "install", package_name,"-i", "--interactive"], check=True, shell=True)
        print(f"{package_name} installed successfully!")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}.")

# Clean menu view
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Choco Install Apps
def choco_install(package):
    try:
        subprocess.run(["powershell","-Command","choco", "install", package, "--not-silent", "--failonstderr", "--no-silent", "-y" ])
        print(f"{package} installed successfully!")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}.")

# Scoop Install
def scoop_setup():
    scoop_cmd= 'Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser'
    scoop_cmd2 = 'iex "& {$(irm get.scoop.sh)} -RunAsAdmin"'
    try:
        process = subprocess.run(["powershell","-Command", scoop_cmd],
        capture_output = True, text= True, check= True
        )
        print(process.stdout)

    except subprocess.CalledProcessError as e:
          print("Installation failed!")
          print("Error:", e.stderr)

    try:
        process = subprocess.run(["powershell", "-Command", scoop_cmd2],
        capture_output = True, text= True, check= True
        )
        print(process.stdout)

        scoop_shims_path = os.path.expanduser("~\\scoop\\shims")
        os.environ["PATH"] += os.pathsep + scoop_shims_path

        path_true_update = """ $env:Path += ";$HOME\\scoop\\shims" """
        process2 = subprocess.run(["powershell", "-Command", path_true_update],
        capture_output= True, text= True, check= True
        )
        print("Scoop installed and PATH updated.")

    except subprocess.CalledProcessError as e:
          print("Installation failed!")
          print("Error:", e.stderr)
    try:
        scoop_update = subprocess.run(["powershell","-Command","scoop","update"], capture_output=True, text=True)      
    
    except subprocess.CalledProcessError as e:
          print("Installation failed!")
          print("Error:", e.stderr)

# Scoop Bucket
def scoop_bucket_add(package):
    try:
        process = subprocess.run(["powershell","-Command", "scoop", "bucket", "add", package])

    except subprocess.CalledProcessError as e:
        print("Installation failed!")
        print("Error:", e.stderr)

#Scoop Install Apps
def scoop_install(package):
    try:
        process = subprocess.run(["powershell","-Command", "scoop", "install", package])

    except subprocess.CalledProcessError as e:
           print("Installation failed!")
           print("Error:", e.stderr)

def download_file(url, filename):
    try:
        urlretrieve(url, filename)
        print(f"Downloaded successfully to {filename}")
        if filename.endswith(".py"):
            subprocess.run(["python", filename])
        else:
            subprocess.run([filename])
            print("File is being executed")
        

    except Exception as e:
        print(f"Error downloading: {str(e)}")

# Git Clone
def git_clone(url):
    user_profile = os.environ.get('USERPROFILE')
    
    try:
        git = subprocess.run(["powershell", "-Command", "git clone", url], 
                       capture_output=True, text=True, shell=True,
                       cwd=os.environ['USERPROFILE']
                       )
        if git.returncode != 0:
            print(f"Command failed with code: {git.returncode}")
            print(f"Error output: {git.stderr}")
        else:
            print(f"Output: {git.stdout}")    
    except subprocess.CalledProcessError as e:
        print(f"The command failed because: {e.stderr}")

def git_clone_branch_txt():
    # Grab TXT File to be replaced
    url = "https://github.com/rosalunna/rosalunna_toolbox/"
    
    try:
        git = subprocess.run(["powershell", "-Command", "git clone", "--branch", "Appslist.txt", "--single-branch", url], 
                       capture_output=True, text=True, shell=True,
                       cwd=os.environ['USERPROFILE']
                       )
    except subprocess.CalledProcessError as e:
        print(e.stderr)    

# Git Clean Repo 
def git_clean(dir):
    def on_rm_error(func, path, exc_info):
        # Ensure the file is writable before removing it
        os.chmod(path, stat.S_IWRITE)
        os.remove(path)

    if os.path.exists(dir):
        shutil.rmtree(dir, onerror=on_rm_error)
        print(f"Directory {dir} cleaned.")    

# Removes X directory
def remove_dir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
        print(f"{dir} was removed")
                
# Git clean cache
def git_clean_cache():
    gitcmdcache = "git rm --cached -r"
    try:
        subprocess.run(["powershell", "-Command", gitcmdcache], 
                       capture_output=True, text=True, shell=True
                       )   
    except subprocess.CalledProcessError as e:
        print(e.stderr)

def raphire_install_txt_change():
    user_profile = os.environ.get('USERPROFILE')
    modTXT = os.path.join(user_profile, "rosalunna_toolbox")
    raphiretxt = os.path.join(user_profile, "Win11Debloat")
    myTXT = os.path.join(modTXT, "Appslist.txt")
    raphiretxt2 = os.path.join(raphiretxt, "Appslist.txt")
    
    # Checks and rememove folders if already existent
    force_clean_directory(raphiretxt) 
    force_clean_directory(modTXT)

    #Download Both Folders
    git_clone("https://github.com/Raphire/Win11Debloat/")
    git_clone_branch_txt()    

    # Delete Raphires txt
    if os.path.exists(raphiretxt2):
        os.remove(raphiretxt2)

    # Copy Mine to Raphires Folder
    if os.path.exists(myTXT):
        shutil.copy(myTXT, raphiretxt)
        print(f"Copied {myTXT} to {raphiretxt}")
    else:
        print(f"The {myTXT} doesn't exist.")    

def raphire_execute_modscript():
    run_bat = "%USERPROFILE%\\Win11Debloat"
    try:
        subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Unrestricted -Scope Process; & %USERPROFILE%\\Win11Debloat\\Win11Debloat.ps1 -Silent -RunDefaults"], 
                       capture_output=True, shell=True, text=True
                       )
    except subprocess.CalledProcessError as e:
        print(e.stderr)    
        
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate_permissions():
    if not is_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

def force_clean_directory(directory):
    """Force clean a directory using system commands"""
    if not os.path.exists(directory):
        return True
        
    try:
        # First try to remove read-only attributes recursively
        os.system(f'attrib -r -s -h "{directory}\\*.*" /s /d')
        time.sleep(1)  # Give system time to process
        
        # Force delete using system command
        if os.system(f'rd /s /q "{directory}"') == 0:
            print(f"Successfully removed directory: {directory}")
            return True
        else:
            print(f"Failed to remove directory using system command: {directory}")
            return False
            
    except Exception as e:
        print(f"Error while cleaning directory {directory}: {str(e)}")
        return False

def ram_map():
    try:
        subprocess.run(["powershell", "-Command", "Rammap -E0 -Et -Ew"], 
                       shell=True, text=True
                       )
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(e.stderr)    

def schedule_rammap():
    # Define the path to RamMap (make sure this path is correct)
    programdata = os.environ.get('PROGRAMDATA')
    rammap_path = os.path.join(programdata, "chocolatey\\lib\\rammap\\tools\\RAMMap.exe")
    rammap_args = "-E0 -Et"
    # Check if RamMap exists at the specified path
    if not os.path.exists(rammap_path):
        print("Error: RamMap.exe not found at the specified path.")
        return

    # Define the task name
    task_name = "RAMCleanup"
    
    # Create the scheduled task using schtasks
    try:
        # Remove any existing task with the same name
        subprocess.run(["schtasks", "/Delete", "/TN", task_name, "/F"], 
                       capture_output=True, text=True, shell=True)

        # Create the new task to run every 30 minutes
        result = subprocess.run([
            "schtasks", "/Create", "/SC", "MINUTE", "/MO", "30",
            "/TN", task_name, "/TR", f'"{rammap_path}"{rammap_args}', "/F", "/RL", "HIGHEST", "/IT"
        ], capture_output=True, text=True, shell=True)
        
        if result.returncode == 0:
            print(f"Scheduled task '{task_name}' created successfully.")
        else:
            print(f"Error creating scheduled task '{task_name}': {result.stderr}")

    except subprocess.CalledProcessError as e:
        print("Failed to create scheduled task:", e.stderr)
   

def add_reg(reg_path):
    try:
        result = subprocess.run(["regedit", "/s", reg_path], capture_output=True, text=True)
        # Check the result
        if result.returncode == 0:
            print("Registry entry added successfully!")
        else:
            print("Failed to add registry entry.")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}")
           
def defender_total_removal():
    userprofile = os.environ.get('USERPROFILE')
    path = os.path.join(userprofile, "windows-defender-remover")
    force_clean_directory(path)

    git_clone("https://github.com/ionuttbara/windows-defender-remover/")

    # Paths
    remove_securitycomp = os.path.expandvars(r"%USERPROFILE%\\windows-defender-remover\\Remove_SecurityComp")
    Remove_defender = os.path.expandvars(r"%USERPROFILE%\\windows-defender-remover\\Remove_defender")

    add_reg(remove_securitycomp)
    add_reg(Remove_defender)

# -------- #
# Winget Silent Install
def winget_silent(pkg):
    try:
        winget = subprocess.run(["powershell", "winget", "install", pkg, "--silent", "--accept-package-agreements", "--accept-source-agreements"], 
                                shell=True, capture_output=True, text=True
                                )
        print(winget.stderr, "\n", winget.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stdout, e.stderr)

def taskschd_stop_delete(task):
    try:
        ts = subprocess.run(["schtasks", "/end", "/TN", task], 
                            capture_output=True, text=True, shell=True
                            )
        td = subprocess.run(["schtasks", "/Delete", "/TN", task, "/F"], 
                            capture_output=True, text=True, shell=True
                            )
        print(td.stderr, ts.stderr)
        print(td.stdout, ts.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr, e.stdout)    


def ms_edgeR():
    user_profile = os.environ.get('USERPROFILE')
    roto = os.path.join(user_profile, "rosalunna_toolbox")
    edgebatdir = "%USERPROFILE%\\rosalunna_toolbox\\edge.bat"

    taskschd_stop_delete("MicrosoftEdgeUpdateTaskMachineUA")
    taskschd_stop_delete("MicrosoftEdgeUpdateTaskMachineCore")

    
    
    # Checks and rememove folder if already existent
    force_clean_directory(roto)

    # Git Clone Applist.txt branch
    git_clone_branch_txt()
    try:

        a = subprocess.run(["powershell", "-Command", "Start-Process", edgebatdir], 
                       shell=True, text=True, capture_output=True
                       )
        print(a.stderr)
        print(a.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr, e.stdout)    

def winget_ms(pkg):
    try:
        ms = subprocess.run(["powershell", "-Command", "winget", "install", pkg, "-s", "msstore", "--accept-package-agreements", "--accept-source-agreements"], 
                   shell=True, capture_output=True, text=True
                   )
        print(ms.stderr)
        print(ms.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr, e.stdout)    


    

    