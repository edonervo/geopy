import ftplib

def main():
    server = 'ftp.ngdc.noaa.gov'
    dir = "hazards/DART/20070815_peru"
    filename = '21415_from_20070727_08_55_15_tides.txt'
    ftp = ftplib.FTP(host=server)  # Main class
    ftp.login() # anonumous login
    ftp.cwd(dir) # change dir

    with open(filename, 'wb') as out:
        ftp.retrbinary('RETR ' + filename, out.write)

    with open(filename) as dart:
        for line in dart:
            if "LAT, " in line:
                print(line)
                break

if __name__ == '__main__':
    main()