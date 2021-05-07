# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB=float(input())
BC=float(input())
c=math.atan(AB/BC)
print(str(int(round(math.degrees(c))))+'\N{DEGREE SIGN}')
