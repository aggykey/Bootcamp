def funky (a,b):

  if type (a) and type (b)==str :
     print a+b
  elif  type (a) and type (b)==int or type (a) and type (b) ==float :
     print a+b
  elif  type (a) and type (b)==list:
     print a+b
  elif type (a) and type(b)==dict:
  	dict1=dict(a.items() +b.items())
  	print dict1
  else:
    print ('invalid output')

funky (1,2)
funky(3.5,5)
funky('heey' ,'there')
funky([1,2,3],['he','she','them'])
funky({'a':1,'b':2},{'c':3,'d':4})
