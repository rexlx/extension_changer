import os
import argparse
import time

"""
description:

this tool swaps a files extension. it will work recursively, or in one
directory.

example:

$ python extension_changer.py -h
usage: extension_changer.py [-h] [-p PATH] [-o OLD] [-n NEW] [-r]

This script converts file extensions

optional arguments:
  -h, --help  show this help message and exit
  -p PATH     path to dir
  -o OLD      old extension
  -n NEW      new extension
  -r          is recursive

python extension_changer.py -p /home/syseng/bin/data/examples/ -o exp -n txt
"""

# you can hard code values here if you dont want a bunch of args
user_path = '/path/here'
user_old = 'okay'
user_new = 'ok'


def get_args():
    """
    get the cli args via the argparse module
    """
    msg = "This script converts file extensions"
    # create an instance of parser with our unique msg
    parser = argparse.ArgumentParser(description=msg)
    # add expected arguments
    parser.add_argument('-p', dest='path', required=False, help="path to dir")
    parser.add_argument('-o', dest='old', required=False, help="old extension")
    parser.add_argument('-n', dest='new', required=False, help="new extension")
    parser.add_argument('-r', dest='recursive', required=False,
                        action="store_true", help="is recursive")
    args = parser.parse_args()
    if args.path:
        path = args.path
    else:
        path = user_path
    if args.old:
        old = args.old
    else:
        old = user_old
    if args.new:
        new = args.new
    else:
        new = user_new
    if args.recursive:
        recursive = True
    else:
        recursive = False
    return path, recursive, old, new


def get_files(recursive, path):
    """
    returns a python list of files with full paths. requires two
    parameters: recursive (boolean) and path (string)
    """
    if not recursive:
        # this makes a list of just filenames (no paths)
        filenames = [e for e in os.listdir(path)]
        # but we wants full paths, use an os path join
        file_list = [os.path.join(path, e) for e in filenames]
    else:
        # this will decend into all subdirs
        file_list = [os.path.join(dir_path, x)
                     for dir_path, dirs, files in os.walk(path)
                     for x in files]
    return file_list


def change_extension(path, file_list, old, new):
    """
    changes the file extension and logs the modification
    """
    # try to remove the change log
    try:
        os.remove('ext_change.log')
    # exception is like file does not exist
    except Exception as _e:
        # whatever it is we dont care
        pass
    # open the change log
    with open('ext_change.log', 'a') as f:
        for i in file_list:
            # if the file ends with the old extension
            if i.endswith(old):
                # split the filename into ('name', '.ext')
                base = os.path.splitext(i)[0]
                # add the new extension to the base file name
                newfile = base + '.' + new
                # log the move
                f.write('moving ' + i + ' to ' + newfile + '\n')
                # do the move
                os.rename(i, newfile)


def main():
    """
    times the duration of the runtime, gets user args, gets the file
    list, changes the extension, informs user upon completion
    """
    start = time.time()
    path, recursive, old, new = get_args()
    file_list = get_files(recursive, path)
    change_extension(path, file_list, old, new)
    runtime = time.time() - start
    print('complete \nran for ' + str(runtime) + ' seconds.')


# if the scripts is being ran as itself, and not being imported
if __name__ == '__main__':
    # run
    main()
