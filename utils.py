#!/usr/bin/env python3

import os
import configparser

defaultConfigFile = '[JiYu]\n'
defaultConfigFile += 'pathToJiYu=C:\\\\Program Files\\\\TopDomain\\\\e-Learning Class\\\\\n'
defaultConfigFile += '\n'
defaultConfigFile += '[utilities]\n'
defaultConfigFile += 'ntsdPath=.\\\\binaries\\\\ntsd.exe\n'
defaultConfigFile += 'suspenderPath=.\\\\binaries\\\\pssuspend.exe\n'
defaultConfigFile += 'jiYuTrainerPath=.\\\\binaries\\\\JiYuTrainer\\\\JiYuTrainer.exe\n'
defaultConfigFile += '\n'
defaultConfigFile += '[Misc]\n'
defaultConfigFile += 'autoUpdate=1'

if os.path.isfile('config.ini'):
    configFile = open('config.ini')
    parser = configparser.ConfigParser()
    parser.read('config.ini')
else:
    configFile = open('config.ini', 'w')
    configFile.write(defaultConfigFile)
    configFile.close()
    parser = configparser.ConfigParser()
    parser.read('config.ini')

jiYuPath = parser.get('JiYu', 'pathToJiYu')
ntsdPath = parser.get('utilities', 'ntsdPath')
suspenderPath = parser.get('utilities', 'suspenderPath')

def NTSDKill():
    if os.path.isfile(ntsdPath):
        os.system('.\\binaries\\ntsd.exe -c q -pn StudentMain.exe')
        return 0
    else:
        return 1

def suspend():
    if os.path.isfile(suspenderPath):
        if 'suspended' in os.popen(suspenderPath + ' StudentMain.exe'):
             return 0
        else:
            return 1
    else:
        return -1

def trashJiYu():
    if os.path.isdir(jiYuPath):
        os.rmdir(jiYuPath)
        return 0
    else:
        return 1
