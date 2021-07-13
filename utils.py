#!/usr/bin/env python3
# StudentMain Manager main functions are put here.

import os
import shutil
import configparser
import winreg

# Default config file.
defaultConfigFile = '[JiYu]\n'
defaultConfigFile += 'pathToJiYu=C:\\\\Program Files\\\\TopDomain\\\\e-Learning Class\\\\\n'
defaultConfigFile += '\n'
defaultConfigFile += '[utilities]\n'
defaultConfigFile += 'ntsdPath=.\\\\binaries\\\\ntsd.exe\n'
defaultConfigFile += 'suspenderPath=.\\\\binaries\\\\pssuspend.exe\n'
defaultConfigFile += 'jiYuTrainerPath=.\\\\binaries\\\\JiYuTrainer\\\\JiYuTrainer.exe\n'
defaultConfigFile += '\n'
defaultConfigFile += '[Misc]\n'
defaultConfigFile += 'stayOnTop=1'

# Check if config file exists.
if os.path.isfile('config.ini'):
    # Open the config file.
    configFile = open('config.ini')
else:
    # Create the config file.
    configFile = open('config.ini', 'w')
    configFile.write(defaultConfigFile)
    configFile.close()

# Attach the parser to the config file.
parser = configparser.ConfigParser()
parser.read('config.ini')

# Get the information from the parser.
jiYuPath = parser.get('JiYu', 'pathToJiYu')
ntsdPath = parser.get('utilities', 'ntsdPath')
suspenderPath = parser.get('utilities', 'suspenderPath')
trainerPath = parser.get('utilities', 'trainerPath')
patchedSethcPath = parser.get('utilities', 'patchedSethcPath')
if parser.get('Misc', 'stayOnTop') == '0':
    winOnTop = False
else:
    winOnTop = True

# Kill JiYu with NTSD.
def NTSDKill():
    if os.path.isfile(ntsdPath):
        os.popen('.\\binaries\\ntsd.exe -c q -pn StudentMain.exe')
        return 0
    else:
        return 1

# Suspend JiYu with PsSuspend.
def suspend():
    if os.path.isfile(suspenderPath):
        if 'suspended' in os.popen(suspenderPath + ' StudentMain.exe'):
             return 0
        else:
            return 1
    else:
        return -1

# Trash JiYu by removing the install directory.
def trashJiYu():
    if os.path.isdir(jiYuPath):
        os.rmdir(jiYuPath)
        return 0
    else:
        return 1

# Launch a fullscreened IE.
def fullscreenIE():
    os.popen('cmd /c "start iexplore.exe -k"')

# Get the password from the registry.
def readPassword():
    try:
        handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\\TopDomain\\e-Learning Class Standard\\1.00')
        passString, regType = winreg.QueryValueEx(handle, 'UninstallPasswd')
        password = passString[7:-1]
        return password
    except WindowsError:
        return None

# Replace C:\Windows\System32\sethc.exe with a patched one.
def replaceSethc():
    env = os.environ
    windir = env['windir']
    try:
        os.rename(windir + '\\System32\\sethc.exe', windir + '\\System32\\sethc_bak.exe')
        shutil.copy('.\\binaries\\PSethc.exe', windir + '\\System32\\sethc.exe')
        return 0
    except PermissionError:
        return 1

# Restore the patched sethc.
def restoreSethc():
    env = os.environ
    windir = env['windir']
    try:
        os.remove(windir + '\\System32\\sethc.exe')
        os.rename(windir + '\\System32\\sethc_bak.exe', windir + '\\System32\\sethc.exe')
        return 0
    except PermissionError:
        return 1

# Launch JiYuTrainer.
def launchTrainer():
    if os.path.isfile(trainerPath):
        os.system(trainerPath)
        return 0
    else:
        return 1

# Launch JiYu.
def launchJiYu():
    if os.path.isfile(jiYuPath):
        os.system(jiYuPath + 'StudentMain.exe')
        return 0
    else:
        return 1

# Resume JiYu with PsSuspend.
def resume():
    if os.path.isfile(suspenderPath):
        if 'suspended' in os.popen(suspenderPath + ' -r StudentMain.exe'):
            return 0
        else:
            return 1
    else:
        return -1

# Write config file.
def writeConfig(newPath, newWindowOnTop):
    parser.set('JiYu', 'pathToJiYu', newPath)
    if newWindowOnTop:
        parser.set('Misc', 'stayOnTop', '1')
    else:
        parser.set('Misc', 'stayOnTop', '0')
    with open('config.ini', 'w+') as file:
        parser.write(file)
