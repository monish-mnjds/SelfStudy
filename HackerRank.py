
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
3) '''Given a string and swap its cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.'''
def swap_case(s):
    string = s.swapcase()
    return string

if __name__ == '__main__':
    s = input("S: ")
    result = swap_case(s)
    print(result)
    
#input  ---> HackerRank.com
#output ---> hACKERrANK.COM
-----------------------------------------------------------------------------------------------------
4) '''ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.'''

def solve(s):
    names = s.split(' ')
    l = []
    for name in names:
        c = name.capitalize()
        l.append(c)
    j = ' '.join(l)
    return j

s = input('First and Last Name: ')

print('Capitalized Form: ', solve(s))

#input  ---> peshwa bajirao
#output ---> Peshwa Bajirao
-------------------------------------------------------------------------------------------------------------
5) '''You are given a string s and width w.
Your task is to wrap the string into a paragraph of width .
Print the text wrapped paragraph.'''

'''input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4'''

'''
output:
   ABCD
   EFGH
   IJKL
   IMNO
   QRST
   UVWX
   YZ'''

import textwrap

def wrap(string, max_width):
    results = textwrap.fill(string, max_width)
    return results

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
--------------------------------------------------------------------------------
6) '''If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird'''

n = int(input('n: '))

if n % 2 == 0:
    if (n >= 2 and n <= 5):
        print('Not Weird')
    elif (n >= 6 and n <= 20):
        print('Weird')
    elif (n > 20):  
        print('Not Weird')

if n % 2 == 1:
    print('Weird')
---------------------------------------------------------------------------------
6) '''You are given two values a and b.
Perform integer division and print a/b.
Print the value of a/b.
In the case of ZeroDivisionError or ValueError, print the error code.'''

#The first line contains T, the number of test cases.
#The next T lines each contain the space separated values of a and b.

n = int(input())

for i in range(n):
    
    try:
        a, b = map(int, input().split())
        print(a // b)
    
    except ZeroDivisionError as e:
        print('Error Code:', e)
    
    except ValueError as e:
        print('Error Code:', e)

# Note: a, b = input().split()    #i/p: 10 20     #a = '10'    #b = '20'
--------------------------------------------------------------------------------------------
7) '''Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stampsone by one from a stack of N country stamps.
Find the total number of distinct country stamps.
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.
Output the total number of distinct country stamps.....''''

n = int(input())            
s = set()
for i in range(n):
    
    s.add(input())

print(len(s))

'''input:
7
UK
China
USA
France
New Zealand
UK
France 

output:
5   '''
--------------------------------------------------------------------------------------------------
8) '''using calendar module find the day of the date specified in mm dd yyyy format.....'''
#08 05 2015 #mm dd yyyy

import calendar

m, d, y = map(int, input().split())
c = calendar.weekday(y, m, d)

if c == 0:
    print('MONDAY')
elif c == 1:
    print('TUESDAY')
elif c == 2:
    print('WEDNESDAY')
elif c == 3:
    print('THURSDAY')
elif c == 4:
    print('FRIDAY')
elif c == 5:
    print('SATURDAY')
elif c == 6:
    print('SUNDAY')
    
---------------------------------------------------------------------------------------------------
