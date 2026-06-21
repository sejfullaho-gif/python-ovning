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
    print("Siffran är positiv")
elif number < 0 :
    print("Siffran är negativ")
else :
    print("Siffran är noll")

if number % 2 == 0 :
    print("Siffran är jämn")
else :
    print("Siffran är udda")
# listor in ptyhon
leksaker = ["bil", "figur", "spade"]
print(leksaker)
print(leksaker[2])
print(len(leksaker))
leksaker.append("hej")
print(leksaker)
ålder = [1, 2 ,3, 4]
leksaker.append(ålder)
print(leksaker)
leksaker.remove("bil")
print(leksaker)

#uppgift 3

favoritsaker = ['godis', 'leksaker', 'bilar', 'basket', 'gaming']
print(f"Det finns totalt {len(favoritsaker)} element i listan")
print(favoritsaker[0])
print(favoritsaker[4])
favoritsaker.append("popcorn")
print(favoritsaker)

#loops
#1 for loops
#printa allt
frukter = ['äpple', 'päron', 'banan']
for x in frukter:
    print(x)
#alla bokstäver i banana
for x in "banana":
    print(x) 
#sluta på ett visst element
for x in frukter:
    if x == "banan":
        break #continue omm du vill att den hoppar över.
    print(x)
# hur mycket en loop ska fortsätta
for x in range(6):
    print(x)
#mellan olika siffror
for x in range(2, 5):
    print(x)
# tredje parametern säger hur mycket den ska hoppa mellan varje
for x in range(2, 10, 2):
    print(x)
# while loop
i = 0
while i<2:
    print(i)
    i+=1


#uppgift 4

for count, x in enumerate(favoritsaker, start=1):
    print(f'{count}.{x}')
