@echo off
del .\__pycache__\*.* /f /s /q
del .\ui\__pycache__\*.* /f /s /q
rd .\__pycache__ /s /q
rd .\ui\__pycache /s /q