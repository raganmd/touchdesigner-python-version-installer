import os
import shutil
import tempfile
import subprocess

raw_sub_p_cmd_str       = '{source} /extract {target}'.format(source=source, target=target)
formatted_cmd_str       = None

def Create_temp_dir():
    temp_dir    = tempfile.mkdtemp()
    print(temp_dir)
    return temp_dir

def Delete_temp_dir(target_dir):
    shutil.rmtree(target_dir)
    pass

def install_td_target(installer_source_dir, installer_target_dir):
    # validate inputs

    # create temp

    # extact source files

    # copy files to installer target from temp

    # delete temp

    pass

# temp_dir = Create_temp_dir()
# print(temp_dir)

# Delete_temp_dir(temp_dir)
# print("Temp Dir deleted")