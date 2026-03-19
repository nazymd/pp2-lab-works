import shutil
import os
shutil.copy("Data.txt", "Data2.txt")
os.remove("Data2.txt")