import re
n = int(input())
for i in range(n):
    name, email = input().split()
    p="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(p, email)):
        print(name,email)