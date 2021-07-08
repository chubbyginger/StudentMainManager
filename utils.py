#!/usr/bin/env python3

import os
import configparser

def checkNTSD():
    return os.path.isfile('./binaries/ntsd.exe')

def checkPsSuspend():
    return os.path.isfile('./binaries/pssuspend.exe')

def checkJiYuTrainer():
    return os.path.isfile('./binaries/JiYuTrainer/JiYuTrainer.exe')

def checkUpdater():
    return os.path.isfile('./AutoUpdate.exe')