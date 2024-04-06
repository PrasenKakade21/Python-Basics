# Define a class MyClass
class MyClass:
    # Constructor to initialize attributes
    def __init__(self, x, y):
        self._x = x  # Protected attribute
        self.__y = y  # Private attribute

    # Method to perform addition
    def add(self):
        return self._x + self.__y

# Define a subclass MySubClass inheriting from MyClass
class MySubClass(MyClass):
    # Method to perform subtraction
    def subtract(self):
        return self._x - self.__y

# Define a class Dog
class Dog:
    # Method to make a dog speak
    def speak(self):
        return "Woof!"

# Define a class Cat
class Cat:
    # Method to make a cat speak
    def speak(self):
        return "Meow!"

# Function to demonstrate polymorphism
def animal_speak(animal):
    return animal.speak()

# Instantiation and usage
obj = MyClass(3, 4)  # Create an object of MyClass
sub_obj = MySubClass(5, 2)  # Create an object of MySubClass
dog = Dog()  # Create an object of Dog
cat = Cat()  # Create an object of Cat

# Accessing attributes and calling methods
print("Object attributes:")
print(obj._x)  # Output: 3 (protected attribute)
# print(obj.__y)  # This would raise an AttributeError (private attribute)
print("Object method:")
print(obj.add())  # Output: 7

# Inheritance
print("Subclass attributes and methods:")
print(sub_obj._x)  # Output: 5
# print(sub_obj.__y)  # This would raise an AttributeError (private attribute)
print(sub_obj.subtract())  # Output: 3

# Polymorphism
print("Polymorphism:")
print(animal_speak(dog))  # Output: Woof!
print(animal_speak(cat))  # Output: Meow!


'''

1. **Classes and Objects**:
   - Classes are blueprints for creating objects, which are instances of a class. 
   - Objects have attributes (variables) and methods (functions) associated with them.

2. **Attributes**:
   - Attributes are variables that store data within an object.
   - They define the state of an object and can be accessed using dot notation (`object.attribute`).

3. **Methods**:
   - Methods are functions defined within a class that operate on the attributes of the class.
   - They define the behavior of an object and can be called using dot notation (`object.method()`).

4. **Instantiation**:
   - Instantiation is the process of creating an object (instance) of a class.
   - It involves calling the class name followed by any necessary arguments to initialize the object.

5. **Inheritance**:
   - Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass).
   - It promotes code reusability and allows for the creation of specialized classes that extend the functionality of the base class.

6. **Encapsulation**:
   - Encapsulation is the concept of bundling data (attributes) and methods that operate on the data within a single unit (class).
   - It hides the internal state of an object from outside access, promoting data abstraction and information hiding.

7. **Polymorphism**:
   - Polymorphism allows objects of different classes to be treated as objects of a common superclass.
   - It enables code to be written in a generic manner that operates on objects of various types, promoting flexibility and code reuse.

Understanding these concepts is essential for writing object-oriented code in Python and building complex software systems. By utilizing classes and objects effectively, developers can create modular, maintainable, and scalable codebases that are easier to understand and extend.

'''


