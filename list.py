if __name__ == '__main__':
    n = int(input())
    command=[]
    for i in range(n):
        command.append(input().split())
    r=[]
    for i in range(n):
        if command[i][0]=='insert':
            r.insert(int(command[i][1]),int(command[i][2]))
        elif command[i][0]=='print':
            print(r)
        
        elif command[i][0]=='remove':
            r.remove(int(command[i][1]))
        elif command[i][0]=='append':
            r.append(int(command[i][1]))
        elif command[i][0]=='pop':
            r.pop()
        elif command[i][0]=='sort':
            r.sort()
        elif command[i][0]=='reverse':
            r.reverse()
        