class countdown_iterator:
	def __init__(self, count: int):
		self.count = count
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.count >= 0:
			x = self.count
			self.count -= 1
			return x
		else:
			raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
	print(item, end=" ")
