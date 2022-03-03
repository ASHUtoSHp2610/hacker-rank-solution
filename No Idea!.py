a,b=list(map(int, input().split()))
c= list(map(int, input().split()))
n=set(map(int, input().split()))
m=set(map(int, input().split()))
res = 0
for x in c:
    if x in n:
        res+=1
    elif x in m:
        res-=1
print(res)