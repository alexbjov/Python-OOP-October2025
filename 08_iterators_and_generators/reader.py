def read_next(*collections):
    for collection in collections:
        for element in collection:
            yield element


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
