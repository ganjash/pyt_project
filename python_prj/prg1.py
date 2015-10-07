y=0
for n in range(2,10000):
	     if(n%100==0):
		print 'count :',100-y
		y=0
	     for x in range(2,n):
		if n%x ==0:
		   y=y+1
		   break
	     else:
	       print n, ': is prime'


