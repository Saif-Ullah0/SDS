from shapely.geometry import Point, LineString, Polygon
from matplotlib import pyplot as plt
point1= Point(31.47996, 74.34298)
point2= Point(31.47572, 74.33779)
point3= Point(31.57593, 74.34255)

# line  from these points

line1 = LineString([point1, point2])
line2 = LineString([point2, point3])
print("Line 1:", line1)
print("Line 2:", line2)

# length of the lines

print("Length of Line 1:", line1.length)
print("Length of Line 2:", line2.length)
print("Total Length:", line1.length + line2.length)

# centroid of the all 3 combined lines
combined_lines = line1.union(line2)
print("Combined Lines:", combined_lines)
print("Centroid of Combined Lines:", combined_lines.centroid)


# combined from all 3 points 
polygon = Polygon([point1, point2, point3])
print("\nPolygon:", polygon)
# print("Centroid of Polygon:", polygon.centroid)

# exterior circumference of the polygon
print("Exterior Circumference of Polygon:", polygon.exterior.length)

print("Area of Polygon:", polygon.area)

#construct  close shape 
polygon2 = Polygon([(31.47996, 74.34298), (31.47572, 74.33779), (31.57593, 74.34255), (31.47996, 74.34298)])
print("\nPolygon 2:", polygon2)
print("Area of Polygon 2:", polygon2.area)
