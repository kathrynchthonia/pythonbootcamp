import random

print('Rock...')
print('Paper...')
print('Scissors...')

rand_num = random.randint(1, 3)
if rand_num == 3:
    computer = "rock"
if rand_num == 1:
    computer = "paper"
if rand_num == 2:
    computer = "scissors"


player = input("Player, make your move: ")


if player == "rock":
    if computer == "scissors":
        print("player wins!")
    elif computer == "paper":
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    elif computer == "scissors":
        print("computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("computer wins!")
    elif computer == "paper":
        print("player wins!")
elif player == computer:
    print("It's a tie!")
else:
    print("something went wrong...")
