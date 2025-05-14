def is_prime(n, i=2):
    if n<2:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    return is_prime(n,i+1)
def fun(l,i=0):
    if i==len(l):
        return 0
    if is_prime(l[i]):
        return 1+fun(l,i+1)
    else:
        return fun(l,i+1)

l= [1,2,3,4,5]
print(fun(l))