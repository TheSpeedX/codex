num=x=13
i=0
Dict={}
lst=[]
# n/2 even
# 3n+1 odd

while i<1000000:
    c=0
    x=num
    while x!=1:
        
        if(x%2 == 0):
            x/=2
            # print('inside if',num)
        else:
            x=3*x+1
            # print('inside else',num)
        c+=1
    
    # print(c,)
    Dict[c]=num
    num+=1
    i+=1
    # print(i)

lst=list(Dict.keys())
print(max(lst))
