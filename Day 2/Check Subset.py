# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):
    a = input()
    a1 = set(input().split())
    b = input()
    b1=set(input().split())
    print(a1.issubset(b1))
