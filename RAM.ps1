# Hide the PowerShell window immediately
$windowHandle = (Get-Process -Id $PID).MainWindowHandle
Add-Type -Name Window -Namespace Console -MemberDefinition '
[DllImport("Kernel32.dll")] 
public static extern IntPtr GetConsoleWindow();
[DllImport("user32.dll")]
public static extern bool ShowWindow(IntPtr hWnd, Int32 nCmdShow);
'
[Console.Window]::ShowWindow([Console.Window]::GetConsoleWindow(), 0)

# Check for admin rights silently
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell -ArgumentList "-WindowStyle Hidden -NoProfile -NonInteractive -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs -WindowStyle Hidden
    exit
}

# Run Rammap silently
$pinfo = New-Object System.Diagnostics.ProcessStartInfo
$pinfo.FileName = "Rammap"
$pinfo.Arguments = "-E0 -Et"
$pinfo.CreateNoWindow = $true
$pinfo.UseShellExecute = $false
$pinfo.WindowStyle = [System.Diagnostics.ProcessWindowStyle]::Hidden
$process = New-Object System.Diagnostics.Process
$process.StartInfo = $pinfo
$process.Start() | Out-Null
$process.WaitForExit()
