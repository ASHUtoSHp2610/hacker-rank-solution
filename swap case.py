def swap_case(s):
    c=[]
    for i in range(len(s)):
        if(s[i].isupper())==True:
            c.append(s[i].lower())
        elif (s[i].islower()==True):
            c.append(s[i].upper())
        else:
            c.append(s[i])
        stri=''
    return stri.join(c)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)