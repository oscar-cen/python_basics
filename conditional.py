schools=['sz','he','ff','qb','jf']
for school in schools:
	if school == 'qb':
		print(school.upper())
	else:
		print(school.title())

age1=18
age2=22
if age1<=19 and age2>=20:
	print('pass')
	
if age1<=18 or age2<=21:
	print('pass')

print(age1 in range(17,19))        #boolean
if age1 not in range(20,22):
	print('good')

if age1<16:
	print('ju')
elif age1<19:
	print('uni')
elif age1<20:
	print('bi')
else:                              #else can be omitted
	print('adult')

test=[]
if test:                            # whether it's empty
	print('false')
else:
	print('true')

avail=['sz','he','ff','qb','jf']
req=['sz','qb','de']
for r in req:
	if r in avail:
		print("Good!"+r)
	else:
		print("No!"+r)











