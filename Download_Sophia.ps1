<#
	.SYNOPSIS
	Download the latest Sophia Script version, depending on what Windows or PowerShell versions are used to

	.SYNOPSIS
	Download the latest Sophia Script version, depending on what Windows or PowerShell versions are used to
	E.g., if you start script on Windows 11 via PowerShell 5.1 you will start downloading Sophia Script for Windows 11 PowerShell 5.1

	.EXAMPLE Download and expand Sophia Script archive
	iwr script.sophia.team -useb | iex

	.NOTES
	Current user
#>
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

if ($Host.Version.Major -eq 5)
{
	# Progress bar can significantly impact cmdlet performance
	# https://github.com/PowerShell/PowerShell/issues/2138
	$Script:ProgressPreference = "SilentlyContinue"
}

$Parameters = @{
	Uri             = "https://api.github.com/repos/farag2/Sophia-Script-for-Windows/releases/latest"
	UseBasicParsing = $true
}
$LatestGitHubRelease = (Invoke-RestMethod @Parameters).tag_name

$DownloadsFolder = Get-ItemPropertyValue -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" -Name "{374DE290-123F-4565-9164-39C4925E467B}"

$Parameters = @{
	Uri             = "https://raw.githubusercontent.com/farag2/Sophia-Script-for-Windows/master/sophia_script_versions.json"
	UseBasicParsing = $true
}

switch ((Get-CimInstance -ClassName Win32_OperatingSystem).BuildNumber)
{
	"17763"
	{
		# Check for Windows 10 LTSC 2019
		if ((Get-ItemPropertyValue -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name ProductName) -match "LTSC 2019")
		{
			$LatestRelease = (Invoke-RestMethod @Parameters).Sophia_Script_Windows_10_LTSC2019
			$Parameters = @{
				Uri             = "https://github.com/farag2/Sophia-Script-for-Windows/releases/download/$LatestGitHubRelease/Sophia.Script.for.Windows.10.LTSC.2019.v$LatestRelease.zip"
				OutFile         = "$env:USERPROFILE\Sophia.Script.zip"
				UseBasicParsing = $true
				Verbose         = $true
			}

			$Version = "Windows_10_LTSC2019"
		}
		else
		{
			exit
		}
	}
	"19044"
	{
		# Check for Windows 10 LTSC 2021
		if ((Get-ItemPropertyValue -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name ProductName) -match "LTSC 2021")
		{
			$LatestRelease = (Invoke-RestMethod @Parameters).Sophia_Script_Windows_10_LTSC2021
			$Parameters = @{
				Uri             = "https://github.com/farag2/Sophia-Script-for-Windows/releases/download/$LatestGitHubRelease/Sophia.Script.for.Windows.10.LTSC.2021.v$LatestRelease.zip"
				OutFile         = "$env:USERPROFILE\Sophia.Script.zip"
				UseBasicParsing = $true
				Verbose         = $true
			}
			$Version = "Windows_10_LTSC2021"
		}
		else
		{

			exit
		}
	}
	"19045"
	{
		if ($Host.Version.Major -eq 5)
		{
			$LatestRelease = (Invoke-RestMethod @Parameters).Sophia_Script_Windows_10_PowerShell_5_1
			$Parameters = @{
				Uri             = "https://github.com/farag2/Sophia-Script-for-Windows/releases/download/$LatestGitHubRelease/Sophia.Script.for.Windows.10.v$LatestRelease.zip"
				OutFile         = "$env:USERPROFILE\Sophia.Script.zip"
				UseBasicParsing = $true
				Verbose         = $true
			}

			$Version = "Windows_10_PowerShell_5.1"
		}
		else
		{
			$LatestRelease = (Invoke-RestMethod @Parameters).Sophia_Script_Windows_10_PowerShell_7
			$Parameters = @{
				Uri             = "https://github.com/farag2/Sophia-Script-for-Windows/releases/download/$LatestGitHubRelease/Sophia.Script.for.Windows.10.PowerShell.7.v$LatestRelease.zip"
				OutFile         = "$env:USERPROFILE\Sophia.Script.zip"
				UseBasicParsing = $true
				Verbose         = $true
			}

			$Version = "Windows_10_PowerShell_7"
		}
	}
	{$_ -ge 22631}
	{
		if ((Get-WindowsEdition -Online).Edition -notmatch "EnterpriseS")
		{
			if ($Host.Version.Major -eq 5)
			{
				$LatestRelease = (Invoke-RestMethod @Parameters).Sophia_Script_Windows_11_PowerShell_5_1
				$Parameters = @{
					Uri             = "https://github.com/farag2/Sophia-Script-for-Windows/releases/download/$LatestGitHubRelease/Sophia.Script.for.Windows.11.v$LatestRelease.zip"
					OutFile         = "$env:USERPROFILE\Sophia.Script.zip"
					UseBasicParsing = $true
					Verbose         = $true
				}

				$Version = "Windows_11_PowerShell_5.1"
			}
			else
			{
				$LatestRelease = (Invoke-RestMethod @Parameters).Sophia_Script_Windows_11_PowerShell_7
				$Parameters = @{
					Uri             = "https://github.com/farag2/Sophia-Script-for-Windows/releases/download/$LatestGitHubRelease/Sophia.Script.for.Windows.11.PowerShell.7.v$LatestRelease.zip"
					OutFile         = "$env:USERPROFILE\Sophia.Script.zip"
					UseBasicParsing = $true
					Verbose         = $true
				}

				$Version = "Windows_11_PowerShell_7"
			}
		}
		else
		{
			$LatestRelease = (Invoke-RestMethod @Parameters).Sophia_Script_Windows_11_LTSC2024
			$Parameters = @{
				Uri             = "https://github.com/farag2/Sophia-Script-for-Windows/releases/download/$LatestGitHubRelease/Sophia.Script.for.Windows.11.LTSC.2024.v$LatestRelease.zip"
				OutFile         = "$env:USERPROFILE\Sophia.Script.zip"
				UseBasicParsing = $true
				Verbose         = $true
			}

			$Version = "Windows_11_LTSC2024"
		}
	}
}
Invoke-WebRequest @Parameters

