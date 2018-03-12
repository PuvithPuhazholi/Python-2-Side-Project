import random
randomnumber=random.randint(0,10)
guess=input("GUESS A NUMBER BETWEEN 0 AND 10: ")
#restart=input("TYPE IN 'PLAY AGAIN' IF YOU WANT TO PLAY AGAIN!")
if int(guess)==randomnumber:
    print("YOUR GUESS WAS RIGHT")
else:
    print("YOUR GUESS WAS WRONG!")
    print("THE CORRECT NUMBER WAS: "+str(randomnumber))
    
