# Nested function

# def main_function():
#     print("I am the main function")
#
#     def secondary_function():
#         print("I am the secondary function")
#
#     return secondary_function()
#
#
# main_function()


# Nested function with function taken as parameter
# def print_hello():
#     print("Hello")
#
#
# def main_function(func):
#     print("I am the main function")
#
#     def secondary_function():
#         print("I am the secondary function")
#         return func()
#
#     return secondary_function()
#
#
# main_function(print_hello)


""" Decorator example -> decorated function is passed as
 an argument to the main function and wrapper is returned
"""

# def main_function(func):
#     print("I am the main function")
#
#     def secondary_function():
#         print("I am the secondary function")
#         return func()
#
#     return secondary_function
#
#
# @main_function
# def decorated_function(*args, **kwargs):
#     print("Hello")
#
# decorated_function()


""" Double decorated function"""

# def main_function(func):
#     print("I am the main function")
#
#     def secondary_function():
#         print("I am the secondary function")
#         return func()
#
#     return secondary_function
#
#
# @main_function
# @main_function
# def decorated_function(*args, **kwargs):
#     print("Hello")
#
#
# decorated_function()
#
""" Example of decorator class and passing function arguments inside the decorator"""


def main_function(func):
    print("I am the main function")

    def secondary_function():
        print("I am the secondary function")
        return func()

    return secondary_function


class decorator_class:

    def __init__(self, func, func2):
        self.func1 = func
        self.func2 = func2

    def __call__(self, wrapper_func):
        return self.wrapper_func

    def wrapper_func(self):
        return self.func1(self.func2)

    def __str__(self):
        return f"{decorator_class.__name__}"

    def __repr__(self):
        return


def decorated_function2():
    print("hello2")


def decorated_function(func):
    return func()


@main_function
@decorator_class(func=decorated_function, func2=decorated_function2)
def _wrapper():
    print("hello")


_wrapper()


""" Example of passing arguments to the wrapper function"""

# def main_function(func):
#     print("I am the main function")
#
#     def secondary_function(func1, func2):
#
#         print("I am the secondary function")
#         return func1(func2)
#
#     return secondary_function
#
#
# class decorator_class:
#
#     def __init__(self, orig_func):
#         self.orig_func = orig_func
#
#     def __call__(self):
#         self.orig_func()
#
#     def __str__(self):
#         return f"{decorator_class.__name__}"
#
#     def __repr__(self):
#         return
#
#
# def decorated_function2():
#     print("hello2")
#
#
# def decorated_function(func):
#     return func()
#
#
# @main_function
# @decorator_class
# def _wrapper():
#     print("Hello")
#
#
# _wrapper(decorated_function, decorated_function2)
