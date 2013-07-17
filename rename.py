#!/usr/bin/env python
from os import listdir
from os.path import isfile, join
from subprocess import call

def main():
    onlyfiles = [ f for f in listdir("/home/yibinl/Downloads/daliu") if isfile(join("/home/yibinl/Downloads/daliu",f)) ]
    files = []
    for f in sorted(onlyfiles):
        if "rename" not in f:
            files.append(f)
    namefile = open('/home/yibinl/Downloads/names/names.txt', 'r')
    cnt = 0
    for line in namefile:
        call(["mv", files[cnt] , line.rstrip()])
        cnt += 1
    return
    

if __name__ == "__main__":
    """
    Announce main
    """
    main()
