from shapely.geometry import point, Polygon
from shapely.geometry import LineString
import matplotlib.pyplot as plt

point1 = point.Point(1.0, 2.0)
point2 = point.Point(3.0, 4.0)
point3 = point.Point(5.0, 6.0)
polygon1 = Polygon([(0, 0), (0, 5), (5, 5), (5, 0)])
print("Point:", point1)
print("Polygon:", polygon1)
print("Point within Polygon:", polygon1.contains(point1))


line = LineString([(0, 0), (1, 1), (2, 2)])
print("LineString:", line)
print("LineString length:", line.length)

list(line.coords)
xcoords, ycoords = line.xy
print("X coordinates:", xcoords)
print("Y coordinates:", ycoords)



print(line.centroid)


polygon2 = Polygon([(1, 1), (1, 4), (4, 4), (4, 1)])
print("Polygon 1:", polygon1)
print("Polygon 2:", polygon2)
print("Polygon 1 contains Polygon 2:", polygon1.contains(polygon2))
# plotting the polygons
x1, y1 = polygon1.exterior.xy
x2, y2 = polygon2.exterior.xy
plt.plot(x1, y1, label='Polygon 1')
plt.plot(x2, y2, label='Polygon 2')
plt.legend()
plt.title('Polygons')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

# filled polygon
plt.fill(x1, y1, alpha=0.5, label='Polygon 1')
plt.fill(x2, y2, alpha=0.5, label='Polygon 2')
plt.legend()
plt.title('Filled Polygons')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()


