print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Lets's Play :) ")
score = 0

answer = input("What does CPU stand for? ")  # .lower() can be added at the end of the answer 
if answer.lower() =="central processing unit":
    print('Correct!')
    score += 1  # This can also be written as score = score + 1 which ever suits better.
else:
    print("Incorect!")
    
answer = input("What does GPU stand for? ")
if answer.lower() =="graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorect!")

answer = input("What does RAM stand for? ")
if answer.lower() =="random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorect!")

answer = input("What does ROM stand for? ")
if answer.lower() =="read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorect!")           

answer = input("What does LAN stand for? ")
if answer.lower() =="local area network":
    print('Correct!')
    score += 1
else:
    print("Incorect!")

answer = input("Which python module generates random floating numbers in the range[0.1, 1.0)? ")
if answer.lower() =="random":
    print('Correct!')
    score += 1
else:
    print("Incorect!")

answer = input("What does EDI stand for? ")
if answer.lower() =="electronic data interchange":
    print('Correct!')
    score += 1
else:
    print("Incorect!")

answer = input("Which is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive? ")
if answer.lower() =="pandas":
    print('Correct!')
    score += 1
else:
    print("Incorect!")

answer = input("Which keyword is used in python to support a funtion ? ")
if answer.lower() =="import":
    print('Correct!')
    score += 1
else:
    print("Incorect!") 

answer = input(" What does MAN stands for? ")
if answer.lower() =="metropolitian area network":
    print('Correct!')
    score += 1
else:
    print("Incorect!")          

print("You got " + str(score) + " questions correct!") # The score will be counted here

print("You got " +str((score / 10) * 100) + "%") # the percentage of the score displayed here

    