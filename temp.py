def map(func, values):
    return [func(x) for x in values]


def reduce(func, values, initial=0):
    result = initial
    for n in values:
        result = func(n, result)
    return result


def sum(x, y):
    return x + y


def square(x):
    return x * x


nums = [1, 2, 3, 4]
result = reduce(sum, map(square, nums))

type()