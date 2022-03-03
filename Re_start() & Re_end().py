import re
s=re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])',input().strip(),re.IGNORECASE)
if s:
    for i in s:
        print(i)
        
else:
    print(-1)