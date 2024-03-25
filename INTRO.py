# python comments-this is a single line comment
"""
this is a sample more than one line comments



student_name = "ian"
student_age = "30"
is_male = True
print(student_name)
print(student_age)
print(is_male)

# outputting the values in the variables
student_name = "ryan"
student_name = "ian"
print(student_name)

STUDENT_NAME = "ryan"
student_name = "ian"
print(STUDENT_NAME)
X = Y = Z = 10.0
X, Y, Z = 10, 11, 12
x = int(1)
y = int(2.8)

price = 10
qty = 7
total = price * qty
answer = " Total :" + str(total) + "kenyan shillings"
answer1 = "the total is:", total, "kenyan shillings"
print(answer)

a = 1
b = "2"
c = a + int(b)
print(c)

pens = 60.0
books = "50"
total = pens + float(books)
result = "My Total is   :$" + str(total) + "kenyan shillings"
print(result)

age = 29
residence = "nairobi"

if residence == "nairobi" or residence == "Kasarani":
    print("can vie for Governor of Nairobi")
else:
    print("Do not meet requirements to become Governor of Nairobi")

# x=int(input("enter number to be checked:"))


#loops
#the while loop
x=1
while x<=5:
    if x==3:
        break
    print(x)
    x+=1

# the continue statement
i = 0
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

country=input("enter country:")
if country == "Rwanda":
    print("East Africa")
elif country=="Kenya":
    print("East Africa")
elif country == "Tanzania":
    print("East Africa")
elif country == "Rwanda":
    print("East Africa")
else:
    print("unknown country")
    
x=1
while x<=5:
    print("the number is:",x)
    x+=1
else:
    print("loop ended")
i=1
while i < 10:
        if i == 3:
            i += 1
            continue
        print(i)
        i += 1
        if i == 5:
            i += 1
            continue

x=1
while x<=100:
    print("the number is:",x)
    x+=2
total=("x+=x")
print("total")

def sum_of_odd_numbers(n):
    total = 0
    for i in range(1, n+1, 2):  # Start from 1 and step by 2 to cover only odd numbers
        total += I
    return total

# Example usage:
n = 100  # Sum odd numbers up to 10
result = sum_of_odd_numbers(n)
print("Sum of odd numbers up to", n, "is:", result)




def main():
    countries = []
    while len(countries) < 2:
        user_input = input("Enter a country: ")
        countries.append(user_input)

    country_counts = {countries[0]: 0, countries[1]: 0}

    while True:
        user_country = input("Enter your country: ")
        if user_country in countries:
            country_counts[user_country] += 1
        else:
            print("Invalid country entered. Please enter one of the two countries.")
            continue

        choice = input("Do you want to allow another person to input their country? (yes/no): ")
        if choice.lower() != 'yes':
            break

    print("Country Counts:")
    for country, count in country_counts.items():
        print(f"{country}: {count} people")


if __name__ == "__main__":
    main()


#using for to add odd numbers

total = 0
n = 50
for i in range(1, n + 1, 2):
 total += I
print("The sum of odd numbers up to", n, "is:", total)


#end



names = [input("Enter a name: ") for _ in range(3)]
name_counts = {name: 0 for name in names}
print(names)


print("         dictionaries            ")
this dict = {"Brand": "porshe",
            "Model": "911",
            "Type": "GT3 RS",
            "Year": "2023",
            "Colour": "red",
            "1": "one"
            }
this dict.get("Model")

print(this dict)

this dict.pop(input("what do you want to remove:") and input("what do you want to remove:"))

for x in this dict:
    print(this dict[x])
if "one" in this dict.values():
    print("yes, 'model' exits in this dictionary")
else:
    print("no, 'model does not exist in this dictionary")

names = ["Rash", "Kil", "Harsh"]
numbers = [1, 4, 5]

print(" names : " + str(names))
print(" numbers : " + str(numbers))

res = dict(zip(names, numbers))

print("dictionary is : " + str(res))

print("            tuples          ")
thistle = ("apple", "banana", "orange", "Mango")
print(thistle)
y = list(thistle)
y[1] = input("new item: ")
x = tuple(y)

print(x)

print("        set               ")
set = {"apple", "banana", "cherry"}
print(set)
set.add(input("new item:"))
print(set)
set.remove(input("what do you want to remove:"))
print(set)

list = [1,2,3,4,5,6,7,8,9,10,10]
repeated number=[]
for item in list:
    if list.count(item)>1:
        repeated number.append(item)
        print(repeated number)
print(max(list))


try:
    number1 =10
    number2 =20

    x=number2/number1


except Exception as e:
    print("error occurred ",e)
else:
    print(x)
    print("program ended")
print("retrying ")



# object-oriented programing
class student:
    # properties
    student_name = ""
    student_age = ""
    student_marks = ""

    def __init__(self, name, age):
        self.student_name = name
        self.student_age = age

        print("constructor called")  # first function in this case is constructor it is the first function to be called

    def display_student_details(self):  # third function displays the student name

        print("student:", self.student_name, "age:", self.student_age)


student1 = student(input("Enter your name:"), input("Enter your age:")) #
student1.display_student_details()




#  start of inheritance
class person:
    name= ""
    age= ""

    def __init__(self, name, age):
        self.name = name
        self. Age = age

    def print person(self):
        print("person details:", self.name, self. Age)


class student(person):  # child from parent class
    uniform=""
    def __init__(self, name, age, uniform):
        super().__init__(name, age)
        self. Uniform = uniform

    def print person(self):
        print(self.name, self. Age, self. Uniform)

student1= student("kelvin",40,"khaki")
student1.print person()



# start of poly
class animal:
    def __init__(self):
        pass

    def speak(self):
        print("I am an animal")


class dog(animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("I am a dog")


class cat(animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("I am a cat")


dog1 = dog()
dog1.speak()

cat1 = cat()
cat1.speak()

"""


# encapsulation
class bank_account:
    account_Name = ""
    Balance = 3000

    def __init__(self):
        pass

    def withdraw(self, amount):
        self.Balance = self.Balance - amount
        return self.Balance

    def transfer(self, amount):
        self.Balance = self.Balance - amount
        return self.Balance

    def deposit(self, amount, account_name):
        self.Balance += amount
        self.account_Name = account_name
        return self.Balance

    def show_balance(self):
        print("Account Name", self.account_Name, "Account Balance", self.Balance)


account1 = bank_account()
account1.account_Name = input("enter account name:")
choice = input("Do you want to withdraw? (yes/no): ")
account1.withdraw(int(input("enter amount you want to withdraw:")))

account1.show_balance()
if choice.lower() != 'yes':

    choice = input("Do you want transfer? (yes/no): ")
    account1.transfer(int(input("enter amount transfer")))
    account1.show_balance()
if choice.lower() != 'yes':

    choice = input("Do you want to see your balance? (yes/no): ")
    account1.show_balance()
    if choice.lower() != 'yes':
        print("thank you for using our services welcome again")

print("thank you for using our services welcome again")


