import random

def generate_random_list(min_value: int, max_value: int, list_size: int) -> list:
    if list_size < 0:
        raise ValueError("Size of the list must be non-negative.")
    return [random.randint(min_value, max_value) for _ in range(list_size)]