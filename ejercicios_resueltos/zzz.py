import os
# points = int( input() )

def duplicate(x):
    return x*2

a = (1, 2, 3)
b = map(duplicate, a)
c = {1, 2, 3}
d = [1, 2, 3]

print(type(a))
print(type(b))
print(type(c))
print(type(d))

input()