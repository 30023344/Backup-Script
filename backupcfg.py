
writeToConsole = True
interactive = False
acceptMultibleArgs = True


# to add more jobs, just copy one from below and change what is needed.
# change filenames in quotes to whatever you want to back up. more files or folders can be added by sepreating them with commas.
# Both relitave and absolute paths work.

job1 = ["../README.md", "./new text document.txt", "./files go in here!/test7.py"]
job2 = ["./folder1"]
job3 = ["./new text document.txt"]
job4 = ["/home/ec2-user/environment/"]
job5 = [".//"]
#job0 = ["<filename>"] - dont forget file extensions!

# old way of getting directory, now it supports different folders for different jobs
backupDir = "./backup/" # could reference this in 'directory'

# changing the bits in quotes changes what you type after 'backup.py' when you run it in console.
jobs = {"job1": job1, "job2": job2, "job3": job3, "h": job4, "ohno": job5}

# change the folder where backups get saved to by changing the bit after the job name.
# Both relitave and absolute paths work.
directory = {"job1": backupDir,  "job2": "/home/ec2-user/environment/BackupScript 1.3.0/h", "job3": backupDir, "h": backupDir, "ohno": backupDir}