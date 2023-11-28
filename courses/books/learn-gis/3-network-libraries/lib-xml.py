from xml.dom import minidom
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def main():
    # minidom
    # kml = minidom.parse('data/time-stamp-point.kml')
    # placemarks = kml.getElementsByTagName('Placemark')
    # # print(len(placemarks))
    # # print(placemarks[0].toxml())
    # coordinates = placemarks[0].getElementsByTagName('coordinates')
    # point = coordinates[0].firstChild.data
    # print(point)

    # ElementTree
    tree = ET.ElementTree(file='data/time-stamp-point.kml')
    ns = '{http://www.opengis.net/kml/2.2}'
    placemark = tree.find(".//%sPlacemark" % ns)
    coordinates = placemark.find("./{}Point/{}coordinates".format(ns, ns))
    print(coordinates.text)

if __name__ == '__main__':
    main()