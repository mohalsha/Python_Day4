#Excercise 1

class Car():
    car_count = 0

    def __init__(self, color, brand, year, price):
        self.color = color
        self.brand = brand
        self.year = year
        self.price = price
        Car.car_count += 1 
    
    def get_car_count(self):
        return Car.car_count
    
    @staticmethod
    def car_info():
        print(f"The car is a {Car.self.color} {Car.self.brand} of model {Car.self.year}, asking price is {Car.self.price} ")

car1 = Car("red", "Mitsubishi", 1997, 2800)
print(Car.car_count)
print(car1)

print(car1.car_info)

#Excercise 2

class BankAccount():
    interest_rate = 0.05

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def set_interest_rate(self, x):
        BankAccount.interest_rate = x
    
    def get_interest_rate(self):
        print(BankAccount.interest_rate)
    
    def add_money(self,ammount):
        self.ammount = ammount
        self.balance = self.balance + ammount

    def withdraw_money(self,ammount):
        self.ammount = ammount
        self.balance = self.balance - ammount
    
    def get_account_balance(self):
        print(self.balance)
    
    def calculate_annual_interest(self):
        return self.balance * self.interest_rate

#Excercise 3

class Person():
    def __init__(self, name, last_name, age):
        self.__name = name
        self.__last_name = last_name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self, name):
        self.__name = name

    @last_name.setter
    def name(self, last_name):
        self.__last_name = last_name

    @age.setter
    def name(self, age):
        self.__age = age

#Excercise 4

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager():
    def __init__(self, department):
        self.department = department

class Executive(Employee,Manager):
    def __init__(self, company_car, bonus):
        self.company_car = company_car
        self.bonus = bonus
    
    def __str__(self):
        print("The Executive name is {self.name} and their salary is {self.salary} USD, they work in the {self.department} department, and they are using company car {self.company_car}. they are entitled to a bonus of {self.bonus} ")

#Excercise 5
#I created the class with a lower case "p" at the start becuase we already have a class called "Person"

class person():
    def _init__(self, name, age):
        self.name = name
        self.age = age
    
    def set_name(self, name):
        self.name = name
        return self.name
    
    def set_age(self, age):
        self.age = age
        return age
    
    def get_person_info(self):
        print("This is {self.name}, and they are {self.age} years old")
    



        
