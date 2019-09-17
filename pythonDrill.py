

import os

myDir = 'C:\\Users\\Alex\Documents\\Tech Academy Notes\\Python\\PythonDrills'
modTime = os.path.getmtime(myDir)


for file in os.listdir('C:\\Users\\Alex\Documents\\Tech Academy Notes\\Python\\PythonDrills'):
    if file.endswith(".txt"):
        print(os.path.join(myDir,file),modTime)
