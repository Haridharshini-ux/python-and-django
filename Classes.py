#class definiton, constructor and properties
class Details:
    team = "Developing"
    def __init__(self, name):
        self.name = name
    def getName(self, name):
        return f"The name of employee is {name}"
obj = Details("Hari")
print(obj.team)
print(obj.name)
print(obj.getName("Hari"))

#---------------------------------------------------------#

#class with properties updation
class Trucks:
    def __init__(self, name):
        self.name = name
        self.trucks = []
    def addTrucks(self, trucks):
        self.trucks.append(trucks)
obj = Trucks("car")
obj1 = Trucks("jeep")
obj.addTrucks("add car")
obj.addTrucks("add jeep")
print(obj.trucks)
print(obj.name)

#---------------------------------------------------------#

#if same attribute occurs in both class and instance it takes the instance value
class Data:
    location = "Coimbatore"
    direction = "North"

person1 = Data()
print(person1.direction)
person1.direction = "South"
print(person1.direction)

#---------------------------------------------------------#

#inheritance - overriding
class greetings:
    def getName(self):
        self.name = "My first kept name is Haridharshini"
        return self.name

class later(greetings):
    def getName(self):
        self.name = "My office kept name is Haridha"
        return self.name

obj = later()
print(obj.getName())

#---------------------------------------------------------#

#inheritance with another lookup chain
class life:
    def worries(self):
        return "worries will fade away"
    def life(self):
        return f"Life taught us to think {self.worries()} but it is not"
    
class old(life):
    def worries(self):
        return "worries will fade away while old"

obj = old()
print(obj.life())

#---------------------------------------------------------#

#inheritance with parent class required place
class life:
    def worries(self):
        return "worries will fade away"

class old(life):
    def worries(self):
        qoutes = life().worries()
        return f"Yes the qoute {qoutes} is true"

print(old().worries())

#---------------------------------------------------------#

#multiple inheritance
class Class1:
    def greet(self):
        return "Hi!, Good Morning"
class Class2:
    def greet(self):
        return "Hi!, Good Afternoon"
    def additional(self):
        return "It is additional method yahhh"
class Class3(Class1, Class2):
    pass

print(Class3().greet()) #it will print only the first base class value
print(Class3().additional())

#---------------------------------------------------------#

#inheritance super keyword
class Class1:
    def greet(self):
        return "Hello"
class Class2(Class1):
    def greet(self):
        greetings = super().greet()
        return f"{greetings}, Hari"

obj = Class2().greet()
print(obj)

#---------------------------------------------------------#

#iterators
class iterator:
    def __init__(self):
        self.number = 1
    def __iter__(self): #it is method for
        return self
    def __next__(self):
        if self.number > 3:
            raise StopIteration
        value = self.number
        self.number += 1
        return value
obj1 = iterator()
for num in obj1:
    print(num)

#---------------------------------------------------------#

#generators
class generators:
    def __iter__(self):
        yield 1
        yield 2
        yield 3
obj1 = generators()
for number in obj1:
    print(number)

