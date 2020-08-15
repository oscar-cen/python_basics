
with open('pi.txt') as f1:
	contents=f1.read()
#	print(contents)                   # one blank line at the end, should be omitted
	print(contents.rstrip())          # rstrip: delete huanhangfu (file has it automatically for each line)
	
with open('pi.txt') as f1:
	for line in f1:
		print(line.rstrip())

with open('pi.txt') as f1:
	lines=f1.readlines()              # lines is a list
for line in lines:
	print(line.rstrip())
 

with open('pi.txt') as f1:
	lines=f1.readlines()  
pi_s=""
for line in lines:
	pi_s+=line.strip()
print(pi_s[:3])
print(pi_s)
print(len(pi_s))
if '268' in pi_s:
	print('pass')
else:
	print('fail')

with open("write.txt",'w') as w1:               # 'r+':can both read and write      default: read only   'a':add sth.
	w1.write("I love programming!\n")
	w1.write("multiple.\n")


with open("write.txt",'a') as w1:               # 'r+':can both read and write      default: read only   'a':add sth.
	w1.write("I also love u!\n")
	w1.write("u_multiple.\n")


















