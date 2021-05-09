# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())

for i in range(0,n):
   txt = input()
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   print(txt)

