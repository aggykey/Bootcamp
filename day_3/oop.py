from person import Person
from kenyan import Kenyan



P = Person('Joe',23)




print P
  

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
