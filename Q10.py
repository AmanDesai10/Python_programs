"""
WPP to enter principal amount, time and interest rate. Create simple_interest(principal, time, rate) function to calculate simple interest.
"""


amount = int(input("Enter principal amount: "))
time = int(input("Enter time period: "))
interest = float(input("Enter interest rate: "))

simple_interest(amount,time,interest)

def simple_interest(principal,time,rate):
    print("Simple interest is : ",(principal*time*rate)/100)