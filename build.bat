@echo off
title StudentMain Manager build
echo StudentMain Manager builder
echo ===========================
echo.
echo Please choose if you want a console for debugging.
echo 1: Console mode
echo 2: Window mode
echo.
choice /c 12 /m "Press 1 or 2 on the keyboard..."

if %errorlevel%==1 goto consolebuild
if %errorlevel%==2 goto windowbuild

:consolebuild
echo.
echo Starting console build.
echo Copying source files.
mkdir build
copy main.py .\build
copy utils.py .\build
echo.
echo Would you like UPX compressing?
echo Y. Yes
echo N. No
choice /c YN /m "Press Y or N on the keyboard..."

if %errorlevel%==1 goto consoleupxbuild
if %errorlevel%==2 goto consolenoupxbuild

:consoleupxbuild
echo.
set /p upxPath=Please specify the path to the UPX binary: 
cd build
echo.
echo Building with PyInstaller...
echo.
pyinstaller --onefile --upx-dir="%upxPath%" -c --icon ..\image-res\StudentMainManager.ico main.py
echo.
goto mkrelease

:consolenoupxbuild
echo.
cd build
echo.
echo Building with PyInstaller...
echo.
pyinstaller --onefile -c --icon ..\image-res\StudentMainManager.ico main.py
echo.
goto mkrelease

:windowbuild
echo.
echo Starting window build.
echo Copying source files.
mkdir build
copy main.py .\build
copy utils.py .\build
echo.
echo Would you like UPX compressing?
echo Y. Yes
echo N. No
choice /c YN /m "Press Y or N on the keyboard..."

if %errorlevel%==1 goto windowupxbuild
if %errorlevel%==2 goto windownoupxbuild

:windowupxbuild
echo.
set /p upxPath=Please specify the path to the UPX binary: 
cd build
echo.
echo Building with PyInstaller...
echo.
pyinstaller --onefile --upx-dir="%upxPath%" -w --icon ..\image-res\StudentMainManager.ico main.py
echo.
goto mkrelease

:windownoupxbuild
echo.
cd build
echo.
echo Building with PyInstaller...
echo.
pyinstaller --onefile -w --icon ..\image-res\StudentMainManager.ico main.py
echo.
goto mkrelease

:mkrelease
echo Making release.
echo Copying files.
mkdir release
copy .\dist\main.exe .\release\StudentMainManager.exe
copy ..\config.ini .\release\config.ini
echo Please manually press D twice below.
xcopy /e ..\binaries .\release\binaries
xcopy /e ..\image-res .\release\image-res
echo.
echo Release build complete. Removing rubbish files...
echo.
rmdir .\build /s /q
rmdir .\dist /s /q
rmdir .\__pycache__ /s /q
del .\main.py /f /q
del .\main.spec /f /q
del .\utils.py /f /q
echo Build complete. The builded release can be found under .\build\release. Press any key to exit.
pause >nul