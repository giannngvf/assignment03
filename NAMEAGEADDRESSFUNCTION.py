def get_name():
    name_function = input("Enter your name: ")
    return name_function

def get_age():
    age_function = input("Enter your age: ")
    return age_function

def get_address():
    address_function = input("Enter your address: ")
    return address_function

def display_output(name_function, age_function, address_function):
    output_function = print(f"Hi, my name is {name}. I am {age} years old and I live in {address}.")

name = get_name()
age = get_age()
address = get_address()
display_output(name, age, address)