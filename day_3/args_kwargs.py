def hello(name,age,class_= ""):
	'''
	format function

	'''
	if class_ != "":
		return "I am {}, {} y/o and class {}".format(name, age, class_)
    #return "I am {}, my age is {}".format(name, age)


people = [
       ("jane",23,'high'),
       ("Joe",25 ,'low'),
       ("Brian",60  ),
       ("Betty",45 )]
'''
for name, age  in people:
	print hello(name, age,class_)

'''

for person in people:
	print hello(*person)

def  super_sum(*args):
 	'''
 	Takes in variable number of items,and
 	returns the sum.
 	e.g super_sum(10, 20) = 30
 	super_sum(10, 20, 40) = 70
 	'''
 	total = 0

 	for i in args:
 		total += i
 	return total	


print super_sum(10,20)
print super_sum(1, 4, 5,7)
a = [10,40,60]
print super_sum(*a)


def hello_again(**kwargs):
	return "I am {}, and I'm {}".format(kwargs['name'],kwargs ['age'])
print hello_again(name='Joe', age=98)
print hello_again(age=98,name='Joe',)


Joe={'name':'Joe' ,'age':98}

print hello_again (**Joe)
print hello_again (name='Joe',age=98)
