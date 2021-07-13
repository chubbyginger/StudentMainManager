@echo off
if not exist .\build mkdir build
pyinstaller -F --onefile main.pyw