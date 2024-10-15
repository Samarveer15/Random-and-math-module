import random

playing= True
Number= str(random.randint(10,20))


print("I will generate a number fron 10 to 20 , and you have to guess the number one digit at a time")
print("The game ends when you get 1 hero!")

while playing:
    guess = input("Give me your best guess! \n")
    if Number == guess:
        print ("Ypu have won the game")
        print ("The number was",Number)
        break

    else:
        print("Your guess isn't quit right, try agian. |n")