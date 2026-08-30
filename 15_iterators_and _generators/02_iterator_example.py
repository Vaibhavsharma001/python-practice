#reating your own iterator

class Counter:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


counter = Counter(5)

for x in counter:
    print(x)