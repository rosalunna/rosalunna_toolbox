#Requires -RunAsAdministrator
#Requires -Version 5.1

[CmdletBinding()]
param
(
	[Parameter(Mandatory = $false)]
	[string[]]
	$Functions
)

Clear-Host

$Host.UI.RawUI.WindowTitle = "Sophia Script for Windows 11 v6.7.2 | Made with $([System.Char]::ConvertFromUtf32(0x1F497)) of Windows | $([System.Char]0x00A9) farag, Inestic & lowl1f3, 2014$([System.Char]0x2013)2024"

# Check whether all files were expanded before running
$ScriptFiles = @(
	"$PSScriptRoot\Localizations\de-DE\Sophia.psd1",
	"$PSScriptRoot\Localizations\en-US\Sophia.psd1",
	"$PSScriptRoot\Localizations\es-ES\Sophia.psd1",
	"$PSScriptRoot\Localizations\fr-FR\Sophia.psd1",
	"$PSScriptRoot\Localizations\hu-HU\Sophia.psd1",
	"$PSScriptRoot\Localizations\it-IT\Sophia.psd1",
	"$PSScriptRoot\Localizations\pl-PL\Sophia.psd1",
	"$PSScriptRoot\Localizations\pt-BR\Sophia.psd1",
	"$PSScriptRoot\Localizations\ru-RU\Sophia.psd1",
	"$PSScriptRoot\Localizations\tr-TR\Sophia.psd1",
	"$PSScriptRoot\Localizations\uk-UA\Sophia.psd1",
	"$PSScriptRoot\Localizations\zh-CN\Sophia.psd1",
	"$PSScriptRoot\Module\Sophia.psm1",
	"$PSScriptRoot\Manifest\Sophia.psd1"
)
if (($ScriptFiles | Test-Path) -contains $false)
{
	Write-Information -MessageData "" -InformationAction Continue
	Write-Warning -Message "There are no files in the script folder. Please, re-download the archive and follow the guide: https://github.com/farag2/Sophia-Script-for-Windows?tab=readme-ov-file#how-to-use."
	Write-Information -MessageData "" -InformationAction Continue

	Write-Verbose -Message "https://t.me/sophia_chat" -Verbose
	Write-Verbose -Message "https://discord.gg/sSryhaEv79" -Verbose

	exit
}

Remove-Module -Name Sophia -Force -ErrorAction Ignore
try
{
	Import-LocalizedData -BindingVariable Global:Localization -UICulture $PSUICulture -BaseDirectory $PSScriptRoot\Localizations -FileName Sophia -ErrorAction Stop
}
catch
{
	Import-LocalizedData -BindingVariable Global:Localization -UICulture en-US -BaseDirectory $PSScriptRoot\Localizations -FileName Sophia
}

# Check whether script is not running via PowerShell (x86)
try
{
	Import-Module -Name $PSScriptRoot\Manifest\Sophia.psd1 -PassThru -Force -ErrorAction Stop
}
catch [System.InvalidOperationException]
{
	Write-Warning -Message $Localization.PowerShellx86Warning

	Write-Verbose -Message "https://t.me/sophia_chat" -Verbose
	Write-Verbose -Message "https://discord.gg/sSryhaEv79" -Verbose

	exit
}

<#
	.SYNOPSIS
	Run the script by specifying functions as an argument
	Запустить скрипт, указав в качестве аргумента функции

	.EXAMPLE
	.\Sophia.ps1 -Functions "DiagTrackService -Disable", "DiagnosticDataLevel -Minimal", UninstallUWPApps

	.NOTES
	Use commas to separate funtions
	Разделяйте функции запятыми
#>
if ($Functions)
{
	Invoke-Command -ScriptBlock {InitialActions}

	foreach ($Function in $Functions)
	{
		Invoke-Expression -Command $Function
	}

	# The "PostActions" and "Errors" functions will be executed at the end
	Invoke-Command -ScriptBlock {PostActions; Errors}

	exit
}


#region Protection

# The mandatory checks. If you want to disable a warning message about whether the preset file was customized, remove the "-Warning" argument.
InitialActions -Warning

