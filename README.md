# extension_changer
changes file extensions with python

can change files recursively, or in just one specified directory

`$ python extension_changer.py -h`
<br/>
usage: extension_changer.py [-h] [-p PATH] [-o OLD] [-n NEW] [-r]

This script converts file extensions

optional arguments:<br/>
  -h, --help  show this help message and exit<br/>
  -p PATH     path to dir<br/>
  -o OLD      old extension<br/>
  -n NEW      new extension<br/>
  -u          undo, revert changes<br/>
  -r          is recursive<br/>

`$ python extension_changer.py -p /home/rxlx/bin/data/examples/ -o txt -n csv`


after completetion, it will create a file  './ext_change.log' that shows each file modification made.
