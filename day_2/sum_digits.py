def sum_digits(A):
	'''
	Takes a list A,and returns
	the sum of all the digits in the
	list e.g[10,30,45] should return
	1+0+3+0+4=5
	'''
	total = 0
	for i in A:
		digit =str (i)
		digit.split()

		for i in digit:
			total+=int(i)

	return total



    
