if __name__ == '__main__':
    N = int(input())
    Output = [];
    for i in range(0,N):
        a= input().split();
        if a[0] == "print":
            print(Output)
        elif a[0] == "insert":
            Output.insert(int(a[1]),int(a[2]))
        elif a[0] == "remove":
            Output.remove(int(a[1]))
        elif a[0] == "pop":
            Output.pop();
        elif a[0] == "append":
            Output.append(int(a[1]))
        elif a[0] == "sort":
            Output.sort();
        else:
            Output.reverse();
