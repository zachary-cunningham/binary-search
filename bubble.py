def bubble (data):
	result = data[:]
	ui = len(result)-1

	while ui > 0:
		si = 0
		i = 0
		while i < ui:
			if result[i] > result[i + 1]:
				result[i], result[i+1] = result[i+1], result[i]
				si = i
			i = i + 1
		ui = si
	return result

# • lines(filename): returns a list containing all individual lines in the file
# • words(filename): returns a list containing all individual words in the file
# You can now for instance type (in the interpreter):
# >>> from ordsearch import binary
# >>> from util import lines
# >>> binary(lines("Unabr.dict"),"eagle")