

#args and kwargs?

#  *args (Non Keyword Arguments)
#  **kwargs (Keyword Arguments)

"""
*args and **kwargs are special keyword which allows function to take variable length argument.
*args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed.
**kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
*args and **kwargs make the function flexible.
"""

class ObjectC(object):
    def what_are_the_vars(cls):
        new_instance = cls()
        return new_instance

    def __init__(self, initX):
        self.x = initX

    def doom_printer(obj):
        if obj is None:
            print("ERROR")
            print("end")
            return
        for attr in dir(obj):
            if attr[0] != "_":
                value = getattr(obj, attr)
                print("{}: {}".format(attr, value))
    print("end")

    def getattr(object, attribute, default):

#setattr : setattr(object, attribute, value)

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
doom_printer(obj)


#getattr: getattr(object, attribute, default)

#setattr : setattr(object, attribute, value)