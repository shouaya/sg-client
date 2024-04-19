@echo off
echo "download python file"
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/shouaya/sg-client/main/monitor.py -OutFile monitor.py"

echo "excute python file"
python ./monitor.py

pause