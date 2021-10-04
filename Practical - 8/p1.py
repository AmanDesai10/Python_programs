'''
Question: functions: With / without Arguments (Positional Arguments)
'''
def greeting(name):
    return f"Good Morning , {name}"

def hello():
    return "Hello, hope you are doing well!!"

name = input("Enter your name : ")
print(greeting(name))
print(hello())