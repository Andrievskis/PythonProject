from time import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Автоматически логирует начало и конец выполнения
    функции, а также ее результаты или возникшие ошибки. Декоратор принимает необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль)."""

    def decorator(function: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time()
            try:
                result = function(*args, **kwargs)
                end_time = time()
                print(f"Time {function.__name__}: {end_time - start_time:.6f}. Result: {result}")
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} ok\n")
                else:
                    print(f"{function.__name__} ok")
                return result
            except Exception as e:
                error_message = f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}."
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{error_message}\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator


@log()
def my_function(x: int, y: int) -> int:
    return x + y


# my_function(1, 3)
# my_function(1, "3")

# @log(filename="mylog.txt")
# def my_function(x: int, y: int) -> int:
#     return x + y

# my_function(1, 3)
# my_function(1, "3")
