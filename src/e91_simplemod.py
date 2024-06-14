# e91_simplemod.py

import pprint
import sys

x = 42  # A global variable


# A simple function
def foo():
    print("x is", x)


# A simple class
class Spam:
    def yow(self):
        print("More Yow!")


# A scripting statement
print("Loaded simplemod")

if __name__ == "__main__":
    pprint.pprint(list(sys.modules))
    pass
