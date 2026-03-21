import os

print(os.listdir(path='.'))
print(os.listdir(path='..'))

#Find files by extension
def find_files(directory, extension):
    result = []
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(extension):
                result.append(entry.name)
    return result

py_files = find_files('.', '.py')
print(py_files)

import shutil

os.mkdir("backup", exist_ok=True)
os.mkdir("archive")

with open("example.py", "w") as f:
    f.write("print('hello')")

shutil.copy("example.py", "backup/example.py")

shutil.move("example.py", "archive/example.py")