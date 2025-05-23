import rich
from Utils.installations import *
from Utils.menu_utils import generic_menu

def platform_menu():
    options = {
        key: {
            "label": data["name"],
            "action": lambda d=data: d["installer"](d["pkg"])
        } for key, data in {
            "1": {"name": "Steam", "installer": winget_install, "pkg": "Valve.Steam"},
            "2": {"name": "GOG Galaxy", "installer": winget_install, "pkg": "GOG.Galaxy"},
            "3": {"name": "Epic Games", "installer": choco_install, "pkg": "epicgameslauncher"},
            "4": {"name": "Battle.net", "installer": winget_install, "pkg": "Blizzard.BattleNet"},
            "5": {"name": "Rockstar Games", "installer": choco_install, "pkg": "rockstar-launcher"},
            "6": {"name": "EA App", "installer": choco_install, "pkg": "ea-app"},
            "7": {"name": "Ubisoft Connect", "installer": choco_install, "pkg": "ubisoft-connect"},
            "8": {"name": "Itch.io", "installer": choco_install, "pkg": "itch"},
            "9": {"name": "Bethesda Launcher", "installer": choco_install, "pkg": "Bethesda.Launcher"},
            "10": {"name": "Playnite", "installer": winget_install, "pkg": "Playnite.Playnite"},
            "11": {"name": "NVIDIA Geforce NOW", "installer": winget_install, "pkg": "Nvidia.GeForceNow"}
        }.items()
    }
    from rosalunna import main_menu
    generic_menu("[#7307a8]Gaming Platforms[/#7307a8]", options, main_menu)    
        
def monitoring_overclocking():
    options = {
        key: {
            "label": data["name"],
            "action": lambda d=data: d["installer"](d["pkg"])
        } for key, data in {
            "1": {"name": "HWiNFO", "installer": winget_install, "pkg": "REALiX.HWiNFO"},
            "2": {"name": "HWMonitor", "installer": winget_install, "pkg":"CPUID.HWMonitor"},
            "3": {"name": "NZXT CAM", "installer": winget_install, "pkg":"NZXT.CAM"},
            "4": {"name": "AIDA64 Extreme", "installer": winget_install, "pkg":"FinalWire.AIDA64.Extreme"},
            "5": {"name": "AIDA64 Engineer","installer": winget_install, "pkg":"FinalWire.AIDA64.Engineer"},
            "6": {"name": "Speccy", "installer": winget_install, "pkg": "Piriform.Speccy"},
            "7": {"name": "MSI Afterburner", "installer": winget_install, "pkg":"Guru3D.Afterburner"},
            "8": {"name": "GPU-Z", "installer": winget_install, "pkg":"TechPowerUp.GPU-Z"},
            "9": {"name": "CPU-Z", "installer": winget_install, "pkg":"CPUID.CPU-Z"},
            "10": {"name": "QuickCPU", "installer": winget_install, "pkg":"CoderBag.QuickCPUx64"},
            "11":{"name": "AMD Ryzen Master", "installer": choco_install, "pkg":"amd-ryzen-master"},
            "12":{"name": "Intel Extreme Tuning Utility", "installer": choco_install, "pkg":"intel-xtu"},
            "13":{"name": "Superposition Benchmark", "installer": choco_install, "pkg":"superposition-benchmark"},
            "14":{"name": "3DMark", "installer": choco_install, "pkg":"3dmark"},
            "15":{"name": "GeekBench", "installer": choco_install, "pkg":"geekbench"},
            "16":{"name": "Heaven Benchmark", "installer": choco_install, "pkg":"heaven-benchmark"},
            "17":{"name": "Cinebench R23", "installer": winget_install, "pkg":"Maxon.CinebenchR23"},
            "18":{"name": "OCCT", "installer": winget_install, "pkg":"OCBase.OCCT.Personal"}
        }.items()
    }   
    from rosalunna import main_menu
    generic_menu("[#006bff]Hardware Monitoring and Benchmarking[/#006bff]", options, main_menu)

def apps_utils():
    options = {
        key: {
            "label": data["name"],
            "action": lambda d=data: d["installer"](d["pkg"])
        } for key, data in {
            "1": {"name": "Discord", "installer": winget_install, "pkg": "Discord.Discord"},
            "2": {"name": "Spotify", "installer": winget_install, "pkg":"Spotify.Spotify"},
            "3": {"name": "WhatsApp", "installer": winget_ms, "pkg":"9NKSQGP7F2NH"},
            "4": {"name": "Telegram", "installer": choco_install, "pkg":"telegram.install"},
            "5": {"name": "Notepads App","installer": winget_install, "pkg":"JackieLiu.NotepadsApp"},
            "6": {"name": "Notepad++", "installer": winget_install, "pkg":"Notepad++.Notepad++"},
            "7": {"name": "VLC Media Player", "installer": winget_install, "pkg":"VideoLAN.VLC"},
            "8": {"name": "Screenbox", "installer": winget_install, "pkg":"Starpine.Screenbox"},
            "9": {"name": "Image Glass", "installer": winget_install, "pkg":"DuongDieuPhap.ImageGlass"},
            "10":{"name": "Nora Music Player", "installer": winget_install, "pkg":"Sandakan.Nora"},
            "11":{"name": "WPS Office", "installer": winget_install, "pkg":"Kingsoft.WPSOffice"} 
        }.items()
    }   
    from rosalunna import main_menu
    generic_menu("[#006bff]Common Applications and Utilities[/#006bff]", options, main_menu)
    
