#default values

# def my_function(b, a=1, c=3):
#     return a+b+c


# a= my_function(4)
# print(a)

# *args

# def add(*args):
#     result = 0
#     #*args:tuple
#     for n in args:
#         print(n)
#         result += n
#     return result

# answer = add(1,2,3,4,5,6,7,8,9,10)
# print(answer)

# **kwargs

# def calculate(n, **kwargs):
#     # print(kwargs) #dictionary
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)


# calculate(3, multiply = 5, add = 2)


class Car:
    def __init__(self, **kwargs):
        self. make = kwargs['make']
        self. model = kwargs['model']

my_car = Car(make = 'Nissan', model = 'ST-R')
print(my_car)