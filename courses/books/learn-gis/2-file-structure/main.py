import struct
import os

def main():
    f = open(os.getcwd() + '/data/hancock.shp', 'rb')
    f.seek(36)
    print(struct.unpack('<dddd', f.read(32)))


if __name__ == '__main__':
    main()