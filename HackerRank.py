
1) '''In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years'''

def is_leap(year):
    
    leap = False
    
    if (((year % 4 == 0) and (year % 100 !=0)) or (year % 400 == 0)):
        leap = True
        
    return leap

year = int(input())
print(is_leap(year))
---------------------------------------------------------------------------------------

2) '''Without using any string methods if n = 5 Print the string '12345' 
Print the list of integers from 1 through n as a string, without spaces......'''

n = int(input('N: '))

es = ''
for i in range(1, n + 1):
    es = es + str(i)

print(es)
---------------------------------------------------------------------------------------
