import sys
import os
import os.path
import shutil
from datetime import datetime
import pathlib

# creates a file called 'backup.log'
backupLog = open('backup.log', 'a')
backupLog.write("\n" + datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + "Backup script ran." + "\n")

if not os.path.exists("backupcfg.py"):
    backupLog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + "Backup canceled: Couldn't find 'backupcfg.py'. make sure it is in the same folder as 'backup.py'." + "\n")
    print("Backup canceled: Couldn't find 'backupcfg.py'. make sure it is in the same folder as 'backup.py'.")
    exit()

from backupcfg import *


backupComplete = True

def writeToLog(message, write):
    backupLog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + message + "\n")
    if write == True and writeToConsole == True:
        print(message)





    

# checks if there is a given argument, and if it matches with a job name described in 'backupcfg.py'. if not, then an error will be given and the script stops
if len(sys.argv) < 2:
    print("Usage: python backup.py <job>")
    writeToLog("Backup canceled: No argument given.", False)
    backupComplete = False

elif not sys.argv[1] in jobs:
    print("No such job exists.")
    writeToLog("Backup canceled: Argument given did not match job in 'backupcfg.py'.", False)
    backupComplete = False

else:
    
    for n in jobs[sys.argv[1]]:
        target = backupDir + "/" + datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + pathlib.PurePath(n).name
        
        if os.path.exists(backupDir) and os.path.exists(n):
        
            if os.path.isdir(n) == False:
                shutil.copyfile(n, target)
                writeToLog(pathlib.PurePath(n).name + " was copied to %s."%(backupDir), True)
            
            else:
                shutil.copytree(n, target)
                writeToLog(pathlib.PurePath(n).name + " and its contents were copied to %s."%(backupDir), True)
        
        elif os.path.exists(n):
        
            if os.path.isdir(n) == False:
                os.mkdir(backupDir)
                writeToLog("'%s' was created."%(backupDir), True)
                shutil.copyfile(n, target)
                writeToLog(pathlib.PurePath(n).name + " was copied to %s."%(backupDir), True)
                
            else:
                shutil.copytree(n, target)
                writeToLog(pathlib.PurePath(n).name + " and its contents were copied to %s."%(backupDir), True)
        
        else:
        
            writeToLog("File skipped: '%s' does not exist."%(n), True)
            
        
    
if backupComplete != False:
    writeToLog("Finished backup.", False)
    print("Backup complete!")