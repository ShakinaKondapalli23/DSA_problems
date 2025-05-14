n=int(input())
untreat=0
police=0
l=list(map(int,input().split()))
for i in l:
    if i==-1:
        if police>0:
            police-=1
        else:
            untreat+=1
    else:
        police+=i
print(untreat)
        
