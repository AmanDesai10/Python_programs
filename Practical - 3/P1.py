'''
Question: To compute distance between two points (x1,y1) to (x2,y2) ( take input from the user)
'''

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = ((x2-x1)**2+(y2-y1)**2)**0.5
print("Distance between ({},{}) and ({},{}) is: {}".format(x1,y1,x2,y2,round(distance,4)))