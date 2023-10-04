import sys

from interface import Interface


USER_DIR = 'data/user/'
SHARE_DIR = 'data/share/'

if __name__ == '__main__':
    interface = Interface(USER_DIR, SHARE_DIR)
    interface.show()

    sys.exit(0)
