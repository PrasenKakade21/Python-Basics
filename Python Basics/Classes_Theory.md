### 1. Classes and Objects:
- **Classes**: In Python, a class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that each object of the class will have. Classes are defined using the `class` keyword followed by the class name and a colon.

- **Objects**: An object is an instance of a class. It represents a specific instance with its own unique attributes and behaviors. Objects are created by calling the class name followed by parentheses containing any necessary arguments to initialize the object.

**Code Example**:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
```

**Additional Resources**:
- [Python Classes and Objects - W3Schools](https://www.w3schools.com/python/python_classes.asp)
- [Object-Oriented Programming (OOP) in Python 3 - Real Python](https://realpython.com/python3-object-oriented-programming/)

### 2. Attributes:
- **Attributes**: Attributes are variables that store data within an object. They define the state of an object and can be accessed using dot notation (`object.attribute`).

- **Instance Attributes**: Instance attributes are specific to each instance of a class. They are defined within the class's `__init__` method using the `self` keyword.

- **Class Attributes**: Class attributes are shared among all instances of a class. They are defined outside any method within the class.

**Code Example**:
```python
class Circle:
    pi = 3.14  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

# Accessing attributes
circle1 = Circle(5)
print(circle1.radius)  # Output: 5
print(Circle.pi)       # Output: 3.14
```

**Additional Resources**:
- [Python Attributes and Methods - LearnPython.org](https://www.learnpython.org/en/Attributes_and_Methods)

### 3. Methods:
- **Methods**: Methods are functions defined within a class that operate on the attributes of the class. They define the behavior of objects and can be called using dot notation (`object.method()`).

- **Instance Methods**: Instance methods are defined within a class and operate on the instance attributes of the class.

- **Class Methods**: Class methods are defined using the `@classmethod` decorator and operate on class attributes rather than instance attributes.

**Code Example**:
```python
class MyClass:
    def instance_method(self):
        print("Instance method")

    @classmethod
    def class_method(cls):
        print("Class method")

# Calling methods
obj = MyClass()
obj.instance_method()  # Output: Instance method
MyClass.class_method()  # Output: Class method
```

**Additional Resources**:
- [Python Methods - Programiz](https://www.programiz.com/python-programming/methods)

### 4. Instantiation:
- **Instantiation**: Instantiation is the process of creating an object (instance) of a class. It involves calling the class name followed by any necessary arguments to initialize the object.

**Code Example**:
```python
class Dog:
    def __init__(self, name):
        self.name = name

# Creating objects (instances)
dog1 = Dog("Buddy")
dog2 = Dog("Max")
```

**Additional Resources**:
- [Instantiating Objects - Real Python](https://realpython.com/python3-object-oriented-programming/#instantiating-objects)

### 5. Inheritance:
- **Inheritance**: Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass). It promotes code reusability and allows for the creation of specialized classes that extend the functionality of the base class.

**Code Example**:
```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Woof")

# Creating objects
dog = Dog()
dog.sound()  # Output: Animal sound
dog.bark()   # Output: Woof
```

**Additional Resources**:
- [Inheritance in Python - GeeksforGeeks](https://www.geeksforgeeks.org/inheritance-in-python/)

### 6. Encapsulation:
- **Encapsulation**: Encapsulation is the concept of bundling data (attributes) and methods within a single unit (class). It hides the internal state of an object from outside access, promoting data abstraction and information hiding.

**Code Example**:
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Encapsulation using single underscore

    def get_balance(self):
        return self

._balance

# Creating object
account = BankAccount(1000)
print(account.get_balance())  # Output: 1000
```

**Additional Resources**:
- [Encapsulation in Python - GeeksforGeeks](https://www.geeksforgeeks.org/encapsulation-in-python/)

### 7. Polymorphism:
- **Polymorphism**: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables code to be written in a generic manner that operates on objects of various types, promoting flexibility and code reuse.

**Code Example**:
```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Function that uses polymorphism
def make_sound(animal):
    animal.sound()

# Creating objects
dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Woof
make_sound(cat)  # Output: Meow
```

**Additional Resources**:
- [Polymorphism in Python - Real Python](https://realpython.com/inheritance-composition-python/#polymorphism-in-python)

Understanding these concepts and practicing with code examples will solidify your understanding of object-oriented programming in Python. Further exploration through the provided additional resources will enhance your knowledge and proficiency.