if (-not (Test-Path -Path "$env:USERPROFILESophia.Script.zip"))
{

	exit
}

$Parameters = @{
	Path            = "$env:USERPROFILE\Sophia.Script.zip"
	DestinationPath = "$env:USERPROFILE"
	Force           = $true
}
Expand-Archive @Parameters

Remove-Item -Path "$env:USERPROFILE\Sophia.Script.zip" -Force

Start-Sleep -Second 1

switch ($Version)
{
	"Windows_10_LTSC2019"
	{
		Invoke-Item -Path "$env:USERPROFILE\Sophia_Script_for_Windows_10_LTSC_2019_v$LatestRelease"

		if ((([System.Security.Principal.WindowsIdentity]::GetCurrent()).Owner -eq "S-1-5-32-544"))
		{
			Set-Location -Path "$env:USERPROFILE\Sophia_Script_for_Windows_10_LTSC_2019_v$LatestRelease"
		}
	}
	"Windows_10_LTSC2021"
	{
		Invoke-Item -Path "$env:USERPROFILE\Sophia_Script_for_Windows_10_LTSC_2021_v$LatestRelease"

		if ((([System.Security.Principal.WindowsIdentity]::GetCurrent()).Owner -eq "S-1-5-32-544"))
		{
			Set-Location -Path "$env:USERPROFILE\Sophia_Script_for_Windows_10_LTSC_2021_v$LatestRelease"
		}
	}
	"Windows_11_LTSC2024"
	{
		Invoke-Item -Path "$env:USERPROFILE\Sophia_Script_for_Windows_11_LTSC_2024_v$LatestRelease"
		if ((([System.Security.Principal.WindowsIdentity]::GetCurrent()).Owner -eq "S-1-5-32-544"))
		{
			Set-Location -Path "$env:USERPROFILE\Sophia_Script_for_Windows_11_LTSC_2024_v$LatestRelease"
		}
	}
	"Windows_10_PowerShell_5.1"
	{
		Invoke-Item -Path "$env:USERPROFILE\Sophia_Script_for_Windows_10_v$LatestRelease"

		if ((([System.Security.Principal.WindowsIdentity]::GetCurrent()).Owner -eq "S-1-5-32-544"))
		{
			Set-Location -Path "$env:USERPROFILE\Sophia_Script_for_Windows_10_v$LatestRelease"
		}
	}
	"Windows_10_PowerShell_7"
	{
		Invoke-Item -Path "$env:USERPROFILE\Sophia_Script_for_Windows_10_PowerShell_7_v$LatestRelease"

		if ((([System.Security.Principal.WindowsIdentity]::GetCurrent()).Owner -eq "S-1-5-32-544"))
		{
			Set-Location -Path "$env:USERPROFILE\Sophia_Script_for_Windows_10_PowerShell_7_v$LatestRelease"
		}
	}
	"Windows_11_PowerShell_5.1"
	{
		Invoke-Item -Path "$env:USERPROFILE\Sophia_Script_for_Windows_11_v$LatestRelease"

		if ((([System.Security.Principal.WindowsIdentity]::GetCurrent()).Owner -eq "S-1-5-32-544"))
		{
			Set-Location -Path "$env:USERPROFILE\Sophia_Script_for_Windows_11_v$LatestRelease"
		}
	}
	"Windows_11_PowerShell_7"
	{
		Invoke-Item -Path "$env:USERPROFILE\Sophia_Script_for_Windows_11_PowerShell_7_v$LatestRelease"

		if ((([System.Security.Principal.WindowsIdentity]::GetCurrent()).Owner -eq "S-1-5-32-544"))
		{
			Set-Location -Path "$env:USERPROFILE\Sophia_Script_for_Windows_11_PowerShell_7_v$LatestRelease"
		}
	}
}

# https://github.com/PowerShell/PowerShell/issues/21070
$CompilerParameters = [System.CodeDom.Compiler.CompilerParameters]::new("System.dll")
$CompilerParameters.TempFiles = [System.CodeDom.Compiler.TempFileCollection]::new($env:TEMP, $false)
$CompilerParameters.GenerateInMemory = $true
$Signature = @{
	Namespace          = "WinAPI"
	Name               = "ForegroundWindow"
	Language           = "CSharp"
	CompilerParameters = $CompilerParameters
	MemberDefinition   = @"
[DllImport("user32.dll")]
public static extern bool ShowWindowAsync(IntPtr hWnd, int nCmdShow);
[DllImport("user32.dll")]
[return: MarshalAs(UnmanagedType.Bool)]
public static extern bool SetForegroundWindow(IntPtr hWnd);
"@
	}

# PowerShell 7 has CompilerOptions argument instead of CompilerParameters as PowerShell 5 has
# https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/add-type#-compileroptions
if ($Host.Version.Major -eq 7)
{
	$Signature.Remove("CompilerParameters")
	$Signature.Add("CompilerOptions", $CompilerParameters)
}

if (-not ("WinAPI.ForegroundWindow" -as [type]))
{
	Add-Type @Signature
}

Start-Sleep -Seconds 1