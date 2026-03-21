import time
def log_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end = time.time()
            log = f"{func.__name__} called with {args}, {kwargs} -> Result: {result}, Time: {end-start:.6f}s\n"
            print(log)

            with open("function_logs.txt", "a") as f:
                f.write(log)

            return result

        except Exception as e:
            end_time = time.time()
            execution_time = end_time - start_time

            error_message = (
                f"Function: {func.__name__}\n"
                f"Arguments: args={args}, kwargs={kwargs}\n"
                f"Error: {e}\n"
                f"Execution time before error: {execution_time:.6f} seconds\n"
                f"{'-' * 40}\n"
            )

            print(error_message)

            with open("function_logs.txt", "a") as file:
                file.write(error_message)

            return None
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

@log_decorator
def display_message(greeting, name):
    print(f"{greeting} {name}")

def main():
    add(a=3, b=5)
    multiply(3,5)
    subtract(b=5, a=3)

    data = {'greeting': "Good morning", 'name': "Roxanne"}
    display_message(**data)


if __name__ == "__main__":
    main()