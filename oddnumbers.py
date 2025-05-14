def oddnumbers(n):
    if n>100:
        return
    if n%2!=0:
        print(n,end=" ")
    oddnumbers(n+1)
oddnumbers(1)

print()

def evennumbers(n):
    if n>100:
        return
    if n%2==0:
        print(n,end=" ")
    evennumbers(n+1)
evennumbers(1)
