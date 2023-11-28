import tarfile

def main():
    # compress
    # tar = tarfile.open('hancock.tar.gz', 'w:gz')
    # tar.add('hancock.shp')
    # tar.add('hancock.shx')
    # tar.add('hancock.dbf')
    # tar.close()

    # extract
    tar = tarfile.open('hancock.tar.gz', 'r:gz')
    tar.extractall()
    tar.close()

if __name__ == '__main__':
    main()