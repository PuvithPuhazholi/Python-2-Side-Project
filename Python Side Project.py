import random
randomnumber=random.randint(0,10)
guess=input("GUESS A NUMBER BETWEEN 0 AND 10: ")
if int(guess)==randomnumber:
    print("YOUR GUESS WAS RIGHT")
else:
    print("THE CORRECT NUMBER WAS: "+str(randomnumber))
