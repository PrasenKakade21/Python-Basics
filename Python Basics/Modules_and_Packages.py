# Importing modules
import math
print("Square root of 16:", math.sqrt(16))  # Output: Square root of 16: 4.0

# Renaming modules
import datetime as dt
print("Current date:", dt.date.today())  # Output: Current date: YYYY-MM-DD

# Importing specific items from modules
from random import randint
print("Random number between 1 and 10:", randint(1, 10))

# Importing all items from a module (not recommended)
from random import *
print("Another random number between 1 and 10:", randint(1, 10))

# Creating a module
# Save the following code in a file named mymodule.py
"""
def greet(name):
    print("Hello,", name)
"""

# Importing a user-defined module
import mymodule
mymodule.greet("Alice")  # Output: Hello, Alice

# Creating a package
# Create a directory named mypackage
# Inside mypackage, create a file named __init__.py and another file named mymodule.py with the following content:
"""
def greet(name):
    print("Hello,", name)
"""

# Importing a module from a package
from mypackage import mymodule
mymodule.greet("Bob")  # Output: Hello, Bob

# Importing a module from a subpackage
# Create a subdirectory named subpackage inside mypackage
# Inside subpackage, create a file named __init__.py and another file named mysubmodule.py with the following content:
"""
def greet(name):
    print("Hi,", name)
"""

# Importing a module from a subpackage
from mypackage.subpackage import mysubmodule
mysubmodule.greet("Charlie")  # Output: Hi, Charlie
