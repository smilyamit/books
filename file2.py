'''
#Notes on dataclasses
In Python, the dataclass decorator is used to automatically generate special methods,
such as __init__, __repr__, and __eq__, for a class based on its annotated fields.
It reduces the boilerplate code needed to define a class and provides a concise way to create
data-oriented classes.
'''
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    profession: str

# Create an instance of the Person class
person = Person("John Doe", 30, "Software Engineer")

# Accessing the fields of the person object
print(f"The person name is {person.name}. who is {person.age} yearls old.\n He works as a {person.profession}")         # Output: John Doe

