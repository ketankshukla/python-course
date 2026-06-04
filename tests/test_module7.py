import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from course_code import module7_oop as m


def test_dog_and_book():
    dog = m.Dog('Rex', 4)
    assert dog.speak() == 'Rex says woof!'
    book = m.Book('1984', 'Orwell')
    assert '1984' in str(book)


def test_vehicle_and_car():
    car = m.Car('Toyota', 'Corolla')
    assert car.drive() == 'Driving a car'


def test_rectangle_and_school():
    rect = m.Rectangle(3, 5)
    assert rect.area == 15
    student = m.Student('Nina', 'A')
    assert 'Nina has grade A' in student.summary()
    teacher = m.Teacher('Lena')
    assert 'I teach' in teacher.greet()


def test_bank_account():
    account = m.BankAccount('Dana', 100)
    assert account.deposit(50) == 150
    assert account.withdraw(30) == 120
