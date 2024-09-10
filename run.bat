@echo off
set "NEW_PATH=D:\comd\"

setx PATH "%PATH%;%NEW_PATH%"

echo The directory %NEW_PATH% has been added to the PATH permanently.
pause
