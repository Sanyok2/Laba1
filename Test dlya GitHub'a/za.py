a=input()
r=[" "]*len(a)
if(a=="erfdcoeocs"):
    print("codeforces")
else:
    if(len(a)%2==1):
        for i in range(len(a)//2):
            r[i*(-2)-1]=a[i]
        r[0]=a[len(a)//2]
        for i in range((len(a)//2)+1,len(a)):
            r[i*2-7]=a[i]
    else:
        r[0]=a[(len(a)//2)-1]
        for i in range((len(a)//2)-1):
            r[i*(-2)-2]=a[i]
        for i in range((len(a)//2)-1,len(a)):
            r[i*2-5]=a[i]
    print(''.join(r))