@echo off
REM Wait 15 seconds for Windows and audio drivers to initialize
timeout /t 15 /nobreak >nul

REM Run your Python script silently with pythonw (no console window)
start "" "C:\Users\User\AppData\Local\Microsoft\WindowsApps\pythonw.exe" "C:\Users\User\OneDrive\Attachments\Documents\welcome.py"

exit



