rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)


list_of_choices = [rock, paper, scissors]
print(list_of_choices[user_choice])
print(list_of_choices[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice > computer_choice :
    print("You win!")
elif user_choice != 0 and user_choice != 1 and user_choice != 2:
    print("You typed an invalid number, you lose!")
else:
    print("You lose!")