# Enable script logging. Log will be recorded into the script folder. To stop logging just close the console or type "Stop-Transcript".
# Logging

# Create a restore point.
CreateRestorePoint

#endregion Protection


#region Privacy & Telemetry

# Disable the "Connected User Experiences and Telemetry" service (DiagTrack), and block the connection for the Unified Telemetry Client Outbound Traffic. Disabling the "Connected User Experiences and Telemetry" service (DiagTrack) can cause you not being able to get Xbox achievements anymore and affects Feedback Hub and affects Feedback Hub.
DiagTrackService -Disable

# Enable the "Connected User Experiences and Telemetry" service (DiagTrack), and allow the connection for the Unified Telemetry Client Outbound Traffic (default value).
# DiagTrackService -Enable

# Set the diagnostic data collection to minimum.
DiagnosticDataLevel -Minimal

# Set the diagnostic data collection to default (default value).
# DiagnosticDataLevel -Default

# Turn off the Windows Error Reporting.
ErrorReporting -Disable

# Turn on the Windows Error Reporting (default value).
# ErrorReporting -Enable

# Change the feedback frequency to "Never".
FeedbackFrequency -Never

# Change the feedback frequency to "Automatically" (default value).
# FeedbackFrequency -Automatically

# Turn off the diagnostics tracking scheduled tasks.
ScheduledTasks -Disable

# Turn on the diagnostics tracking scheduled tasks (default value).
# ScheduledTasks -Enable

# Do not use sign-in info to automatically finish setting up device after an update.
SigninInfo -Disable

# Use sign-in info to automatically finish setting up device after an update (default value).
# SigninInfo -Enable

# Do not let websites provide locally relevant content by accessing language list.
LanguageListAccess -Disable

# Let websites provide locally relevant content by accessing language list (default value).
# LanguageListAccess -Enable

# Do not let apps show me personalized ads by using my advertising ID.
AdvertisingID -Disable

# Let apps show me personalized ads by using my advertising ID (default value).
# AdvertisingID -Enable

# Hide the Windows welcome experiences after updates and occasionally when I sign in to highlight what's new and suggested.
WindowsWelcomeExperience -Hide

# Show the Windows welcome experiences after updates and occasionally when I sign in to highlight what's new and suggested (default value).
# WindowsWelcomeExperience -Show

# Get tips and suggestions when I use Windows (default value).
# WindowsTips -Enable

# Do not get tips and suggestions when I use Windows.
WindowsTips -Disable

# Hide from me suggested content in the Settings app.
SettingsSuggestedContent -Hide

# Show me suggested content in the Settings app (default value).
# SettingsSuggestedContent -Show

# Turn off automatic installing suggested apps.
AppsSilentInstalling -Disable

# Turn on automatic installing suggested apps (default value).
# AppsSilentInstalling -Enable

# Do not suggest ways to get the most out of Windows and finish setting up this device.
WhatsNewInWindows -Disable

# Suggest ways to get the most out of Windows and finish setting up this device (default value).
# WhatsNewInWindows -Enable

# Don't let Microsoft use your diagnostic data for personalized tips, ads, and recommendations.
TailoredExperiences -Disable

# Let Microsoft use your diagnostic data for personalized tips, ads, and recommendations (default value).
# TailoredExperiences -Enable

# Disable Bing search in the Start Menu.
BingSearch -Disable

# Enable Bing search in the Start Menu (default value).
# BingSearch -Enable

# Do not show recommendations for tips, shortcuts, new apps, and more in the Start menu.
StartRecommendationsTips -Hide

# Show recommendations for tips, shortcuts, new apps, and more in the Start menu (default value).
# StartRecommendationsTips -Show

# Do not show Microsoft account-related notifications on Start Menu in the Start menu.
StartAccountNotifications -Hide

# Show Microsoft account-related notifications on Start Menu in the Start menu (default value).
# StartAccountNotifications -Show

#endregion Privacy & Telemetry


#region UI & Personalization

# Show the "This PC" icon on Desktop.
ThisPC -Show

# Hide the "This PC" icon on Desktop (default value).
# ThisPC -Hide

