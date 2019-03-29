import os
import shutil
import tempfile
import subprocess

raw_sub_p_cmd_str       = '{source} /extract {target}'
formatted_cmd_str       = None

def Create_temp_dir():
    temp_dir    = tempfile.mkdtemp()
    print(temp_dir)
    return temp_dir

def Delete_temp_dir(target_dir):
    shutil.rmtree(target_dir)
    pass

def install_td_target(installer_source_file, installer_target_dir):
    # validate inputs
    valid_dir           = os.path.isdir(installer_target_dir)
    valid_path          = os.path.isfile(installer_source_file)

    if valid_dir and valid_path:
        # valid path and dir - we can continue 

        # create temp
        temp_loc        = Create_temp_dir()

        # extact source files
        cmd_str         = raw_sub_p_cmd_str.format(source=installer_source_file, target=temp_loc)
        subprocess.call(cmd_str)

        # get unpacked direcotry
        extracted_td_dir = None

        # copy files to installer target from temp
        shutil.move(extracted_td_dir, installer_target_dir)

        # delete temp
        Delete_temp_dir(temp_loc)
        pass

    else:
        # we don't have valid inputs, we should exit at this point
        pass
        

    pass

# temp_dir = Create_temp_dir()
# print(temp_dir)

# Delete_temp_dir(temp_dir)
# print("Temp Dir deleted")