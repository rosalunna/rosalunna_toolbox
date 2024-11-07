# Import required Windows API functions
Add-Type @"
    using System;
    using System.Runtime.InteropServices;
    public class Win32 {
        [DllImport("kernel32.dll")]
        public static extern IntPtr GetConsoleWindow();

        [DllImport("user32.dll")]
        public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
        
        public const int SW_HIDE = 0;
    }
"@

# Immediately hide the window
$consolePtr = [Win32]::GetConsoleWindow()
[Win32]::ShowWindow($consolePtr, [Win32]::SW_HIDE)

# Run Rammap with hidden window
$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = "Rammap"
$psi.Arguments = "-E0 -Et"
$psi.UseShellExecute = $false
$psi.CreateNoWindow = $true
$psi.WindowStyle = [System.Diagnostics.ProcessWindowStyle]::Hidden
$proc = [System.Diagnostics.Process]::Start($psi)
$proc.WaitForExit()
