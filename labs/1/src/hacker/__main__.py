import sys
from multiprocessing import Process

from interface import Interface


HACKER_DIR = 'data/hacker/'
SHARE_DIR = 'data/share/'

if __name__ == '__main__':
    interface = Interface(HACKER_DIR, SHARE_DIR)

    try:
        interface.show()
    except BaseException as e:
        with open('err', 'w') as ef:
            ef.write(str(e))

    sys.exit(0)
