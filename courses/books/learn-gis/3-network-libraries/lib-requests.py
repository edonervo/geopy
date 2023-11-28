import requests

def main():
    url = "https://github.com/GeospatialPython/Learning/raw/master/hancock.zip"
    filename = "data/hancock.zip"
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

if __name__ == '__main__':
    main()

