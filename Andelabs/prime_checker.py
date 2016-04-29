class PrimeChecker():
  def __init__(self, number):
    self.number=number
    
  def is_prime(self,num):
    if num > 1:
      if (num % num) == 0:
       print(num,"is not a prime number")
      else:
        print(num,"is a prime number")
    else:
      print num
p=PrimeChecker(7)
print p.is_prime()
