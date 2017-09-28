import re

fhand = open("mbox-short.txt")

for line in fhand:
	line = line.rstrip()
	if re.search("^From",line):
		print("********PART A***********", line)

lst = list()
for line in fhand:
	line = line.rstrip()
	lst = re.findall("^From ([0-9]*)", line)
	print(re.findall("^From ([0-9]*)", line))
print("**********PART B**********", lst)