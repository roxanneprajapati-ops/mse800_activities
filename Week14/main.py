def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def subtract(a, b):
    return b - a

@log_decorator
def multiply(a, b):
    return a * b

@log_decorator
def divide(a, b):
    return a / b

def main():
    add(a=3, b=5)
    multiply(3,5)
    subtract(b=5, a=3)


if __name__ == "__main__":
    main()