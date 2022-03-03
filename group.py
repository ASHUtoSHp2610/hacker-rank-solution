import re
e=r"([a-zA-Z0-9])\1+"
m=re.search(e,input())
if m:
    print(m.group(1))
else:
    print(-1)