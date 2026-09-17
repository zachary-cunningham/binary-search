# <!-- Question 5.5. Implement a function ordsearch.binary_pairs that, given an or-
# dered list of pairs and a value, looks for this value as first element of a pair and
# returns the index of that pair in the list, or -1 if the value does not occur in the list.
# For example:
# >>> x = [["Anne",7],["John",5],["Pete",9]]
# >>> ordsearch.binary_pairs(x,"Brenda")
# -1
# >>> ord -->

def binary_pairs(data, value):
	result = data[:]

	i = 0
	while (i < len(result)):
		if data[i][0] == value:
			return i
		else:
			return -1

	i += 1

print(binary_pairs([["Anne",7],["John",5],["Pete",9]], "John"))