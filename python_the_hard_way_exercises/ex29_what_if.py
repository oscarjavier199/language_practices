#program to practice boolean operators with simple if statements

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
if people > cats:
    print("Not many cats! the world is sad :(")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry")
    
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("people are dogs")    
    
if True and True  == True:
    print("true")
