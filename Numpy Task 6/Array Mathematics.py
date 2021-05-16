import numpy
n,m = map(int, input().split())
a=numpy.array([list(map(int, input().split())) for n in range(n)])
b=numpy.array([list(map(int, input().split())) for n in range(n)])

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
