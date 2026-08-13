# Python OOP Challenge: 30 Problem-Solving Questions

This document contains 30 problem-solving questions designed to challenge and deepen your understanding of Object-Oriented Programming (OOP) concepts in Python.

---

## Easy Level (Questions 1â€“10)

### Question 1: Basic Class and Object
Create a `Car` class with attributes `brand` and `year`. Instantiate two objects and print their details.

**Expected Output:**
```
Brand: Toyota, Year: 2020
Brand: Honda, Year: 2019
```

---

### Question 2: Constructor with Default Values
Create a `Student` class where the constructor accepts `name` and `grade`, with `grade` defaulting to `"A"`. Create objects with and without providing the grade.

**Expected Output:**
```
Alice - Grade: A
Bob - Grade: B
```

---

### Question 3: Instance Methods
Create a `Rectangle` class with `width` and `height`. Add a method `area()` that returns the area of the rectangle.

**Expected Output:**
```
Area: 50
```

---

### Question 4: String Representation
Create a `Book` class with `title` and `author`. Override the `__str__` method so that printing the object shows a readable format.

**Expected Output:**
```
Book: 1984 by George Orwell
```

---

### Question 5: Class vs Instance Attributes
Create a `Dog` class with a class attribute `species = "Canis familiaris"` and an instance attribute `name`. Show that all instances share the class attribute.

**Expected Output:**
```
Buddy: Canis familiaris
Max: Canis familiaris
```

---

### Question 6: Modifying Instance Attributes
Create a `BankAccount` class with `balance`. Add methods `deposit(amount)` and `withdraw(amount)` that modify the balance.

**Expected Output:**
```
Balance after deposit: 1500
Balance after withdrawal: 1200
```

---

### Question 7: Private Attributes (Name Mangling)
Create a `Person` class with a "private" attribute `__age`. Provide a public method `get_age()` to access it.

**Expected Output:**
```
Age: 25
```

---

### Question 8: Simple Inheritance
Create a base class `Animal` with a method `speak()` that prints "Some sound". Create a derived class `Cat` that overrides `speak()` to print "Meow".

**Expected Output:**
```
Some sound
Meow
```

---

### Question 9: Using `super()` in Inheritance
Create a `Vehicle` class with `__init__` accepting `brand`. Create a `Bike` class that inherits from `Vehicle` and adds a `type` attribute. Use `super()` to initialize `brand`.

**Expected Output:**
```
Brand: Yamaha, Type: Sports
```

---

### Question 10: Multiple Objects Tracking
Create a `Employee` class with a class variable `count` that tracks how many employees have been created. Increment it in the constructor.

**Expected Output:**
```
Total Employees: 3
```

---

## Medium Level (Questions 11â€“20)

### Question 11: Property Decorators
Create a `Temperature` class that stores temperature in Celsius internally. Use `@property` to provide a `fahrenheit` getter and `@fahrenheit.setter` to allow setting temperature via Fahrenheit.

**Expected Output:**
```
37Â°C = 98.6Â°F
Setting 100Â°F -> 37.78Â°C
```

---

### Question 12: Class Methods and Factory Methods
Create a `Date` class with `day`, `month`, `year`. Add a class method `from_string(cls, date_string)` that parses "DD-MM-YYYY" and returns a `Date` object.

**Expected Output:**
```
Date: 15-08-2023
```

---

### Question 13: Static Methods
Create a `MathUtils` class with a static method `is_even(n)` that returns `True` if `n` is even. Demonstrate calling it without creating an instance.

**Expected Output:**
```
4 is even: True
7 is even: False
```

---

### Question 14: Multiple Inheritance
Create classes `Flyer` (method `fly()`) and `Swimmer` (method `swim()`). Create a `Duck` class that inherits from both and can do both.

**Expected Output:**
```
Flying high!
Swimming deep!
```

---

### Question 15: Method Resolution Order (MRO)
Given classes `A`, `B(A)`, `C(A)`, `D(B, C)`, print the MRO of `D` and explain the diamond problem resolution.

