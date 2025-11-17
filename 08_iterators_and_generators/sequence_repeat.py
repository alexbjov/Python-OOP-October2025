class sequence_repeat:
	def __init__(self, sequence, number):
		self.sequence = sequence
		self.number = number
		self.x = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.x < self.number:
			x = self.x % len(self.sequence)
			self.x += 1
			return self.sequence[x]
		else:
			raise StopIteration


# result = sequence_repeat('abc', 5)
# for item in result:
# 	print(item, end='')

result = sequence_repeat('I Love Python', 3)
for item in result:
	print(item, end='')
