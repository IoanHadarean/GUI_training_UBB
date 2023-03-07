def define_local_value():
    """ Here we define the local variable x = 20 in define_local_value and in define_global_value we define another x
    which can be accessed only globally (outside of function) -> break encapsulation """
    x = 5

    def define_global_value():
        global x
        x = 25

    print(f"{x} before calling global value")
    define_global_value()
    print(f"{x} after calling global value")


define_local_value()
print("{} as it is defined globally".format(x))


def outer_bound_function():
    """ Nonlocal keyword has to exist in the outer scope (bound scope)  and it can not be assigned"""
    variable = 0

    def inline_bound_function():
        nonlocal variable
        variable = 10

    print(f"We defined variable = {variable} here")
    inline_bound_function()
    print(f"We modified value of variable that is defined in the outer bound function and now the value is {variable}")


outer_bound_function()


def func_with_args_and_kwargs(*args, **kwargs):
    """A function with *args as a parameter can have any number of arguments, and with **kwargs as a parameter any number
    of keyword arguments """
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)


a = 2
func_with_args_and_kwargs('3', 1, a, is_func=True, rush_b=True)

""" Merge dictionaries """

d1 = {"A": 10, "B": 20, "C": 30}
d2 = {"X": 100, "Y": 200, "Z": 300}


d3 = {**d1, **d2}
print(d3)


""" Partial unpacking """

l1 = (1, 2, 3, 4, 5)
a, b, c, d, e = l1
print(a, b, c, d, e)
a, *b, c = l1
print(a, b, c)