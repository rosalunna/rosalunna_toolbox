# Re-run this script hidden using Start-Process if not already hidden
if ($MyInvocation.WindowHandle -ne [System.IntPtr]::Zero) {
    Start-Process powershell -ArgumentList "-WindowStyle Hidden -File `"$PSCommandPath`"" -Verb RunAs
    exit
}
Rammap -E0 -Et
