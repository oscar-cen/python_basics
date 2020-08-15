try:
	print(5/0)
except ZeroDivisionError:
	print("Wrong!")
	
try:
	print(5/1.2)
except ZeroDivisionError:
	print("Wrong!")

try:
	ans=5/0
except ZeroDivisionError:
	print("Wrong!")
else:
	print(ans)

try:
	ans=5/1.2
except ZeroDivisionError:
	print("Wrong!")
else:
	print(ans)

try:
	with open("alice.txt") as f1:
		contents=f1.read()
except FileNotFoundError:
	print("Not exist")

mysp=" alice 12    is a girl! "
print(mysp.split())     # split as blanks, as a list
print(len(mysp.split()))

try:
	with open("alice.txt") as f1:
		contents=f1.read()
except FileNotFoundError:
	pass                         # do nothing
else:
	mysplit=contents.split()
	print(len(mysplit))

import math
print(math.sqrt(16))

from random import sample
print(sample(range(1,100),24))

from statistics import mean,median
print(mean([2,3,5]))
print(median([2,3,5]))













