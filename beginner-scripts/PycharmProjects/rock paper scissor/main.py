import random
value=input("rock,paper,scissors:")

choice = ['rock', 'paper', 'scissors']

result = random.choice(choice)
print(result)

print("arun chose " + result)

if value == ("rock"):

 if result==('rock'):
    print("its a tie")

 elif result==('paper'):
    print("you lose")

 elif result==('scissors'):
    print("you win")

if value == ("paper"):

 if result==('rock'):
    print("you win")

 elif result==('paper'):
    print("its a tie")

 elif result==('scissors'):
    print('you lose')

if value == ("scissors"):

  if result == ('rock'):
      print("you lose")

  elif result == ('paper'):
      print("you win")

  elif result==('scissors'):
      print("its a tie")
else:
    print("thats not rock paper or scissors")







