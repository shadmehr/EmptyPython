""" this is an example for decorator pattern in python"""
from functools import wraps


def blink_print(fuction):

    @wraps(fuction)
    def decorator():
        """this is new

        Returns:
            [type]: [description]
        """
        ret = fuction()
        return "<blink>" + str(ret) + "</blink>"

    return decorator


@blink_print
def m1():
    """This is hello world

    Returns:
        str: helo world
    """
    return "Hello World"


print(m1())
print(m1.__name__)
print(m1.__doc__)
