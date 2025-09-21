
import os

folder = "files"
name = "Kisha"
age = 29
print(f"My name is {name} and I'm {age}, trying to figure out my life.")

for fileName in os.listdir(folder):
    oldPath = os.path.join(folder, fileName)
    print(oldPath)

    newPath = os.path.join(folder, fileName.replace(".py", "_old.py"))
    print(newPath)

    os.rename(oldPath, newPath)