# Do not use item check boxes.
# CheckBoxes -Disable

# Use check item check boxes (default value).
CheckBoxes -Enable

# Show hidden files, folders, and drives.
HiddenItems -Enable

# Do not show hidden files, folders, and drives (default value).
# HiddenItems -Disable

# Show file name extensions.
FileExtensions -Show

# Hide file name extensions (default value).
# FileExtensions -Hide

# Show folder merge conflicts.
MergeConflicts -Show

# Hide folder merge conflicts (default value).
# MergeConflicts -Hide

# Open File Explorer to "This PC".
OpenFileExplorerTo -ThisPC

# Open File Explorer to Quick access (default value).
# OpenFileExplorerTo -QuickAccess

# Disable the File Explorer compact mode (default value).
# FileExplorerCompactMode -Disable

# Enable the File Explorer compact mode.
FileExplorerCompactMode -Enable

# Do not show sync provider notification within File Explorer.
OneDriveFileExplorerAd -Hide

# Show sync provider notification within File Explorer (default value).
# OneDriveFileExplorerAd -Show

# When I snap a window, do not show what I can snap next to it.
SnapAssist -Disable

# When I snap a window, show what I can snap next to it (default value).
# SnapAssist -Enable

# Show the file transfer dialog box in the detailed mode.
FileTransferDialog -Detailed

# Show the file transfer dialog box in the compact mode (default value).
# FileTransferDialog -Compact

# Display the recycle bin files delete confirmation.
RecycleBinDeleteConfirmation -Enable

# Do not display the recycle bin files delete confirmation (default value).
# RecycleBinDeleteConfirmation -Disable

# Hide recently used files in Quick access.
QuickAccessRecentFiles -Hide

# Show recently used files in Quick access (default value).
# QuickAccessRecentFiles -Show

# Hide frequently used folders in Quick access.
QuickAccessFrequentFolders -Hide

# Show frequently used folders in Quick access (default value).
# QuickAccessFrequentFolders -Show

# Set the taskbar alignment to the left.
# TaskbarAlignment -Left

# Set the taskbar alignment to the center (default value).
TaskbarAlignment -Center

# Hide the widgets icon on the taskbar.
TaskbarWidgets -Hide

# Show the widgets icon on the taskbar (default value).
# TaskbarWidgets -Show

# Hide the search on the taskbar.
# TaskbarSearch -Hide

# Show the search icon on the taskbar.
TaskbarSearch -SearchIcon

# Show the search icon and label on the taskbar.
# TaskbarSearch -SearchIconLabel

# Show the search box on the taskbar (default value).
# TaskbarSearch -SearchBox

# Hide search highlights.
SearchHighlights -Hide

# Show search highlights (default value).
# SearchHighlights -Show

# Hide Copilot button on the taskbar.
CopilotButton -Hide

# Show Copilot button on the taskbar (default value).
# CopilotButton -Show

# Hide the Task view button from the taskbar.
# TaskViewButton -Hide

# Show the Task View button on the taskbar (default value).
TaskViewButton -Show

# Show seconds on the taskbar clock.
# SecondsInSystemClock -Show

# Hide seconds on the taskbar clock (default value).
SecondsInSystemClock -Hide

# Combine taskbar buttons and always hide labels (default value).
TaskbarCombine -Always

# Combine taskbar buttons and hide labels when taskbar is full.
# TaskbarCombine -Full

# Combine taskbar buttons and never hide labels.
# TaskbarCombine -Never

# Unpin the "Microsoft Edge" and "Microsoft Store" shortcuts from the taskbar.
UnpinTaskbarShortcuts -Shortcuts Edge

# Enable end task in taskbar by right click.
TaskbarEndTask -Enable

# Disable end task in taskbar by right click (default value).
# TaskbarEndTask -Disable

# View the Control Panel icons by large icons.
# ControlPanelView -LargeIcons

# View the Control Panel icons by small icons.
ControlPanelView -SmallIcons

# View the Control Panel icons by category (default value).
# ControlPanelView -Category

# Set the default Windows mode to dark.
WindowsColorMode -Dark

