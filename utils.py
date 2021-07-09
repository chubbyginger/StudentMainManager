#!/usr/bin/env python3

import os
import configparser

if os.path.isfile('config.ini'):
    configFile = open('config.ini')
    parser = configparser.ConfigParser()
    parser.read('config.ini')
else:
    configFile = open('config.ini', 'w')
    configFile.write('[JiYu]\n')
    configFile.write('pathToJiYu=C:\\\\Program Files\\\\TopDomain\\\\e-Learning Class\\\\')
    configFile.close()

def getConfigExist():
    return os.path.isfile('config.ini')

def getPathFromCfg():
    JiYuPath = parser.get('JiYu', 'pathToJiYu')
    return JiYuPath

# Here are the checking functions
def checkNTSD():
    return os.path.isfile('./binaries/ntsd.exe')

def checkPsSuspend():
    return os.path.isfile('./binaries/pssuspend.exe')

def checkJiYuTrainer():
    return os.path.isfile('./binaries/JiYuTrainer/JiYuTrainer.exe')

def checkUpdater():
    return os.path.isfile('./AutoUpdate.exe')


def NTSDKill():
    os.system('.\\binaries\\ntsd.exe -c q -pn StudentMain.exe')

def suspend():
    os.system('.\\binaries\\pssuspend.exe StudentMain.exe')

def trashJiYu(JiYuPath):
    os.rmdir(JiYuPath)
