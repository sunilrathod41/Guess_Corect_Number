'''we are going to write a program that generate a random number and ask a user to guess it
if the players guess is higher number than actual number then the program displays " for Lower number "
similarly if the players guess too low then program will display " for  Higher number  "
then the users guess the correct number
the program will display the number of guesses the player used to arrive at the actual number User
 has only 3 chance to guess the correct number'''

import random
randNumber=random.randint(1,10)
#print(randNumber)
userguess=None
guess=0
guesses=3
while (True):
    print("\n")
    print("\n\t****    Guess Number in between 1 to 10    ****")
    print("\t********    Enter q for quit the game    ********")
    userguess=input("Guess Number---\t ")
    print("")
    if (userguess=='q'):
        print("You can try again")
        break
    try:
        userguess=int(userguess)
        guesses -=1
        guess+=1
        if guesses==0:
            print("\t\t Try again and get 3 chance more")

            break
        if (userguess==randNumber):
            print(f"\t\tcongratulations you guessed correct numer in {guess} attempt \n")
            break
        else:
             if (userguess>randNumber):
                 print("Your guessed it Wrong Number!! Guess Smaller Number\n")
             else:
                 print("You guessed it Wrong Number!! Guess Larger Number\n")
        print(f"\t\t\t You have only {guesses} chance for Guess \n")

    except Exception as e:
        print(e)
