def sumMultiplesof5not7(n):
	'''prints the sum of numbers less than n that are multiples of 5 but not 7
	'''
	res = 0
	i=0
	for i in range(1,500):
		if(i%7 !=0 and i%5==0):
			res+=i
			
	print(res)
sumMultiplesof5not7(500)
