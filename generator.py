

def generator(n):
    for x in range(n):
        yield x ** 3;


value = generator(100);
print(next(value));
print(next(value));
print(next(value));
print(next(value));
print(next(value));

