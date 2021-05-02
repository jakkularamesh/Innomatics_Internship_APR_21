a = set(input().split())
n=int(input())
counter= 0
for i in range (n):
        b = set(input().split())
        if a.issuperset(b) :
                counter += 1
print(counter == n)
