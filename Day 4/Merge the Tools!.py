def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        l = string[i:i+k]
        n = ""
        for i in l:
            if i not in n:
                n+=i
        print(n)

