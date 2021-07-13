@echo off
echo Building StudentMain Manager release.
echo.
if not exist .\build mkdir build

echo Copying files.
copy main.pyw .\build\main.pyw

echo Packing with PyInstaller. Please be sure PyInstaller is installed.
cd build
pyinstaller -F --onefile main.pyw

echo Removing rubbish files.
del .\build\*.* /f /s /q
rd .\build /s /q
del .\__pycache__\*.* /f /s /q
rd .\__pycache__ /s /q

echo Creating release.
mkdir release
copy .\dist\main.exe .\release\StudentMainManager.exe
copy ..\config.ini .\release\config.ini
xcopy ..\binaries .\release\binaries

echo Release creation completed. The release files are in the build/release folder.
echo.
echo Any key to exit.
pause >nul