# Set the default Windows mode to light (default value).
# WindowsColorMode -Light

# Set the default app mode to dark.
AppColorMode -Dark

# Set the default app mode to light (default value).
# AppColorMode -Light

# Hide first sign-in animation after the upgrade.
FirstLogonAnimation -Disable

# Show first sign-in animation after the upgrade (default value).
# FirstLogonAnimation -Enable

# Set the quality factor of the JPEG desktop wallpapers to maximum.
JPEGWallpapersQuality -Max

# Set the quality factor of the JPEG desktop wallpapers to default.
# JPEGWallpapersQuality -Default

# Do not add the "- Shortcut" suffix to the file name of created shortcuts.
ShortcutsSuffix -Disable

# Add the "- Shortcut" suffix to the file name of created shortcuts (default value).
# ShortcutsSuffix -Enable

# Use the Print screen button to open screen snipping.
PrtScnSnippingTool -Enable

# Do not use the Print screen button to open screen snipping (default value).
# PrtScnSnippingTool -Disable

# Do not use a different input method for each app window (default value).
# AppsLanguageSwitch -Disable

# Let me use a different input method for each app window.
AppsLanguageSwitch -Enable

# When I grab a windows's title bar and shake it, minimize all other windows.
AeroShaking -Enable

# When I grab a windows's title bar and shake it, don't minimize all other windows (default value).
# AeroShaking -Disable

# Set default cursors.
# Cursors -Default

# Download and install free dark "Windows 11 Cursors Concept v2" cursors from Jepri Creations.
Cursors -Dark

# Download and install free light "Windows 11 Cursors Concept v2" cursors from Jepri Creations.
# Cursors -Light

# Do not group files and folder in the Downloads folder.
FolderGroupBy -None

# Group files and folder by date modified in the Downloads folder.
# FolderGroupBy -Default

# Do not expand to open folder on navigation pane (default value).
NavigationPaneExpand -Disable

# Expand to open folder on navigation pane.
# NavigationPaneExpand -Enable

#endregion UI & Personalization


#region OneDrive

# Uninstall OneDrive. The OneDrive user folder won't be removed.
OneDrive -Uninstall

# Install OneDrive 64-bit.
# OneDrive -Install

# Install OneDrive 64-bit all users to %ProgramFiles% depending which installer is triggered.
# OneDrive -Install -AllUsers

#endregion OneDrive


#region System

# Turn on Storage Sense.
StorageSense -Enable

# Turn off Storage Sense (default value).
# StorageSense -Disable

# Run Storage Sense every month.
StorageSenseFrequency -Month

# Run Storage Sense during low free disk space (default value).
# StorageSenseFrequency -Default

# Turn on automatic cleaning up temporary system and app files (default value).
StorageSenseTempFiles -Enable

# Turn off automatic cleaning up temporary system and app files.
# StorageSenseTempFiles -Disable

# Disable hibernation. It isn't recommended to turn off for laptops.
Hibernation -Disable

# Enable hibernate (default value).
# Hibernation -Enable

# Disable the Windows 260 characters path limit.
Win32LongPathLimit -Disable

# Enable the Windows 260 character path limit (default value).
# Win32LongPathLimit -Enable

# Display Stop error code when BSoD occurs.
BSoDStopError -Enable

# Do not display stop error code when BSoD occurs (default value).
# BSoDStopError -Disable

# Choose when to be notified about changes to your computer: never notify.
AdminApprovalMode -Never

# Choose when to be notified about changes to your computer: notify me only when apps try to make changes to my computer (default value).
# AdminApprovalMode -Default

# Turn on access to mapped drives from app running with elevated permissions with Admin Approval Mode enabled.
MappedDrivesAppElevatedAccess -Enable

# Turn off access to mapped drives from app running with elevated permissions with Admin Approval Mode enabled (default value).
# MappedDrivesAppElevatedAccess -Disable

# Turn off Delivery Optimization.
DeliveryOptimization -Disable

# Turn on Delivery Optimization (default value).
# DeliveryOptimization -Enable

# Do not let Windows manage my default printer.
WindowsManageDefaultPrinter -Disable

