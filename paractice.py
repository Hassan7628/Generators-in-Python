# Legacy:
class It:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            result = self.iterable[self.index]
            self.index += 1
            return result

        else:
            raise StopIteration


obj1 = It("apple")
for i in obj1:
    print(i)


print()


# New version:
class Loop:
    def __init__(self, iteration):
        self.iteration = iteration

    def __iter__(self):
        for i in self.iteration:
            yield i


loop1 = Loop("apple")
for i in loop1:
    print(i)


print("\n\n")

num = [11, 22, 33, 44]

it = iter(num)
print(next(it))
print(next(it))
print(next(it))