
writeToConsole = True
interactive = False


# to add more jobs, just copy one from below and change what is needed.
# change filenames in quotes to whatever you want to back up. more files or folders can be added by sepreating them with commas.
# complete paths also work.

job1 = ["../README.md", "new text document.txt", "files go in here!/test7.py"]
job2 = ["folder1"]
job3 = ["new text document.txt"]
job4 = ["/home/ec2-user/environment/"]
#job0 = ["<filename>"] - dont forget file extensions!



# changing the bits in quotes changes what you type after 'backup.py' when you run it in console.
jobs = {"job1": job1, "job2": job2, "job3": job3, "h": job4}
# change the folder where backups get saved to by changing the bit after the job name.
# both complete and relative paths work here.
directory = {"job1": "backup",  "job2": "backup", "job3": "backup", "h": "backup"}


#backupDir = "backup" # old way of getting directory, now it supports different folders for different jobs