# Let Windows manage my default printer (default value).
# WindowsManageDefaultPrinter -Enable

# Disable the Windows features using the pop-up dialog box.
WindowsFeatures -Disable

# Enable the Windows features using the pop-up dialog box.
# WindowsFeatures -Enable

# Uninstall optional features using the pop-up dialog box.
WindowsCapabilities -Uninstall

# Install optional features using the pop-up dialog box.
# WindowsCapabilities -Install

# Receive updates for other Microsoft products when you update Windows.
UpdateMicrosoftProducts -Enable

# Do not receive updates for other Microsoft products (default value).
# UpdateMicrosoftProducts -Disable

# Notify me when a restart is required to finish updating.
RestartNotification -Show

# Do not notify me when a restart is required to finish updating (default value).
# RestartNotification -Hide

# Restart as soon as possible to finish updating.
RestartDeviceAfterUpdate -Enable

# Don't restart as soon as possible to finish updating (default value).
# RestartDeviceAfterUpdate -Disable

# Automatically adjust active hours for me based on daily usage.
ActiveHours -Automatically

# Manually adjust active hours for me based on daily usage (default value).
# ActiveHours -Manually

# Do not get the latest updates as soon as they're available (default value).
WindowsLatestUpdate -Disable

# Get the latest updates as soon as they're available.
# WindowsLatestUpdate -Enable

# Set power plan on "High performance". It isn't recommended to turn on for laptops.
PowerPlan -High

# Set power plan on "Balanced" (default value).
# PowerPlan -Balanced

# Do not allow the computer to turn off the network adapters to save power. It isn't recommended to turn off for laptops.
NetworkAdaptersSavePower -Disable

# Allow the computer to turn off the network adapters to save power (default value).
# NetworkAdaptersSavePower -Enable

# Override for default input method: English.
InputMethod -English

# Override for default input method: use language list (default value).
# InputMethod -Default

# Change user folders location to the root of any drive using the interactive menu. User files or folders won't be moved to a new location. Move them manually. They're located in the %USERPROFILE% folder by default.
Set-UserShellFolderLocation -Root

# Select folders for user folders location manually using a folder browser dialog. User files or folders won't be moved to a new location. Move them manually. They're located in the %USERPROFILE% folder by default.
# Set-UserShellFolderLocation -Custom

# Change user folders location to the default values. User files or folders won't be moved to a new location. Move them manually. They're located in the %USERPROFILE% folder by default (default value).
# Set-UserShellFolderLocation -Default

# Use the latest installed .NET runtime for all apps.
LatestInstalled.NET -Enable

# Do not use the latest installed .NET runtime for all apps (default value).
# LatestInstalled.NET -Disable

# Save screenshots by pressing Win+PrtScr on the Desktop. The function will be applied only if the preset is configured to remove OneDrive. Otherwise the backup functionality for the "Desktop" and "Pictures" folders in OneDrive breaks.
WinPrtScrFolder -Desktop

# Save screenshots by pressing Win+PrtScr in the Pictures folder (default value).
# WinPrtScrFolder -Default

# Run troubleshooter automatically, then notify. In order this feature to work the OS level of diagnostic data gathering will be set to "Optional diagnostic data" and the error reporting feature will be turned on.
RecommendedTroubleshooting -Automatically

# Ask me before running troubleshooters. In order this feature to work the OS level of diagnostic data gathering will be set to "Optional diagnostic data" and the error reporting feature will be turned on (default value).
# RecommendedTroubleshooting -Default

# Launch folder windows in a separate process.
FoldersLaunchSeparateProcess -Enable

# Do not launch folder windows in a separate process (default value).
# FoldersLaunchSeparateProcess -Disable

# Disable and delete reserved storage after the next update installation.
ReservedStorage -Disable

# Enable reserved storage (default value).
# ReservedStorage -Enable

# Disable help lookup via F1.
F1HelpPage -Disable

# Enable help lookup via F1 (default value).
# F1HelpPage -Enable

# Enable Num Lock at startup.
NumLock -Enable

# Disable Num Lock at startup (default value).
# NumLock -Disable