def peripheals_apps():
    options = {
        key: {
            "label": data["name"],
            "action": lambda d=data: d["installer"](d["pkg"])
        } for key, data in {
            "1": {"name": "Razer Synapse 4", "installer": winget_install, "pkg": "RazerInc.RazerInstaller.Synapse4"},
            "2": {"name": "Razer Synapse 3", "installer": winget_install, "pkg": "RazerInc.RazerInstaller.Synapse3"},
            "3": {"name": "HyperX NGENUITY", "installer": choco_install, "pkg": "hyperx-ngenuity"},
            "4": {"name": "SteelSeries GG", "installer": winget_install, "pkg": "SteelSeries.GG"},
            "5": {"name": "Logitech GHUB", "installer": winget_install, "pkg": "Logitech.GHUB"},
            "6": {"name": "Corsair iCUE 5", "installer": winget_install, "pkg": "Corsair.iCUE.5"},
            "7": {"name": "Corsair iCUE 4", "installer": winget_install, "pkg": "Corsair.iCUE.4"},
            "8": {"name": "Corsair iCUE 3", "installer": winget_install, "pkg": "Corsair.iCUE.3"} 
        }.items()
    }   
    from rosalunna import main_menu
    generic_menu("[#006bff]Peripheals[/#006bff]", options, main_menu)
    
def custom_mod():
    options = {
        key: {
            "label": data["name"],
            "action": lambda d=data: d["installer"](d["pkg"])
        } for key, data in {
            "1":{"name": "ohmyposh", "installer": winget_install,"pkg":"JanDeDobbeleer.OhMyPosh"},
            "2":{"name": "komorebi", "installer": winget_install,"pkg":"LGUG2Z.komorebi"},
            "3":{"name": "GlazeWM" , "installer": winget_install,"pkg":"glzr-io.glazewm"},
            "4":{"name": "FancyWM" , "installer": winget_ms,"pkg":"9P1741LKHQS9"},
            "5":{"name": "SecureUX Theme" , "installer": winget_install,"pkg":"namazso.SecureUXTheme"},
            "6":{"name": "YASB" , "installer": winget_install,"pkg":"AmN.yasb"},
            "7":{"name": "Flow Launcher" , "installer": winget_install,"pkg":"Flow-Launcher.Flow-Launcher"},
            "7":{"name": "Nilesoft Shell" , "installer": winget_install,"pkg":"Nilesoft.Shell"}
        }.items()
    }   
    from rosalunna import main_menu
    generic_menu("[#800080]PC Modding/Customizing[/#800080]", options, main_menu)
    
def development_menu():
    options = {
        key: {
            "label": data["name"],
            "action": lambda d=data: d["installer"](d["pkg"])
        } for key, data in {
            "1": {"name": "Python", "installer": winget_install, "pkg": "Python.Python.3.13"},
            "2": {"name": "Java (JDK)", "installer": winget_install, "pkg": "Oracle.JDK.23"},
            "3": {"name": "Ruby", "installer": winget_install, "pkg": "RubyInstallerTeam.Ruby.3.2"},
            "4": {"name": "Kotlin (Compiler)", "installer": winget_install, "pkg": "JetBrains.Kotlin.Compiler"},
            "5": {"name": "Go", "installer": winget_install, "pkg": "GoLang.Go"},
            "6": {"name": "TypeScript (via Node.js LTS)", "installer": winget_install, "pkg": "Nodejs.LTS"},
            "7": {"name": "Rust", "installer": winget_install, "pkg": "Rust.Rustlang.Rustup"},
            "8": {"name": "PHP", "installer": winget_install, "pkg": "PHP.PHP.8.4"},
            "9": {"name": "Lua", "installer": winget_install, "pkg": "DEVCOM.Lua"},
            "10": {"name": "Ada (GNAT)", "installer": winget_install, "pkg": "AdaCore.GNAT"},

            # Code Editors/IDEs
            "11": {"name": "VS Code", "installer": winget_install, "pkg": "Microsoft.VisualStudioCode"},
            "12": {"name": "VS Codium", "installer": winget_install, "pkg": "VSCodium.VSCodium"},
            "13": {"name": "IntelliJ IDEA Community", "installer": winget_install, "pkg": "JetBrains.IntelliJIDEA.Community"},
            "14": {"name": "PyCharm Community", "installer": winget_install, "pkg": "JetBrains.PyCharm.Community"},
            "15": {"name": "Arduino IDE", "installer": winget_install, "pkg": "ArduinoSA.IDE.stable"},
            "16": {"name": "Eclipse IDE", "installer": winget_install, "pkg": "EclipseFoundation.EclipseIDE"},
            "17": {"name": "JupyterLab (includes Notebook)", "installer": winget_install, "pkg": "Jupyter.JupyterLab"},
            "18": {"name": "Code::Blocks", "installer": winget_install, "pkg": "CodeBlocks.CodeBlocks"}
        }.items()
    }
    from rosalunna import main_menu
    generic_menu("[#800080]PC Modding/Customizing[/#800080]", options, main_menu)   
    
    