'''
Demonstrate the Handling Multiple Exceptions

Name- Shreyansh Bhagat
Id- 19IT009
'''
def fun(num):
    if num < 5:
        result = num/(num-3)
 
    print("Value of result : ", result)
     
try:
    num = int(input("Enter any number : "))
    fun(num)
 
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
except ValueError:
    print("Your entered number is invalid.")
