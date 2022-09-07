# creates a file called 'backup.log'
backupLog = open('backup.log', 'a')

# tries to import libraries. if it fails, it will show a custom error and write to log, then end the script
try:
    import sys
    import os
    import os.path
    import shutil
    from datetime import datetime
    import pathlib
except:
    backupLog.write("\n" + datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + "Backup Canceled: Library import failed." + "\n")
    print("Backup canceled: Library import failed.")
    exit()


backupLog.write("\n" + datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + "Backup script ran." + "\n")


#checks if the config file exists. if it doesn't, it will attempt to retrieve it from github

if not os.path.exists("backupcfg.py"):
    cfgUrl = "https://raw.githubusercontent.com/30023344/Backup-Script/8f964dfeddf6128b5fa482f8031e925d59e19f38/backupcfg.py?token=GHSAT0AAAAAABYMOCIT7AWR27WYPWFC7EIYYYYCPBA"
    try:
        import urllib.request
        urllib.request.urlretrieve(cfgUrl, "backupcfg.py")
        backupLog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + "'backupcfg.py' was created. Retrieved from '%s'."%(cfgUrl) + "\n")
        print("'backupcfg.py' was created.")
    except:
        backupLog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + "Backup Canceled: couldn't retrieve 'backupcfg.py' from '%s'."%(cfgUrl) + "\n")
        print("Backup canceled: Couldn't retrieve 'backupcfg.py' from '%s'."%(cfgUrl))
        exit()

from backupcfg import *


# function for writing messages in log, where it also writes the time
# the first argument given when you call the function tells it what to write after the time stamp
# the second argument given tells it if you want it to print to console or not

def writeToLog(message, write):
    backupLog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + message + "\n")
    if write == True and writeToConsole == True: # will only print a message if both the writeToConsole anhd write variables are set to True
        print(message)

# this bit copys files
def copyFiles(n):
    if os.path.isdir(n) == False:
        shutil.copyfile(n, target)
        writeToLog(pathlib.PurePath(n).name + " was copied to %s."%(backupDir), True)
            
    else:
        shutil.copytree(n, target)
        writeToLog(pathlib.PurePath(n).name + " and its contents were copied to %s."%(backupDir), True)



    

# checks if there is a given argument, and if it matches with a job name described in 'backupcfg.py'. if not, then an error will be given and the script stops
if len(sys.argv) < 2: # this allows the script to still run if there are more then two arguments given, as they are just ignored
    if interactive == True:
        job = input("Enter name of job: ")
    
    else:
        print("Usage: python backup.py <job>")
        writeToLog("Backup canceled: No argument given.", False)
        exit()
else:
    job = sys.argv[1]
    
# makes sure you dont enter a job that does not exist
if not job in jobs:
    if interactive == True:
        while not job in jobs:
            print("No such job exists.")
            job = input("Enter name of job: ")
    else:
        print("No such job exists.")
        writeToLog("Backup canceled: Argument given did not match job in 'backupcfg.py'.", False)
        exit()


# this part calls the 'copyFiles()' function

if True: # me being lazy and not wanting to unindent everything
    writeToLog("backing up files defined in '%s'"%(job), True)
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S ') # i could use this where it is needed but incase there is a lot of files being backed up then they would all have the same timestamp 
    backupDir = directory[job]
    for n in jobs[job]:
        target = backupDir + "/" + time + pathlib.PurePath(n).name
        
        if os.path.exists(backupDir) and os.path.exists(n):
        
            copyFiles(n)
        
        elif os.path.exists(n):
            
            os.mkdir(backupDir)
            writeToLog("'%s' was created."%(backupDir), True)
            copyFiles(n)
        
        else:
        
            writeToLog("File skipped: '%s' does not exist."%(n), True)
            
        

writeToLog("Finished backup.", False)
print("Backup complete!")