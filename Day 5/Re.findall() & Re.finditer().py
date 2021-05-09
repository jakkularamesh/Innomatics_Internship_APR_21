# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',input(),flags = re.I)
if match:
    for i in match:
        print (i)
else:
    print (-1)
