import math
"""
def perim(abc):
    p = (int(abc.split()[0]) + int(abc.split()[1]) + int(abc.split()[2])) / 2
    return p

def area(p, abc):
    s = math.sqrt(p * (p - int(abc.split()[0])) * (p - int(abc.split()[1])) * (p - int(abc.split()[2])))
    return s 

abc1 = input()
abc2 = input()
abc3 = input()

p1 = perim(abc1)
p2 = perim(abc2)
p3 = perim(abc3)
s1 = area(p1, abc1)
s2 = area(p2, abc2)
s3 = area(p3, abc3)
               
if (s1 == s2 and s2 == s3):
    print("same")
else:
    print("not same")


ab1 = input()
ab2 = input()
ab3 = input()

def area(ab):
    S = int(ab.split()[0]) * int(ab.split()[1])
    return S

print("1st rectangle: ", area(ab1))
print("2st rectangle: ", area(ab2))
print("3st rectangle: ", area(ab3))
"""

def zamena(array):
    a = int(array[0])
    b = int(array[len(array)-1])
    array.pop(0)
    array.pop(len(array)-1)
    array.insert(0, b)
    array.insert(len(array), a)
    return array

n = int(input())
array = [int(input()) for i in range(0, n)]

print(array)
print(zamena(array))



