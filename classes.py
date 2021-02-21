# Dog Class
class Dog:
    # method of the dogs
    def bark(self):
        print("bark!!")
    
    def play(self):
        print("I am happy play with me")


scooby = Dog()
scooby.bark()

# class Inheritance
class Employee:
    def __init__(self, name, last_name, job):
        self.name = name
        self.last_name = last_name
        self.job = job

class Company(Employee):
    def greetings(self):
        print("welcome",self.name)


tero = Company("Tero"," Baroos" ," Python")
tero.greetings()