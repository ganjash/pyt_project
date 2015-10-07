import sys
y=int(sys.argv[1])
print y
def fib(n,L):
	# fibonocci
	a,b=0,1
	while(a<n):
	   L.append(a)
	   a,b=b,a+b
        return L

x=[]
print fib(y,x[:])

