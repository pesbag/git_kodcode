# 1
class Dog:
    def __init__(self,name):
        """Docstring"""
        self._name=name

    def bark(self):
        """Docstring"""
        return f'{self.name} says woof'
# 2
class Rectangle:
    def __init__(self,width,height):
        """Docstring"""
        self._width=width
        self._height=height
    def area(self):
        """Docstring"""
        return self._width*self._height

# 3
class Counter:
    def __init__(self):
        """Docstring"""
        self._counter=0
    def increment(self):
        """Docstring"""
        self._counter+=1
    def value(self):
        """Docstring"""
        return self._counter
# 4
class Point:
    def __init__(self,x,y):
        """Docstring"""
        self._x=x
        self._y=y
    def __str__(self):
        """Docstring"""
        return f"({self._x},{self._y})"
# print(Point(2,3))

# 5
class BankAccount:
    def __init__(self):
        self._balance=0
    def deposit(self,amount):
        """Docstring"""
        self._balance+=amount
    def withdraw(self,amount):
        """Docstring"""
        if self._balance>=amount:
            self._balance-=amount

class Temperature:
    def __init__(self,temp):
        """Docstring"""
        self._temp=temp
    def to_fahrenheit(self):
        """Docstring"""
        self._temp=(self._temp*1.8)+32
        print(self._temp)
# Temperature(100).to_fahrenheit()

#7
class Student:
    _school="Kodcode"
    def __init__(self,name):
        """Docstring"""
        self._name=name
    def __str__(self):
        """Docstring"""
        return self._name
# s1=Student("Pesach")
# s2=Student("Netanel")
# print(s1)
# print(s2)
# s1._name="shalom"
# print(s1)
# print(s2)

# 8
class Player:
    counter=0
    def __init__(self,name):
        """Docstring"""
        Player.counter+=1
        self._name=name

# p1=Player("shalom")
# p2=Player("pesach")
# print(p2.counter)

# 9
class Money:
    def __init__(self,amount):
        """Docstring"""
        self._amount=amount
    def get_amount(self):
        """Docstring"""
        return self._amount

    def is_more_than(self,other):
        """Docstring"""
        return self._amount>other.get_amount()
# 10
class PlayList:
    def __init__(self,song_lst):
        """Docstring"""
        self._song_lst=song_lst

    def add(self,title):
        """Docstring"""
        self._song_lst.append(title)

    def remove(self,title):
        """Docstring"""
        self._song_lst.remove(title)

    def count(self):
        """Docstring"""
        return len(self._song_lst)

    def __str__(self):
        """Docstring"""
        return str(self._song_lst)
# p1=PlayList(["a","b"])
# print(p1)
# p1.add("c")
# print(p1)