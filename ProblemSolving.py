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
arr = map(int, input().split())

a = max(arr)

c = arr.count(a)

for i in range(c):
    arr.remove(a)

print(max(arr))
--------------------------------------------
