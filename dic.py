a1={"color":"red", 'age':18, 'shape':'circle'}
print(a1)
print(a1["age"])
print("He's "+str(a1['age'])+" years old!")

a1['xpos']=25      # add jianzhidui freely like LIST
a1['ypos']=10
print(a1)

a2={}              # create an empty dictionary
a2['color']="blue"
a2['xpos']=25      
a2['ypos']=10
print(a2)
a2['xpos']=23       # revise a value freely
print(a2)
del a2['color']
print(a2)

favo_lan={
	'sam':'python',
	'peter':'c',
	'john':'python',
	'alice':'java'
}
print(favo_lan)
for a,b in favo_lan.items():        #transverse: xxx.items()
	print("key: "+a)
	print("value: "+b)

for a in favo_lan.keys():           #ransverse all keys
	print(a)

for name in sorted(favo_lan.keys()):
	print("Name: "+name+": "+favo_lan[name])

for val in favo_lan.values():
	print(val)
print("\n")
for val in set(favo_lan.values()):    # all alternative keys
	print(val)

a1={"color":"red", 'age':18, 'shape':'circle'}
a2={"color":"blue", 'age':20, 'shape':'rec'}
a3={"color":"green", 'age':22, 'shape':'tri'}
aliens=[a1,a2,a3]
for alien in aliens:
	print(alien)

pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese']
}
for topping in pizza['toppings']:
	print("\t"+topping)

users={
	'oscar':{
		'name':'cen',
		'password':123,
		'hobby':'swimming'
	},
	'john':{
		'name':'hey',
		'password':234,
		'hobby':'joking'
	}
}
print(users)









































	
	
	
	
	
	
