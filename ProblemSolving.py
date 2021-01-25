#staircase

def staircase(n):
    for i in range(1, n+1):
        s = '#' * i
        print(s.rjust(n))
if __name__ == '__main__':
    n = int(input())

    staircase(n)
    
-----------------------------------
#list comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([ [a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != n])
    
--------------------------------------------------------------------------------------------------------------
#runner-up

n = int(input())
arr = list(map(int, input().split()))

a = max(arr)

c = arr.count(a)

for i in range(c):
    arr.remove(a)

print(max(arr))
--------------------------------------------
#find a string
def count_substring(string, sub_string):
    ml = len(string)
    sl = len(sub_string)
    c = 0
    for i in range(ml - sl + 1):
        if (string[i:i+sl] == sub_string):
            c = c + 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
-------------------------------------------------------
#string validators

s = input()
print(any([ i.isalnum() for i in s]))
print(any([ i.isalpha() for i in s]))
print(any([ i.isdigit() for i in s]))
print(any([ i.islower() for i in s]))
print(any([ i.isupper() for i in s]))
-------------------------------------------------------
#camelcase

def camelcase(s):
    count = 1
    for char in s:
        if char.isupper():
            count += 1
    return count

s = input()

print(camelcase(s))
-------------------------------------------------------
