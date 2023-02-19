res = ""
with open('en.txt', 'r') as f:
	for line in f:
		res += chr(eval(line.strip()))
print(res)
