# Check for admin rights silently
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell -ArgumentList "-WindowStyle Hidden -NoProfile -NonInteractive -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs -WindowStyle Hidden
    exit
}

# Run the RAM cleanup command silently
Start-Process Rammap -ArgumentList "-E0 -Et" -WindowStyle Hidden -Wait
