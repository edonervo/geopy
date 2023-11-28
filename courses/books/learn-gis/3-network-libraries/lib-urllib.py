import urllib.request
import urllib.parse
import urllib.error

def main():
    # url = "https://github.com/GeospatialPython/Learn/raw/master/hancock.zip"
    # filename = 'hancock.zip'
    # print(urllib.request.urlretrieve(url, filename))   

    url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv'
    filename = 'earthquakes_last_hour.csv'
    print(urllib.request.urlretrieve(url, filename))   

if __name__ == '__main__':
    main()

