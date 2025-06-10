import random

print("Hi! Weelcome to the Number Guessing Game.\nYou have only 7 chances to guess the number.Lets start!")

low=int(input("Enter the Lower Bound:"))
high=int(input("Enter the Upper Bound:"))

print("You have 7 chances to guess the number between",low,"and",high,".","Lets start!")

number=random.randint(low,high)
ch=7      #chances
gc=0      #guess counter

while gc < ch:
    gc+=1
    guess=int(input("Guess a number: "))


    if guess == number:
        print("Congratulation! you did it in",gc,"try.")
        break

    elif gc >= ch :
        print("Sorry The number was",number,"Better luck next time!") 

    elif guess > number:
        print("Try Again! You guessed too high.")

    elif guess < number:
        print("Try Again! You guessed too low.")
    
    
  