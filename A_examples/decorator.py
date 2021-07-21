def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args!r}, {kwargs!r}) -> {result!r}")
        return result

    return wrapper


@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


# @trace
# fibonacci = trace(fibonacci)

@trace
def test(*args, **kwargs):
    path = ["ab", "v", "c"]
    "".join(path)

    str1 = "".join(str(v) for v in args)
    print(str1)


# fibonacci(4)
path = ["ab", "v", "c"]
my_kyargs = {
    'number': 20,
    'divisor': 7
}
test(*path,**my_kyargs)
