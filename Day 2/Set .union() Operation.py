# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
n1=set(input().split())

m=int(input())
m1=set(input().split())

u=n1.union(m1)
print(len(u))




