def sum_1_n(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
#print("sum(5)=",sum_1_n(5))
def sum_fx(x,n):
    s=0
    for i in range(1,n+1):
        s=s+x**i/sum_1_n(i)
    return s
x=2
n=3
r=sum_fx(x,n)
print("S{},{}={}".format(x,n,r))