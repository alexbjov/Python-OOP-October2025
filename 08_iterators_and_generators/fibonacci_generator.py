def fibonacci():
	current_num = 0
	next_num = 1
	while True:
		yield current_num
		current_num, next_num = next_num, current_num + next_num


generator = fibonacci()
for i in range(10):
	print(next(generator))
