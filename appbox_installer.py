#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import importlib
import appbox_modules
from appbox_modules import *
import subprocess

try:
    import consolemenu as cm
except ImportError:
    print('Trying to Install required module: console-menu\n')
    os.system('python -m pip install console-menu')
finally:
    import consolemenu as cm

# -- above lines try to install console-menu module if not present
# -- if all went well, import required module again (for global access)


def exitScript(code: int = 1, message: str = ''):
    if len(message) > 0 and code == 1:
        sys.exit(message)
    elif len(message) > 0:
        print(message)
    sys.exit(code)


options = ['Yes', 'No']

selection = cm.SelectionMenu.get_selection(options, 'Appbox Installer',
                                           'Is it okay if we try to update the system before we continue?')

if selection >= len(options):
    exitScript(0)

if selection == 0:  # 'Yes'
    os.system('sudo apt update && sudo apt upgrade')



program_list = appbox_modules.__all__

selection = cm.SelectionMenu.get_selection(program_list, 'Appbox Installer',
                                           'Choose a program to install:')

if selection >= len(appbox_modules.__all__):
    sys.exit()

current_application = getattr(importlib.import_module('appbox_modules'), program_list[selection]).program()

# print(current_application.getDownloadUrl())
