class dictionary_iter:
	def __init__(self, my_dict: dict):
		self.dict_tuple = tuple(my_dict.items())
		self.counter = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.counter < len(self.dict_tuple):
			x = self.counter
			self.counter += 1
			return self.dict_tuple[x]
		else:
			raise StopIteration


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
# 	print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
	print(x)
