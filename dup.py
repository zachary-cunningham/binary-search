# checks adjacent, not thorough all per word

def remove_dups(DATA):
	data = DATA[:]
	res = []

	if len(data) > 0:

		fresh = data[0]
		i = 1

		while (i <= len(data)-1):
			if (data[i] != fresh):
				res.append(fresh)
				fresh = data[i]
			i = i + 1
		res.append(fresh)
	return res

# print(remove_dups([1, 2, 2, 3, 3, 4, 5]))

def get_diff(DATA):
	return len(remove_dups(DATA))

# list = [["Animal", "Cat"], ["Dog"]]
# list[0] = ["Animal", "Cat"]
# list[0][1] = "Cat"

def sortt(DATA):
	data = DATA[:]
	i = 0

	while (i < len(data)-1):
		if ((data[i][0] > data[i+1][0])
	  		or data[i][0] == data[i+1][0] and (data[i][1] > data[i+1][1])):
			data[i], data[i+1] = data[i+1], data[i]

			print("jumped back to start")

		i += 1
	return data
