@echo off
echo "download python file"
@REM powershell -Command "pip install 'python-socketio[asyncio_client]'"
@REM powershell -Command "pip install pyautogui"
@REM @REM powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/shouaya/sg-client/main/monitor.py -OutFile monitor.py"

@REM https://stackoverflow.com/questions/3057576/how-to-launch-an-application-from-a-browser

echo "excute python file"
python ./monitor.py

pause