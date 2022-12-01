
max = 0

with open("input1.txt") as f:
	lines = f.readlines()

#	print(lines)

	running_total = 0
	for line in lines:
#		print(line[:-1])
#		print(type(line[:-1]))
		if line[:-1].find("\n") == -1 and line[:-1] != "":
			num = line[:-1]
#			print(num)
			running_total += int(num)
		else:
			if running_total > max:
				max = running_total
			running_total = 0
	if running_total > max:
		max = running_total
print(max)
