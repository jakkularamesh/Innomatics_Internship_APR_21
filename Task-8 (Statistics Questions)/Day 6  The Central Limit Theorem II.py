# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
target =250
n =100
mean =2.4

std = 2.0


mean_s = n * mean
std_s = std * n**(1/2)

def cdf(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))

print(round(cdf(target, mean_s, std_s), 4))
