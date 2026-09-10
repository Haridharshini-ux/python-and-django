#function definition
def greet(name):
    print("Hi", name)
greet("hari")

#---------------------------------------------------------#

#function with no return value
def greet(name):
    print("Hi", name)
result = greet("hari")
print(result)

#---------------------------------------------------------#

#with return value
def add(a, b):
    return a+b
result = add(2, 3)
print(result)

#---------------------------------------------------------#

#local variable
city = "coimbatore"
def declareCity():
    city = "pollachi"
    print(city)
declareCity()
print(city)

#---------------------------------------------------------#

#default argument value
def greetings(name, message = "Hello"):
    return f"{message} {name}"
print(greetings("Hari"))

#override the default argument value
def greetings(name, message = "Hello"):
    return f"{message} {name}"
print(greetings("Hari", "Welcome Back"))

#---------------------------------------------------------#

#mistake of empty default value
def addToCart(name, cart=[]):
    cart.append(name)
    return cart
print(addToCart("apple"))
print(addToCart("orange")) #output: ["apple", "orange"] #it wont forgot previous values

#---------------------------------------------------------#

#to overcome above this, we have to pass None instead of []
def addToCart(name, cart=None):
    if cart is None:
        cart = []
    cart.append(name)
    return cart
print(addToCart("apple"))
print(addToCart("orange")) #output: ["orange"] #now previous value will disappear

#---------------------------------------------------------#

#keyword arguments
def pet(animal: str, name: str):
    print(f"The {animal} kept it name as {name}")
pet('lion', 'king')
pet(animal = "dog", name = "shadow")
pet(name = "meenu", animal = "fish")
pet('king', 'lion')

#---------------------------------------------------------#

#*args and **kwargs 
def addition(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(addition(1, 2, 3))

#---------------------------------------------------------#

#**kwargs, it have details and unpacking it
def describe(**details):
    for key, value in details.items():
        return f"{key} : {value}"
print(describe(name="hari", role="developer"))