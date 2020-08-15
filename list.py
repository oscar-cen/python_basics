mylist1=["solder","bright","td"]
print(mylist1[0])
print(mylist1[-1])          #[-1]:the last element
mylist2=[3,'srf',1]
print(mylist2[0])
mylist2[0]="hello"          # change an element
print(mylist2)
mylist2.append("me")        # add an element
print(mylist2)

city=[]
city.append("Shanghai")
city.append("Beijing")
city.append("Guangzhou")
print(city)
city.insert(1,"Hangzhou")   # insert an element to designated order
print(city)
del city[1]                 # delete an element
print(city)                 
mypop=city.pop()            # pop the last element, and return the element
print(mypop)
print(city)
city.append("Guangzhou")
pop2=city.pop(1)            # pop(1):pop the [1] element, and return it
print(pop2)
print(city)
city.insert(1,"Beijing")
city.remove("Beijing")      # remove the element(the first occurred)
print(city)
city.insert(1,"Beijing")

city.sort()                   #.sort()
print(city)
city.sort(reverse=True)
print(city)
print(sorted(city))           #sorted(city): original list not changed  
print(city)

city2=["Bei","Guang","Shang"]
city2.reverse()                #reverse the list
print(city2)
print(len(city2))               #length
city2=["Bei","Guang","Shang"]

for item in city2:
	print(item)
	print(item.upper())
	
for value in range(1,5):         #from 1 to 4
	print(value)

list3=list(range(1,6))
list3=list([1,2,3,4,5])
print(list3)
even_n=list(range(2,12,2))        # from, to(not included),walk
print(even_n)
print(min(even_n))
print(max(even_n))
print(sum(even_n))

my1=[val**2 for val in range(1,11)]     # ATTENTION
print(my1)

players=["Jordan","Alice","Oscar","Hulk"]
print(players[0:3])                       # 3 not included
print(players[:3])                        # from beginning defaulted
print(players[1:])                        # to end defaulted
print(players[-2:])                       # last two elements
print(players[:])                         # all elements

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
	print(player)

dimensions=(100,200)              #yuanzu,cannot be changed
print(dimensions[0])
for dimension in dimensions:
	print(dimension)
dimensions=(250,200)
print(dimensions)





