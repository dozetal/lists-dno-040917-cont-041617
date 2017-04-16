def foods_in_common(a, b):

	# a = [1, 2, 3, 4, 5, 6, 7, 8]
	# b = [12, 11, 10, 9, 8, 7, 6, 5]

	result = list(set(a).intersection(set(b)))

	# Uncomment this to print / check output
	# print sorted(result)

	return (result)

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [12, 11, 10, 9, 8, 7, 6, 5]

foods_in_common(a,b)