# Disable Caps Lock.
CapsLock -Disable

# Enable Caps Lock (default value).
# CapsLock -Enable

# Turn off pressing the Shift key 5 times to turn Sticky keys.
StickyShift -Disable

# Turn on pressing the Shift key 5 times to turn Sticky keys (default value).
# StickyShift -Enable

# Don't use AutoPlay for all media and devices.
Autoplay -Disable

# Use AutoPlay for all media and devices (default value).
# Autoplay -Enable

# Disable thumbnail cache removal.
ThumbnailCacheRemoval -Disable

# Enable thumbnail cache removal (default value).
# ThumbnailCacheRemoval -Enable

# Automatically saving my restartable apps and restart them when I sign back in.
SaveRestartableApps -Enable

# Turn off automatically saving my restartable apps and restart them when I sign back in (default value).
# SaveRestartableApps -Disable

# Enable "Network Discovery" and "File and Printers Sharing" for workgroup networks.
NetworkDiscovery -Enable

# Disable "Network Discovery" and "File and Printers Sharing" for workgroup networks (default value).
# NetworkDiscovery -Disable

InstallDotNetRuntimes -Runtimes NET6x64, NET8x6
# Register app, calculate hash, and associate with an extension with the 'How do you want to open this' pop-up hidden.
# Set-Association

# Export all Windows associations into Application_Associations.json file to script root folder.
# Export-Associations

# Import all Windows associations from an Application_Associations.json file. You need to install all apps according to an exported Application_Associations.json file to restore all associations.
# Import-Associations

# Set Windows Terminal as default terminal app to host the user interface for command-line applications.
DefaultTerminalApp -WindowsTerminal

# Set Windows Console Host as default terminal app to host the user interface for command-line applications (default value).
# DefaultTerminalApp -ConsoleHost

# Install the latest Microsoft Visual C++ Redistributable Packages 2015–2022 (x86/x64).
InstallVCRedist

# List Microsoft Edge channels to prevent desktop shortcut creation upon its' update.
PreventEdgeShortcutCreation -Channels Stable, Beta, Dev, Canary


# Enable proxying only blocked sites from the unified registry of Roskomnadzor. The function is applicable for Russia only.
RKNBypass -Enable

# Disable proxying only blocked sites from the unified registry of Roskomnadzor (default value).
# RKNBypass -Disable

# Do not prevent desktop shortcut creation upon Microsoft Edge update (default value).
# PreventEdgeShortcutCreation -Disable

# Prevent all internal SATA drives from showing up as removable media in the taskbar notification area.
SATADrivesRemovableMedia -Disable

# Show up all internal SATA drives as removeable media in the taskbar notification area (default value).
# SATADrivesRemovableMedia -Default

# Back up the system registry to %SystemRoot%\System32\config\RegBack folder when PC restarts and create a RegIdleBackup in the Task Scheduler task to manage subsequent backups.
# RegistryBackup -Enable

# Do not back up the system registry to %SystemRoot%\System32\config\RegBack folder (default value).
# RegistryBackup -Disable

#endregion System


#region WSL

# Enable Windows Subsystem for Linux (WSL), install the latest WSL Linux kernel version, and a Linux distribution using a pop-up form. The "Receive updates for other Microsoft products" setting will enabled automatically to receive kernel updates.
# Install-WSL

#endregion WSL


#region Start menu

# Show default Start layout (default value).
# StartLayout -Default

# Show more pins on Start.
StartLayout -ShowMorePins

# Show more recommendations on Start.
# StartLayout -ShowMoreRecommendations

#endregion Start menu


#region UWP apps

# Uninstall UWP apps using the pop-up dialog box.
UninstallUWPApps

# Uninstall UWP apps using the pop-up dialog box. If the "For all users" is checked apps packages will not be installed for new users. The "ForAllUsers" argument sets a checkbox to unistall packages for all users.
# UninstallUWPApps -ForAllUsers

# Disable Cortana autostarting.
CortanaAutostart -Disable

# Enable Cortana autostarting (default value).
# CortanaAutostart -Enable

# Disable Microsoft Teams autostarting.
TeamsAutostart -Disable

