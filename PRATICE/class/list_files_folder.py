import sys
import os

def main(argc, argv):
    if [argc != 2]:
        print("Usage Error: require one cli argument")
        sys.exit(-1)

    if not os.path.isdir(argv[1]):
        print("input path is not dir")
        sys.exit(-1)

    def check_dir(item):
        if os.path.isdir(item):
            return True
        else
            return False


    files = os.listdir(argv[1])

    for i in files:
        ret=check_dir(i)
        if ret=True:
            os.listdir(i)
            









main(len(sys.argv), sys.argv)