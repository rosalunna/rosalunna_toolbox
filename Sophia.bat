@echo off
set "baseDir=%USERPROFILE%\Sophia.Script"

rem Finds the most recent folder in the baseDir and sets it to the scriptPath variable
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    " $latestDir = Get-ChildItem -Path '%baseDir%' -Directory | Sort-Object LastWriteTime -Descending | Select-Object -First 1;" ^
    " $scriptPath = Join-Path $latestDir.FullName 'Sophia.ps1';" ^
    " Start-Process powershell -ArgumentList '-ExecutionPolicy Bypass -NoExit -File', $scriptPath"
