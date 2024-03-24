print("count to 10!")
for x in range(0, 11):
    print(x)
print("welcome to guess the number")
print("the rules are simple.i will think a number. you have to guess it")
import random
number = random.randint(1,10)
guessNumber = False
while guessNumber != True:
    guess = input("guess a number between 1 to 10: ")
    if int(guess) == number:
        print("you gueese {}. that's good! you won".format(guess))
        guessNumber = True
    else:
        print("you guesses {}. sorry, thats wrong".format(guess))
        
    
