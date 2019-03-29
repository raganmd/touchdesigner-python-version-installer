import os
import sys
from argparse import ArgumentParser
import subprocess

def TD_updateder(source, target):
    # call string looks like
    # source_installer /extract target_dir
    installer_str       = "{source} /extract {target}".format(source=source, target=target)
    subprocess.call(installer_str)
    pass

# execution order matters -this puppy has to be at the bottom as our functions are defined above
if __name__ == '__main__':
    parser = ArgumentParser(description='Set up a file watcher to stylize files that are added to the specified folder')
    parser.add_argument("-s", "--source", dest="source", help="the source installer", required=True)
    parser.add_argument("-t", "--target", dest="target", help="the target installer directory", required=True)    

    args = parser.parse_args()
    TD_updateder(args.source, args.target)
    pass