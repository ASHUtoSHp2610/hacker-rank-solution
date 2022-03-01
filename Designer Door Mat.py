# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m= input().split()
a='|'
b='.'
n= int(n)
m=int(m)
j=n//2-1
for i in range(n):
    if i==n//2:
        print('WELCOME'.center(m,'-'))
    else:
        if i<n//2:
            print(((b+a+b)*(2*i+1)).center(m,'-'))
        else:
            print(((b+a+b)*(2*j+1)).center(m,'-'))
            j=j-1
