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

#Write your code below this line 👇

prompt = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))

comp = random.randint(0, 2)

if prompt not in range(3):
    print("Invalid number!")
elif prompt == 0:
    if comp == 0:
        print(f" You chose: \n {rock} \n Computer chose: \n {rock} \n Its a Draw!")
    elif comp == 1:
        print(f" You chose: \n {rock} \n Computer chose: \n {paper} \n You Lose!")
    else:
        print(f" You chose: \n {rock} \n Computer chose: \n {scissors} \n You Win!")
elif prompt == 1:
    if comp == 0:
        print(f" You chose: \n {paper} \n Computer chose: \n {rock} \n You Win!!")
    elif comp == 1:
        print(f" You chose: \n {paper} \n Computer chose: \n {paper} \n Its a Draw!")
    else:
        print(f" You chose: \n {paper} \n Computer chose: \n {scissors} \n You Lose!")
else:
    if comp == 0:
        print(f" You chose: \n {scissors} \n Computer chose: \n {rock} \n You Lose!")
    elif comp == 1:
        print(f" You chose: \n {scissors} \n Computer chose: \n {paper} \n You Win!")
    else:
        print(f" You chose: \n {scissors} \n Computer chose: \n {scissors} \n Its a Draw!")

