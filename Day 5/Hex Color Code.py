# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
f = False
for _ in range(T):
    s = input()
    if '{' in s:
        f = True
    elif '}' in s:
        f= False
    elif f:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)
