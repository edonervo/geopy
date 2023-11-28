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
    map_width = 800
    map_height = 300

    # Define the bounding box of the main plygon (Colorado State)
    minx = min(point[0] for point in state[POINTS])
    maxx = max(point[0] for point in state[POINTS])
    miny = min(point[1] for point in state[POINTS])
    maxy = max(point[1] for point in state[POINTS])
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
    # TODO: How to force it to go in a display?
    # window_width = window.window_width()
    # window_height = window.window_height()
    # window.setup(width=window_width, height=window_height)
    # screen_x = 0
    # screen_y = 0
    # window.setworldcoordinates(screen_x, screen_y, window_width, window_height)
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

    # render the cities
    for city in cities:
        pixel = convert(city[POINTS])
        t.up()  
        t.goto(pixel)
        # Place a point for the city
        t.dot(10)
        # Label the city
        t.write(city[NAME] + ", Pop.: " + str(city[POP]), align="left")
        t.up()

    # Spatial Query: which has the largest population?
    biggest_city = max(cities, key=lambda city:city[POP])
    t.goto(0, -200)  
    t.write('The biggest city is: ' + biggest_city[NAME])

    # Spatial Query: which has the largest population?
    western_city = min(cities, key=lambda city:city[POINTS])
    t.goto(0, -220) 
    t.write('The most western city is: ' + western_city[NAME])


    t.pen(shown=False)
    t.done()


if __name__ == '__main__':
    main()