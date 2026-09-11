import time


def merge(data):
	result = data[:]
	start = time.process_time()

	if len(result) <=1: 
		end = time.process_time()

		duration = round((end - start) * 1000000)  
		return result, duration

	else:
		fst = merge (result [:(len(result) // 2)])
		snd = merge (result [(len(result) // 2):]) 
		# check above
		res = []
		fi = 0
		si = 0
		 
		while (fi <= (len(fst) - 1)) and (si <= (len(snd) - 1)):
			if (fst[fi]) < (snd[si]):
				res.append(fst[fi])
				fi = fi + 1
			else: 
				res.append(snd[si])
				si = si + 1
		if fi <= (len(fst) - 1):
			res.extend(fst[fi:])
		else:
			res.extend(snd[si:])

	end = time.process_time()

	duration = round((end - start) * 1000000)
	return res, duration