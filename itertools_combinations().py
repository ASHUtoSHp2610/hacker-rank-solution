from itertools import combinations
i = input().split()
s =i[0]
k = int(i[1])
for i in range(1,k+1):
    for j in combinations(sorted(s),i):
        print("".join(j))