import serlib
import re
import inspect
import math
import sys
import os.path
import importlib
import types

path = "/home/user/Documents/SCI/Lab3/"


def funcuc():
    cl_var = None

    def uhuhu():
        nonlocal cl_var

    return uhuhu


Cell = type(funcuc().__closure__[0])


class Sass:
    def __init__(self, a: str, b: int):
        self.a = a
        self.b = b
        self.__hop = "hop" + a
        self.__poh = "jej" + str(b)

    def method(self):
        return self.a + str(self.b)

    def ppp(self, c: int):
        print(str(c) + self.a + str(self.b))

        """
        format:
        {
            "type":"typename",
            "type properties":{...},
            //"field":value
        }
        """

    def __add__(self, other):
        return 1

    def __private(self):
        print("private")

    def _protected(self):
        print("protected")

    def prpuk(self):
        print(self.__puk)


def dec(func):
    def d(*args):
        print("it's decoratin' time")
        return func(*args)

    return d


i = 5


# @dec


def print_tuple_list(d: list):
    for k, v in d:
        print(str(k) + " : " + str(v))


def print_dict(d: dict):
    for k, v in d.items():
        print(str(k) + " : " + str(v))


def func(a, b):
    print(a - b)


def main():
    t = 0

    @dec
    def f(a: int):
        print(8)
        h = 7 + 7.4
        print(h)
        print(i)
        print(math.sin(i * a + t))
        return "kikiki"

    # types.CodeType()
    sass_str = serlib.serialize(Sass)
    print(sass_str)
    sass = serlib.deserialize(sass_str)
    s = sass("a", 2)
    print(s.method())
    print(s.ppp(8))
    print(s._Sass__private())
    print(s._protected())


if __name__ == "__main__":
    main()
