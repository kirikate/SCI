from serlib import *
import re
import inspect

path = "/home/user/Documents/SCI/Lab3/"


class Sass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__hop = "hop" + a
        self.__poh = "jej" + str(b)

    def method(self):
        return self.a + str(self.b)

    def ppp(self, c):
        print(str(c) + self.a + str(self.b))

        """
        format:
        {
            "type":"typename",
            "type properties":{...},
            //"field":value
        }
        """


def f():
    print(8)
    h = 7 + 7.4
    print(h)
    return "kikiki"


def main():
    # d = {"one": 1, "string": "str", "float": 1.25, "bool": False,
    #      "set": {1, 2, 3}, "list": [], "tuple": (1, 2, 3), 'empty dict': {}}
    # ser = serialize(d)
    # print(ser)
    # print("\n\n")
    # print(deserialize(ser))
    src = inspect.getsource(f)
    print(src)
    rv = None

    # def sf(param):
    #     nonlocal rv
    #     rv = param
    # src = src + '\nsf(f())'
    # rv = 1
    # exec(src, {'sf': sf})
    # print("rv" + rv)

    f_str = serialize(f)
    # f_str = type(f)
    print(f_str)
    smth = deserialize(f_str)
    print(smth())


if __name__ == "__main__":
    main()