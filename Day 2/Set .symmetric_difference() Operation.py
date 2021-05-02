# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
m=set(input().split())
N=int(input())
n=set(input().split())
print(len(m.symmetric_difference(n)))
