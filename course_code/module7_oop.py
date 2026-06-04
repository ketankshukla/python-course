class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f'{self.name} says woof!'


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"

    def __str__(self):
        return f'{self.title} by {self.author}'


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        return 'Driving'


class Car(Vehicle):
    def drive(self):
        return 'Driving a car'


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def summary(self):
        return f'{self.name} has grade {self.grade}'


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, I am {self.name}'


class Teacher(Person):
    def greet(self):
        return f'Hello, I am {self.name}, and I teach.'


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        return self.balance
