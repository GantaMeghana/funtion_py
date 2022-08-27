def even(a):
    i=0
    b=[]
    while i<len(a):
        if a[i]%2==0:
            b.append(a[i])
        i=i+1
    # print(b)
    return(b)
    
print(even([1,2,3,4,5,6]))

a=["a","n","i","a",'n',"a"]
i=0
b=[]
while i<len(a):
    j=0
    c=[]
    count=0
    while j<len(a):
        if a[i] in a:
            if a[i]==a[j]:
                count=count+1
            j=j+1
    c.append(a[i])
    c.append(count)
    if c not in b:
        b.append(c)
    i=i+1
print(b)

a=["1","2","3","4","5","6","7","8"]
i=0
c=[]
while i<len(a):
    b=a[i]+a[i+1]
    c.append(b)
    i=i+2
print(c)

a=[[1,2],[3,4],[5,6]]
i=0
b=[]
while i<len(a):
    c=a[i],a[i+1]
    b.append(c)
    i=i+2
print(b)