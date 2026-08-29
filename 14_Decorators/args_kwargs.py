def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Function is starting...")

        result = func(*args, **kwargs)

        print("Function is finished!")

        return result

    return wrapper


@my_decorator
def introduce(name, age, city="Delhi"):
    print(f"My name is {name}, I am {age} years old, and I live in {city}.")


introduce("Vaibhav", 20, city="Panipat")