def greet():
	"""notes
	notes"""
	print("Hello")
	
greet()

def greet(user_name,gender):
	print("Hello! "+user_name+" "+gender)
greet("Oscar","male")
greet("Alice","female")
greet(gender="male",user_name="Oscar")

def greet(user_name,gender='male'):
	print("Hello! "+user_name+" is a "+gender)

greet("Oscar","female")
greet("Oscar")

def get_full(last,first):
	full=last+" "+first
	return full
full=get_full('Sheng','Cen')
print(full)

def format_n(one,two,three=''):
	if three:
		print(one+" "+two+" "+three)
	else:
		print(one+" "+two)
format_n('hey','bye','mo')
format_n('hey','bye')

def build_person(first,last,age=''):
	person={'first':first,'last':last}
	if age:
		person['age']=age
	return person
oscar=build_person('Sheng','Cen',20)
print(oscar)
oscar=build_person('Sheng','Cen')
print(oscar)

def greet_users(names):
	for name in names:
		print("Hello! "+name)
greet_users(["Oscar Cen","Mike Zhang"])
greet_users("Oscar Cen, Mike Zhang")



unprinted=['a','b','c']
printed=[]
def print_model(unprinted0,printed0):
	while unprinted:
		my=unprinted0.pop()
		printed0.append(my)
print_model(unprinted,printed)
print(printed)


'''def menu(size,*toppings):          # *:undefined number of parameters, can be various types
	print(size)
	for topping in toppings:
		print("-")
		print(topping)
menu(16,"garlic","great")	
menu(17,["garlic","xo"],["see"])	
menu(18)'''

def mydic(**dic):   
	profile={}         # two*:empty dictionary
	for key,value in dic.items():
		profile[key]=value
	return profile
mypro=mydic(a1="yes",a2="no",a3="yes")
print(mypro)


import pizza       # pizza.py available, like include in C++
pizza.menu(3,"a","b","c")       # should add "pizza."

from pizza import menu        # An alternative way.   menu:function name
menu(3,"a","b","c")           

from pizza import menu as m      # An alternative way.   i:abbreviated name for function
m(3,"a","b","c") 

import pizza as p               # An alternative way.   p:abbreviated name for module
p.menu(3,"a","b","c")

from pizza import *             # import all functions from the module
menu(6,"a","b","c") 
test()