**Expected Output:**
```
[<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

---

### Question 16: Abstract Base Class
Use the `abc` module to create an abstract class `Shape` with an abstract method `area()`. Create `Circle` and `Square` classes that implement `area()`.

**Expected Output:**
```
Circle Area: 78.54
Square Area: 16
```

---

### Question 17: Encapsulation with Getters/Setters
Create a `BankAccount` class with a private `__balance`. Implement getter and setter with validation (balance cannot be negative).

**Expected Output:**
```
Balance: 1000
Invalid balance! Setting to 0.
Balance: 0
```

---

### Question 18: Operator Overloading (`__add__`)
Create a `Vector` class with `x` and `y`. Overload the `+` operator so that two vectors can be added.

**Expected Output:**
```
Vector(1, 2) + Vector(3, 4) = Vector(4, 6)
```

---

### Question 19: `__len__` and `__getitem__` Overloading
Create a `Library` class that holds a list of books. Overload `__len__` to return the count of books and `__getitem__` to access a book by index.

**Expected Output:**
```
Total books: 3
First book: Python 101
```

---

### Question 20: Composition vs Inheritance
Create a `Engine` class and a `Car` class. Use **composition** (not inheritance) so that a `Car` "has an" `Engine`. The `Car` should be able to `start()` which calls the engine's `ignite()` method.

**Expected Output:**
```
Engine ignited!
Car started with V8 engine.
```

---

## Hard Level (Questions 21â€“30)

### Question 21: Custom Iterator
Create a `Countdown` class that takes a `start` value. Implement `__iter__` and `__next__` so it can be used in a `for` loop to count down to 0.

**Expected Output:**
```
5 4 3 2 1 0
```

---

### Question 22: Context Manager (`__enter__` and `__exit__`)
Create a `FileSafe` context manager class that prints "Opening file..." on enter and "Closing file..." on exit. Use it in a `with` statement.

**Expected Output:**
```
Opening file...
Processing file...
Closing file...
```

---

### Question 23: Metaclass Basics
Create a metaclass `SingletonMeta` that ensures only one instance of any class using it can exist. Apply it to a `Database` class.

**Expected Output:**
```
Both variables point to the same object: True
```

---

### Question 24: Descriptor Protocol
Create a `Validator` descriptor class that ensures an attribute is always a positive integer. Use it in a `Product` class for the `price` attribute.

**Expected Output:**
```
Price: 100
ValueError: Price must be a positive integer!
```

---

### Question 25: Custom Exception Hierarchy
Create a custom exception hierarchy: `PaymentError` (base), `InsufficientFundsError`, and `InvalidCardError`. Create a `PaymentProcessor` class that raises these exceptions appropriately.

**Expected Output:**
```
InsufficientFundsError: Balance too low.
```

---

### Question 26: Mixin Pattern
Create a `JSONSerializableMixin` that adds a `to_json()` method to any class. Create a `User` class that uses this mixin and converts its attributes to JSON.

**Expected Output:**
```
{"name": "Alice", "age": 30}
```

---

### Question 27: Proxy Pattern using `__getattr__`
Create a `LazyImage` proxy class that wraps an `Image` class. The actual `Image` object should only be created when an attribute is first accessed (lazy initialization).

**Expected Output:**
```
Image loaded lazily!
Image size: 1024x768
```

---

### Question 28: Observer Pattern
Implement the Observer pattern. Create a `NewsPublisher` class (subject) and a `Subscriber` class (observer). When the publisher updates news, all subscribers should be notified.

**Expected Output:**
```
Subscriber 1 received: Breaking News!
Subscriber 2 received: Breaking News!
```

---

### Question 29: Strategy Pattern with First-Class Functions
Create a `ShoppingCart` class that accepts a discount strategy (function) at checkout. Implement `no_discount`, `ten_percent_off`, and `bulk_discount` strategies.

**Expected Output:**
```
Total with no discount: 100.0
Total with 10% off: 90.0
Total with bulk discount: 80.0
```

---

### Question 30: Complete OOP Design Challenge
Design a `University` system with the following requirements:
- Abstract class `Person` with subclasses `Student` and `Professor`.
- `Student` can enroll in `Course` objects (composition).
- `Professor` can teach multiple `Course` objects.
- `Course` has a maximum capacity; enrollment should fail if full.
- Implement appropriate encapsulation, inheritance, and error handling.
- Add a method to display a student's transcript (list of courses and grades).

**Expected Output:**
```
Alice enrolled in Python 101
Python 101 is full! Bob cannot enroll.
Transcript for Alice:
  - Python 101: A
  - Data Structures: B+
```

---

## Answer Key (Brief Hints)

<details>
<summary>Click to expand hints</summary>

**Easy:**
1. Use `__init__` to initialize attributes.
2. Use default parameter in `__init__(self, name, grade="A")`.
3. Define `def area(self): return self.width * self.height`.
4. Override `def __str__(self): return f"Book: {self.title} by {self.author}"`.
5. Define `species` outside `__init__`.
6. Use `self.balance += amount` and `self.balance -= amount`.
7. Use `self.__age` and `def get_age(self): return self.__age`.
8. Use `class Cat(Animal):` and override `speak`.
9. In `Bike.__init__`, call `super().__init__(brand)`.
10. Use `Employee.count += 1` inside `__init__`.

**Medium:**
11. Use `@property def fahrenheit(self):` and `@fahrenheit.setter`.
12. Use `@classmethod` and `cls(day, month, year)`.
13. Use `@staticmethod` decorator.
14. Define `class Duck(Flyer, Swimmer):`.
15. Use `D.__mro__` or `D.mro()`.
16. Inherit from `ABC` and use `@abstractmethod`.
17. Use `@property def balance(self):` with validation in setter.
18. Define `def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)`.
19. Define `def __len__(self):` and `def __getitem__(self, index):`.
20. Initialize `self.engine = Engine(...)` in `Car.__init__`.

**Hard:**
21. Implement `__iter__` returning `self` and `__next__` decrementing until 0.
22. Define `__enter__` and `__exit__` methods.
23. Override `__call__` in metaclass to store instance in a dict.
24. Implement `__get__`, `__set__`, and `__delete__` in descriptor.
25. Create exception classes inheriting from `Exception`.
26. Mixin defines `to_json` using `self.__dict__` and `json.dumps`.
27. Use `__getattr__` to initialize wrapped object on first access.
28. Publisher maintains a list of observers; notifies them on update.
29. Pass strategy function to `checkout` method.
30. Use abstract base class, composition for courses, and custom exceptions for capacity.

</details>

---

*Happy Coding! Master these to solidify your Python OOP skills.*