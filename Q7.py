"""
 WPP to enter 2 angles and using the function third angle( angle1, angle2 ) calculate the third angle.
"""
angle1 = float(input("Enter angle 1: "))
angle2 = float(input("Enter angle 2: "))

calc_angle(angle1,angle2)

def calc_angle(angle1,angle2):
    print("The third angle is :",(180-angle1-angle2))
    