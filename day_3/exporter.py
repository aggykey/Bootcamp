people = [
('Joe',78),
('Janet',90),
('Brian',67)
]

def super_sum(*args):
	return sum(args)

def hello_again (name,age):
	return "I am {},and {} years old ".format (name, age)


def max_min(A):
	'''
	returns max value- min value

	'''
	#return max (A) - min(A)
	max_,min_ = A[0],A[0]

	for i in A :
		if i > max_:
			max_ = i
		if i < min_:
			return max_ - min_
