

class Person:
	people_count = 0
#initializa an object
	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.people_count += 1

	def __repr__ (self):
		return " < object: {}, {}> ".format (self.name,self.age)



	def say_hello(self):
		return "Hello,I'm {} and {} y/o".format (self.name,self.age)


P = Person('Joe',23)
P2 = Person('Jane',23)
P3= Person('George',40)

print P.say_hello()

a = [('Jane',23), ('Joe',50),('Jacky',60), ('Jee',18), ('Josh',60)]

b = []

for name, age in a:
	person = Person(name,age)
	b.append (person)

for person in b:
	print person.say_hello()
	
print b
