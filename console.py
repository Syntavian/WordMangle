def print_wrap(func):
    def wrapper(*args):
        print()
        result = func(*args)
        print()
        return result

    return wrapper


@print_wrap
def print_outputs(_results: list[str]):
    print()

    for i in range(0, len(_results), 5):
        print(*_results[i : i + 5])

    print()


@print_wrap
def print_error(_error_message: str):
    print(f"Error: {_error_message}")
