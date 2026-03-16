import random

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
plays = [rock, paper, scissors]

def play():
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if choice in [0, 1, 2]:
        print(plays[int(choice)])
        comp = random.randint(0,2)
        print("Computer chose:")
        print(plays[comp])
        if choice == comp:
            print("It's a draw!")
        elif choice == 0 and comp == 2:
            print("You win!")
        elif choice == 1 and comp == 0:
            print("You win!")
        elif choice == 2 and comp == 1:
            print("You win!")
        else:
            print("You loose!")
    else:
        print("You choose poorly!")