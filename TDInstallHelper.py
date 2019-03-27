import os
import shutil
import tempfile

def Create_temp_dir():
    temp_dir    = tempfile.mkdtemp()
    print(temp_dir)
    return temp_dir

def Delete_temp_dir(target_dir):
    shutil.rmtree(target_dir)
    pass

temp_dir = Create_temp_dir()
print(temp_dir)

Delete_temp_dir(temp_dir)
print("Temp Dir deleted")