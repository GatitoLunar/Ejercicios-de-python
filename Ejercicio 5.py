def my_sum(entrada):
	total = 0.0
	for item in entrada:
		total += item
	return total

def multi(entrada):
	total = 1.0
	for item in entrada:
		total *= item
	return total

multi([2,3,5,8,4,3])