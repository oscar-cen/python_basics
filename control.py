st=[2,4]
st[0]=1
st[1]=2
print(st)

my={}
my['st']=2
print(my)




cur=1;
while cur<=5:
	print(cur)
	cur+=1

cur=0
while cur<=10:
	cur+=1
	if cur%2==0:
		continue                  #skip the remaining steps in the "current" loop
	print(cur)


pets=['cat','dog','bird','cat','cat']
while 'cat' in pets:
	pets.remove('cat')
print(pets)

while True:
	city=input("Prompt:")
	if city=='quit':
		break
	else:
		print(city)



message=input("Tell me something: ")
print(message)

age=input("Your age: ")
age=int(age)
print(age>=18)