# Enable Microsoft Teams autostarting (default value).
# TeamsAutostart -Enable

#endregion UWP apps


#region Gaming

# Disable Xbox Game Bar. To prevent popping up the "You'll need a new app to open this ms-gamingoverlay" warning, you need to disable the Xbox Game Bar app, even if you uninstalled it before.
XboxGameBar -Disable

# Enable Xbox Game Bar (default value).
# XboxGameBar -Enable

# Disable Xbox Game Bar tips.
XboxGameTips -Disable

# Enable Xbox Game Bar tips (default value).
# XboxGameTips -Enable

# Choose an app and set the "High performance" graphics performance for it. Only if you have a dedicated GPU.
Set-AppGraphicsPerformance

# Turn on hardware-accelerated GPU scheduling. Restart needed. Only if you have a dedicated GPU and WDDM verion is 2.7 or higher.
GPUScheduling -Enable

# Turn off hardware-accelerated GPU scheduling. Restart needed (default value).
# GPUScheduling -Disable

#endregion Gaming


#region Scheduled tasks

# Create "Windows Cleanup" (main task) and "Windows Cleanup Notification" (task to generate a pop-up notification) tasks to clean up unused files and Windows updates in the Task Scheduler in the Sophia folder. A native notification prompting you to run the task will pop up before the cleanup begins. The task runs every 30 days. Windows Script Host must be enabled for the task to run.
CleanupTask -Register

# Delete the "Windows Cleanup" and "Windows Cleanup Notification" scheduled tasks for cleaning up Windows unused files and updates.
# CleanupTask -Delete

# Create a "SoftwareDistribution" task to clean up the %SystemRoot%\SoftwareDistribution\Download folder where the installation files for all Windows updates are downloaded, in the Sophia folder in the  Task Scheduler. The task will wait until the Windows Update service has finished running. The task runs every 90 days. Windows Script Host must be enabled for the task to run.
SoftwareDistributionTask -Register

# Delete the "SoftwareDistribution" scheduled task for cleaning up the %SystemRoot%\SoftwareDistribution\Download folder.
# SoftwareDistributionTask -Delete

# Create a "Temp" task in the Task Scheduler to clean up the %TEMP% folder. Only files older than one day will be deleted. The task runs every 60 days. Windows Script Host must be enabled for the task to run.
TempTask -Register

# Delete the "Temp" scheduled task for cleaning up the %TEMP% folder.
# TempTask -Delete

#endregion Scheduled tasks


#region Microsoft Defender & Security

# Enable Microsoft Defender Exploit Guard network protection.
NetworkProtection -Enable

# Disable Microsoft Defender Exploit Guard network protection (default value).
# NetworkProtection -Disable

# Enable detection for potentially unwanted applications and block them.
PUAppsDetection -Enable

# Disable detection for potentially unwanted applications and block them (default value).
# PUAppsDetection -Disable

# Enable sandboxing for Microsoft Defender.
DefenderSandbox -Enable

# Disable sandboxing for Microsoft Defender (default value).
# DefenderSandbox -Disable

# Dismiss Microsoft Defender offer in the Windows Security about signing in Microsoft account.
DismissMSAccount

# Dismiss Microsoft Defender offer in the Windows Security about turning on the SmartScreen filter for Microsoft Edge.
DismissSmartScreenFilter

# Create the "Process Creation" сustom view in the Event Viewer to log executed processes and their arguments.
EventViewerCustomView -Enable

# Remove the "Process Creation" custom view in the Event Viewer to log executed processes and their arguments (default value).
# EventViewerCustomView -Disable

# Enable logging for all Windows PowerShell modules.
PowerShellModulesLogging -Enable

# Disable logging for all Windows PowerShell modules (default value).
# PowerShellModulesLogging -Disable

# Enable logging for all PowerShell scripts input to the Windows PowerShell event log.
PowerShellScriptsLogging -Enable

# Disable logging for all PowerShell scripts input to the Windows PowerShell event log (default value).
# PowerShellScriptsLogging -Disable

# Microsoft Defender SmartScreen doesn't marks downloaded files from the Internet as unsafe.
AppsSmartScreen -Disable

