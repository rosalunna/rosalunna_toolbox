# Run once with elevated privileges if needed
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell -ArgumentList "-WindowStyle Hidden -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

# Run the RAM cleanup command once
Rammap -E0 -Et
