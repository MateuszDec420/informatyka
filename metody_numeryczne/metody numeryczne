def wb(x):
    if x<0:
        return -x
    else:
        return x
def f(x):
    return 2*x-1
a=-1
b=4
e=0.0001
if f(a)*f(b)<=0:
    while wb(a-b)>e:
        s=(a+b)/2
        print(s)
        if f(a)*f(s)<0:
            b=s
        else:
            a=s