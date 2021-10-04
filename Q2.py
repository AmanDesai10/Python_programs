"""
 WPP to enter the radius of the circle and calculate the area and circumference of the circle. 
"""


radius = int(input("Enter radius of circle : "))

print("Area of circle : ",end = "")
print("{:.2f}".format(3.14*radius*radius))
print("Circumference of circle : ",end = '')
print("{:.2f}".format(2*3.14*radius))