"""Simple GIS application"""
from constants import NAME, POINTS, POP
import turtle as t # simple module for graphics in python

def main():
    # Base data structure. State name, polygon, population
    state = ["COLORADO", [[-109, 37],[-109, 41],[-102, 41],[-102, 37]],
5187582]
    
    # Cities
    cities = []
    cities.append(["DENVER",[-104.98, 39.74], 634265])
    cities.append(["BOULDER",[-105.27, 40.02], 98889])
    cities.append(["DURANGO",[-107.88,37.28], 17069])

    # Map size
    map_width = 400
    map_height = 300

    # Define the bounding box of the main plygon (Colorado State)
    minx = min([city[POINTS][0] for city in cities])
    maxx = max([city[POINTS][0] for city in cities])
    miny = min([city[POINTS][1] for city in cities])
    maxy = max([city[POINTS][1] for city in cities])
    # print(minx, maxx, miny, maxy)

    # Calculate the ration of state against canvas
    dist_x = maxx - minx
    dist_y = maxy - miny
    x_ratio = map_width / dist_x
    y_ratio = map_height / dist_y

    def convert(point:list[float]):
        """It transforms a point in the map coordinates from data layers into pixel coordinates using previous calculations."""
        lon, lat = point[0], point[1]
        x = map_width - ((maxx-lon)*x_ratio)
        y = map_height - ((maxy-lat)*y_ratio)
        # Python turtle graphics start in the
        # middle of the screen. We must offset
        x = x-(map_width/2)
        y = y-(map_height/2)    
        return [x, y]
    
    # Render the State
    window = t.Screen() # screen obj
    window.title("Simple GIS")
    t.up() # move the cursor up, it will not draw
    first_pixel = None
    for point in state[POINTS]:
        pixel = convert(point)
        if not first_pixel:
            first_pixel = pixel
        t.goto(pixel)
        t.down() # move the cursor down, ready to write
    t.goto(first_pixel)
    t.up()
    t.goto([0, 0])
    t.write(state[NAME], align='center', font=("Arial", 16, "bold"))
    t.done()

    #
    
        



        
    









if __name__ == '__main__':
    main()