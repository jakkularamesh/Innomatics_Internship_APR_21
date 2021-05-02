# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
m=input()
N=int(input())
n=input()

x=list(map(int,m.split()))
y=list(map(int,n.split()))

a=set(x)
b=set(y)

c=a.difference(b)
d=b.difference(a)

e=c.union(d)

result=list(e)

result.sort()
for i in range(len(result)):
    print(result[i])
