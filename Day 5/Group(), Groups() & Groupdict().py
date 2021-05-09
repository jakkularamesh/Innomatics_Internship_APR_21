# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.search(r'([A-Za-z0-9])\1+',input())
if m:
    a=m.group(1)
    print (a)
else:
    print (-1)
