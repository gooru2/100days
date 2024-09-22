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

choices = [rock, paper, scissors]
player_choice = int(input("What do you chose. 0 is rock, 1 is paper, 3 is scissors\n"))
print(choices[player_choice])

print("computer choose: ")
computer_choice=random.randint(0,2)
print(choices[computer_choice])

if computer_choice == player_choice:
    print("it's draw")
elif computer_choice==0 and player_choice==1:
    print("player win")
elif computer_choice==0 and player_choice==2:
    print("comp win")
elif computer_choice==1 and player_choice==0:
    print("comp win")
elif computer_choice==1 and player_choice==2:
    print("player win")
elif computer_choice==2 and player_choice==0:
    print("player win")
else:
    print("comp win")