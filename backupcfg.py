
WRITE_TO_CONSOLE = True
INTERACTIVE = False
ACCEPT_MULTIPLE_ARGS = True


# to add more jobs, just copy one from below and change what is needed.
# change filenames in quotes to whatever you want to back up. more files or folders can be added by separating them with commas.
# Both relative and absolute paths work.
# These are constants because they're not expected to change over runtime
JOB_1 = ["../README.md", "./new text document.txt",
         "./files go in here!/test7.py"]
JOB_2 = ["./folder1"]
JOB_3 = ["./new text document.txt"]
JOB_4 = ["/home/ec2-user/environment/"]
JOB_5 = [".//"]
# job0 = ["<filename>"] - dont forget file extensions!

# old way of getting directory, now it supports different folders for different jobs
backupDir = "./backup/"  # could reference this in 'directory'

# changing the bits in quotes changes what you type after 'backup.py' when you run it in console.
VALID_JOBS = {"job1": JOB_1, "job2": JOB_2,
              "job3": JOB_3, "h": JOB_4, "ohno": JOB_5}

# change the folder where backups get saved to by changing the bit after the job name.
# Both relative and absolute paths work.
directory = {"job1": backupDir,  "job2": "/home/ec2-user/environment/BackupScript 1.3.0/h",
             "job3": backupDir, "h": backupDir, "ohno": backupDir}
