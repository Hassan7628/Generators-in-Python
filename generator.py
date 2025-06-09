from sys import getsizeof
from time import sleep

list1 = [1, 2, 3, 4, 5]  # takes storage in the memory
print(f"list1 size: {getsizeof(list1)}")

print(
    f"range(1,6) size: {getsizeof(range(1,6))}\n"
)  # It is a lazy iterator it pause the program returns one value at a time than repeats the program.


""" We can test it by using sleep function, if the program saves all the values 
it should print them at once but if it doesnt it will apply the sleep function
after each iteration. """

for i in range(1, 6):
    sleep(0.1)
    print(i)


print("\n\n")

# Working:
fruits = ["apple", "banana", "cherry", "pineapple", "melon"]  # it's an iterable

""" An iterable is like a book — it can be read one page at a time.
An iterator is like a bookmark — it remembers the current page you're on. """

fruit_iterator = iter(
    fruits
)  # gets the iterator from list or you can say makes it iterator

print(next(fruit_iterator))  # returns item one at a time
print(next(fruit_iterator))

# Since in a for loop the same things happen it will only print the remaining  objects.
print("for loop starts")  # we can test it.
for i in fruit_iterator:
    print(i)


print("\n\n")

# map function also does the same thing.
y = map(lambda x: x**2, range(1, 6))

print(next(y))
print(next(y))
print(next(y))

print(f"\nIn a list: {list(y)}\n")


# Behind the scene of how for loop works:
num = [11, 22, 33, 44]

it = iter(num)
while True:
    try:
        print(next(it))

    except StopIteration:
        break


print("\n\n")


# Let's see how we can loop over our custom created objects:
class Loop:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self  # we need to make the object an iterator

    def __next__(self):
        if self.index < len(self.iterable):
            result = self.iterable[self.index]
            self.index += 1
            return result

        else:
            raise StopIteration  # This is the old legacy way of creating loop


obj = Loop("name")

for i in obj:
    print(i)


print("\n\n")

# Now let's see how we can do the same thing using generators:


def gen(n):
    for i in range(n):
        yield i  # Yield pauses the program and returns the value and then go back to the program and reapeat the same process.


for i in gen(5):
    print(i)


print("\n\n")


# Now let's implement it in a class:
class Num:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self.generator()

    def generator(self):
        for i in range(self.iterable):
            yield i


num1 = Num(6)
for i in num1:
    print(i)