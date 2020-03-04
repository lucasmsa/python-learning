import os
from datetime import datetime

# Get current working directory
print(os.getcwd())

# Change directory 
os.chdir('e:\Lavid')

print(os.getcwd())

# List files and folders on the desktop
print(os.listdir())


# Create new directory
#os.makedirs('OS-demo')

# Remove directory
#os.removedirs('OS-demo')

# Renaming
#os.rename('Python learning', 'pythonLearning')

print(os.listdir())

os.chdir('e:\Lavid\Python learning\modules')
# Check file info

# Check last modified time
mod_time = os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(mod_time))


# Checking all files starting from folder
for dirPath, dirnNames, fileNames in os.walk('e:\Lavid\Python learning'):
    print(dirPath)
    print(dirnNames)
    print(fileNames)