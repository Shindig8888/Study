# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

#first-class object

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)

# result = calculate(add, 1, 2)
# print(result)

#nested function
# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     nested_function()

# outer_function()

#nested return
# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     return nested_function

# result = outer_function()
# result()


#python decorator
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("bye")

@delay_decorator
def say_greetingf():
    print("greetinf")

say_hello()