pascal = [1,2]
def fib(x):
	print 'started fib'
	total = 0 
	while pascal[len(pascal)-1] < x:
		print 'started while loop'
		print 'pascal is ' + str(pascal)
		print 'max in pascal is ' + str(pascal[len(pascal)-1])
		pascal.append(pascal[len(pascal)-1] + pascal[len(pascal) - 2])
	for y in pascal[:(len(pascal)-1)]:
		print 'starting for loop'
		print 'pascal is ' +str(pascal)
		print 'total = ' + str(total)
		print 'y is ' + str(y)
		if y%2 ==0:
			total = total + y
	return total
	
