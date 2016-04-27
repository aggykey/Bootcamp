def data_type(x):
	'''
	Takes in an argument ,x:
	-for a interger,return x**2
	-for a float,return x/2
	-for a string,returns"hello" + x
	-for a boolean ,returns"boolean"
	-for a  long,return 'long'
	'''
	if type(x) == int:
		return x ** 2
	elif type(x) == float:
		return x / 2
	elif type(x) == str:
		return "Hello {}".format(x)
	elif type(x) == bool:
		return "boolean"
	elif type (x) == long:
		return "long"
	else:
		return ()

print data_type(4)
print data_type(2.4)
print data_type('hello')
print data_type(True)
print data_type(123456789098765432345678)



