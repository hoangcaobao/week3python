def timso2mulonnha(m,n):
    if m<n:
        m,n=n,m
    for i in range(0,n):
        if 2**i<=n:
            result=2**i
    return result

def baobeo(m,n):
    if m<n:
        m,n=n,m
    if m==1 and n==1:
        result= 1
   
    elif m==0 :
        result=0
    elif n==0:
        result=0
    else:
        if n==timso2mulonnha(m,n) and m==timso2mulonnha(m,n):
            result=1;
        else:
            i=timso2mulonnha(m,n)
            result=1+baobeo(m,n-i)+baobeo(m-i,i)
    return result
    print(i)

x=baobeo(4,5)
print(x)
