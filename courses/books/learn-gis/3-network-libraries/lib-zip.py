import zipfile

def main():
    zip = open('data/hancock.zip', 'rb')
    zip_shape = zipfile.ZipFile(zip)
    shp_name, shx_name, dbf_name = zip_shape.namelist()
    shp_file = open(shp_name, 'wb')
    shx_file = open(shx_name, 'wb')
    dbf_file = open(dbf_name, 'wb')
    shp_file.write(zip_shape.read(shp_name))
    shx_file.write(zip_shape.read(shx_name))
    dbf_file.write(zip_shape.read(dbf_name))
    shp_file.close()
    shx_file.close()
    dbf_file.close()

if __name__=='__main__':
    main()