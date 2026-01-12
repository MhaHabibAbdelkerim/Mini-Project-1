#import the random module to generate random numbers
import random

#start an infinite loop to allow multiple rolls
while True:
 #Get user input
 choice= input("Do you want to roll the dice? (yes/no): ").lower()
 
 #If choice is yes, roll the dice and display the result
 if choice == 'yes':
    dice_roll1= random.randint(1,6)
    dice_roll2= random.randint(1,6)
    print(f"You rolled a {dice_roll1} and a {dice_roll2}.")
 
 #if choice is no, exit the loop
 elif choice == 'no':
    print("Thank you for playing!")
    break
 #if input is invalid, ask the user for input again
 else:
    print("Invalid input. Please enter 'yes' or 'no'.")