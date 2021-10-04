"""
WPP to enter value in days and convert in form of years, months and days 

(assuming all months have 30 days and the year is 360). 

  eg: input is 400 so output should be 1 year 1 month and 10 days 
  
"""
value = int(input("Enter the value in days : "))

years = int(value/360)

months = int((value-360)/30) 

days = int(((value-360)-30))

print(years,"year",months, "months", days,"days" )