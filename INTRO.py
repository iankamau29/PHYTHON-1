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
myanswer = " Total :" + str(total) + "kenyan shillings"
myanswer1 = "the total is:", total, "kenyan shillings"
print(myanswer)

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

if residence == "nairobi" or residence == "kasarani":
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

countyr=input("enter country:")
if countyr == "Rwanda":
    print("East Africa")
elif countyr=="Kenya":
    print("East Africa")
elif countyr == "Tanzania":
    print("East Africa")
elif countyr == "Rwanda":
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
        total += i
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
 total += i
print("The sum of odd numbers up to", n, "is:", total)


#end



names = [input("Enter a name: ") for _ in range(3)]
name_counts = {name: 0 for name in names}
print(names)

"""

thisdict={
    "brand": "porshe",
    "model": "911",
    "type":"GT3 RS",
    "year": "2023"
}
print(thisdict["model"])

