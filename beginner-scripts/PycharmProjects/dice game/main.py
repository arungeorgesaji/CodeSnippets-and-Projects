import random

player1 = input("type first players name:")
while player1 == (""):
    print("this field is mandatory")
    player1 = input("type first players name:")

player2 = input("type second players name:")
while player2 == (""):
    print("this field is mandatory")
    player1 = input("type seconds players name:")

while player1 == player2:
    print("hmm the names should be different from each other")
    player2 = input("type another name for second player:")
rolldice = ['1', '2', '3', '4', '5', '6']
dice1 = random.choice(rolldice)
dice2 = random.choice(rolldice)
print(player1 + " got " + dice1)
print(player2 + " got " + dice2)
if dice1 < dice2:
    print(player2 + " won")
if dice1 > dice2:
    print(player1 + " won")
if dice1 == dice2:
    print("its a tie")