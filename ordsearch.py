import search
import importlib
importlib.reload(search)

def linear(data, value):
	"""Return the index of 'value' in 'data', or -1 if it does not occur"""
	# Go through the data list from index 0 upwards
	i = 0
	# continue until value found or index outside valid range

	# not (data[i] > value)
	while i < len(data) and data[i] != value and data[i] < value:
		# increase the index to go to the next data value
		i = i + 1
		print(i)
		# test if we have found the value
	
	if data[i] > value:
		return 'gave up early, im tired boss'
	if i == len(data):
		# no, we went outside valid range; return -1
		return 'does not occur'
	else:
		# yes, we found the value; return the index
		return i

def binary(data, value):
	low = 0
	high = len(data) - 1

	while True:
		if low > high:
			return "value not found!"

		middle = (high + low ) // 2
		if data[middle] == value:
			return middle
		elif data[middle] > value:
			high = middle - 1
		else:
			low = middle + 1

		