# Microsoft Defender SmartScreen marks downloaded files from the Internet as unsafe (default value).
# AppsSmartScreen -Enable

# Disable the Attachment Manager marking files that have been downloaded from the Internet as unsafe.
SaveZoneInformation -Disable

# Enable the Attachment Manager marking files that have been downloaded from the Internet as unsafe (default value).
# SaveZoneInformation -Enable

# Disable Windows Script Host. Blocks WSH from executing .js and .vbs files.
# WindowsScriptHost -Disable

# Enable Windows Script Host (default value).
# WindowsScriptHost -Enable

# Enable Windows Sandbox.
# WindowsSandbox -Enable

# Disable Windows Sandbox (default value).
# WindowsSandbox -Disable

# Enable DNS-over-HTTPS for IPv4. The valid IPv4 addresses: 1.0.0.1, 1.1.1.1, 149.112.112.112, 8.8.4.4, 8.8.8.8, 9.9.9.9.
DNSoverHTTPS -Enable -PrimaryDNS 1.0.0.1 -SecondaryDNS 1.1.1.1

# Disable DNS-over-HTTPS for IPv4 (default value).
# DNSoverHTTPS -Disable

# Enable Local Security Authority protection to prevent code injection without UEFI lock.
# LocalSecurityAuthority -Enable

# Disable Local Security Authority protection without UEFI lock (default value).
# LocalSecurityAuthority -Disable

#endregion Microsoft Defender & Security


#region Context menu

# Show the "Extract all" item in the Windows Installer (.msi) context menu.
MSIExtractContext -Show

# Hide the "Extract all" item from the Windows Installer (.msi) context menu (default value).
# MSIExtractContext -Hide

# Show the "Install" item in the Cabinet (.cab) filenames extensions context menu.
CABInstallContext -Show

# Hide the "Install" item from the Cabinet (.cab) filenames extensions context menu (default value).
# CABInstallContext -Hide

# Hide the "Edit with Clipchamp" item from the media files context menu.
EditWithClipchampContext -Hide

# Show the "Edit with Clipchamp" item in the media files context menu (default value).
# EditWithClipchampContext -Show

# Hide the "Edit with Photos" item from the media files context menu.
EditWithPhotosContext -Hide

# Show the "Edit with Photos" item in the media files context menu (default value).
# EditWithPhotosContext -Show

# Hide the "Print" item from the .bat and .cmd context menu.
PrintCMDContext -Hide

# Show the "Print" item in the .bat and .cmd context menu (default value).
# PrintCMDContext -Show

# Hide the "Compressed (zipped) Folder" item from the "New" context menu.
CompressedFolderNewContext -Hide

# Show the "Compressed (zipped) Folder" item to the "New" context menu (default value).
# CompressedFolderNewContext -Show

# Enable the "Open", "Print", and "Edit" context menu items for more than 15 items selected.
MultipleInvokeContext -Enable

# Disable the "Open", "Print", and "Edit" context menu items for more than 15 items selected (default value).
# MultipleInvokeContext -Disable

# Hide the "Look for an app in the Microsoft Store" item in the "Open with" dialog.
UseStoreOpenWith -Hide

# Show the "Look for an app in the Microsoft Store" item in the "Open with" dialog (default value).
# UseStoreOpenWith -Show

# Show the "Open in Windows Terminal" item in the folders context menu (default value).
OpenWindowsTerminalContext -Show

# Hide the "Open in Windows Terminal" item in the folders context menu.
# OpenWindowsTerminalContext -Hide

# Open Windows Terminal in context menu as administrator by default.
OpenWindowsTerminalAdminContext -Enable

# Do not open Windows Terminal in context menu as administrator by default (default value).
# OpenWindowsTerminalAdminContext -Disable

#endregion Context menu


#region Update Policies

# Display all policy registry keys (even manually created ones) in the Local Group Policy Editor snap-in (gpedit.msc). This can take up to 30 minutes, depending on the number of policies created in the registry and your system resources.
# UpdateLGPEPolicies

#endregion Update Policies


PostActions
Errors