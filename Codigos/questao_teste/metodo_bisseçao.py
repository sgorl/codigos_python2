from math import fabs
def bi(função, a, b, tol, inter):

    if(fabs(função(a)) <= tol): return a
    if(fabs(função(b)) <= tol): return b
    if((função(a))*função(b) > 0): 
        print(" there is no root here ")
        return None
    for i in range(1,inter + 1):
        x = (a + b)/2
        if(fabs(função(x)) < tol): break
        if(função(x)*função(a) < 0):
            b = x
        else:
            a = x
    return x    



    