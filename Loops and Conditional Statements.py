#Conditional Statements
x = 5
if x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
else:
    print("Moree")

#---------------------------------------------------------#

#For Loop Statements
users = {'a': 'active', 'b': 'inactive', 'c': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

#---------------------------------------------------------#

#range() function
for i in range(5):
    print(i)

#---------------------------------------------------------#

#range function with start, end and step values
print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -40, -70)))

#---------------------------------------------------------#

#to iterate over indicies of sequence we can go for range + len functions
a = ['hari', 'keerthi', 'jothi']
for i in range(len(a)):
    print(i)

#---------------------------------------------------------#

#range and sum of range values
print(range(10))
print(sum(range(10)))

#---------------------------------------------------------#

# #break statement
for n in range(2, 10):
    for x in range(2, n):
        if n%x == 0:
            print(f"{n} is equals {x}*{n//x}")
            break

#---------------------------------------------------------#

# #continue statement
for n in range(2, 10):
    if n%2 == 0:
        print(f"It prints the even number {n}")
        continue
    print(f"It prints the odd number {n}")

#---------------------------------------------------------#

#else statement
for n in range(2, 10):
    for x in range(2, n):
        if n%x == 0:
            print(f"{n} is equals {x}*{n//x}")
            break
    else:
        print(n, "is a prime number")

#---------------------------------------------------------#

#match statement
def match_method(status):
    match status:
        case "400":
            return "400 error"
        case "500":
            return "Internal Server Error"
        case _:
            return "There is something error"

print(match_method("_"))

#---------------------------------------------------------#

#while loop
count = 0
while count <= 3:
    print("Print the values of count", {count})
    count += 1

#---------------------------------------------------------#

#while loop with break statement
count = 0
while count <= 3:
    count += 1
    if (count % 2) == 0:
        print("It is even number")
        break
    print("It is odd number")

#---------------------------------------------------------#

#while loop with continue statement
count = 0
while count <= 3:
    count += 1
    if (count % 2) == 0:
        print("It is even number")
        continue
    print("It is odd number")

#---------------------------------------------------------#

#while loop with else statement
count = 0
while count <= 3:
    count += 1
    if (count % 2) == 0:
        print(count, "count")
        print("It is even number")
else:
    print("Else statement executed")

#---------------------------------------------------------#

#no do-while but achieve with while true with break statement
while True:
    user_input = input("Type exit to stop")
    if user_input == 'exit':
        break