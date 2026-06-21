#string
name = "Sejfullah"
email = "Sejfullah0@gmail.com"
adress = "karmgatan 39"

#integer
age = -1
height = 180

#float 
weight = 66.5

#boolean
is_student = True
is_employed = False

#list
hobbies = ["programming", "gaming", "traveling"]

print("Name:", name)
print("Email:", email)
print("Address:", adress)
print("Age:", age)
print("Height:", height)
print("Weight:", weight)
print("Is Student:", is_student)
print("Is Employed:", is_employed)
print("favorite hobbie is:", hobbies[0])

#if statement
if age > 18: 
    print(f"{name} is an adult and that is {is_student}")
elif age <= 18 and age > 0:
    print(f"{name} is not an adult and that is {is_employed}")
else :   print("Invalid age")

#type casting

weight = int(weight)
age = str(age)
print("Weight as integer:", weight)
print("Age as string:", age)
print(type(age))
age += "1"
print("Age after concatenation:", age)
#user input

name= input("vad heter du? ")
if bool(name) == True:
    print(f"Hej {name}!")
else :   print("Du måste ange ett namn!")

# första uppgiften
name = input("vad heter du? ")
age = input("Hur gammal är du? ")
age = int(age)
age += 1
print(f"Hej {name}, nästa år fyller du {age} år !")

# andra uppgiften
number = input("Skriv in ett nummer: ")
number = int(number)
if number > 0 :
    print("Siffran är possitiv")
elif number < 0 :
    print("Siffran är negativ")
else :
    print("Siffran är noll")

if number % 2 == 0 :
    print("Siffran är jämn")
else :
    print("Siffran är udda")