# extension_changer
changes file extensions with python

can change files recursively, or in just one specified directory

`$ python extension_changer.py -h`
usage: extension_changer.py [-h] [-p PATH] [-o OLD] [-n NEW] [-r]

This script converts file extensions

optional arguments:
  -h, --help  show this help message and exit
  -p PATH     path to dir
  -o OLD      old extension
  -n NEW      new extension
  -r          is recursive

`$ python extension_changer.py -p /home/syseng/bin/data/examples/ -o exp -n txt`
