"""
WPP to enter marks of 5 subjects and find the mean of 5 subjects, calculate percentage. If the percentage is less than 35 print fail else print pass. 
"""


sub1 = int(input("Enter marks for subject 1 :"))
sub2 = int(input("Enter marks for subject 2 :"))
sub3 = int(input("Enter marks for subject 3 :"))
sub4 = int(input("Enter marks for subject 4 :"))
sub5 = int(input("Enter marks for subject 5 :"))

per = (sub1+sub2+sub3+sub4+sub5)/5
#print(per)
if(per<35):
    print("Fail")
else:
    print("Pass")

