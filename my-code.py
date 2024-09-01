def add_numbers(num1, num2):
    return num1 + num2

def is_even(number):
    return number % 2 == 0

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text if char in vowels)

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

def run_tests():
    print("Testing add_numbers:")
    print(add_numbers(6, 3))

    print("\nTesting is_even:")
    print(is_even(4))
    print(is_even(7))

    print("\nTesting reverse_string:")
    print(reverse_string("hello"))

    print("\nTesting count_vowels:")
    print(count_vowels("hello world"))

    print("\nTesting calculate_factorial:")
    print(calculate_factorial(6))
    print(calculate_factorial(0))

    print("\nTesting sort_by_age:")
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print(sort_by_age(people))

    print("\nTesting merge_dicts:")
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    print(merge_dicts(dict1, dict2))

    print("\nTesting Car class:")
    my_car = Car("BMW", "Mercedes", 2023)
    my_car.display_info()

    print("\nTesting apply_decorator:")
    @apply_decorator
    def greet(name):
        print(f"Hello, {name}")

    greet("Alice")

if __name__ == "__main__":
    run_tests()
