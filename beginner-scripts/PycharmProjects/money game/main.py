print("you been walking and you see a homeless person and he asked for money")
print("will you give him money")
alg1 = ("")
money = input("yes or no:")
if money == ("yes"):
    print("you gave the homeless person money")
    alg1 = ("money")
elif money == "no":
    print("you told no")
    print("he started crying")
    print("you eventually died because of wealth issues ")
    print("you lose")
    exit()
else:
    print("you didnt tell anything")
    print("homeless man asked to tell something")
    print("you didnt tell anything")
    print("you died in car crash which came from front while you wear turning")
    print("you lose")
    exit()

bank = ("")
if alg1 == "money":
    print("he was mrbeast acting like a homeless man")
    print("he gave you a million dollars")
    bank = ("million")

job = ("")
if bank == "million":
    print("what would you do with the money")
    print("1 for starting buisness")
    print("2 for buying lottery tickets")
    job = input("")

if job == "1":
    print("your buisness failed")
    print("you are now homeless")
    print("you lose")
    exit()
elif job == "2":
    print("you spent all your money on lottery")
    print("you won 1 trilllion")
    print("you are now a trillionare")
    bank = ("thrillion")
else:
    print("you didnt spend your money and you live happily ever after")
    print("but you still lose cause you didnt win")
    print("you lose")
    exit()

giveaway = ("")
if bank == ("thrillion"):
    print("would you give 1 tenth of your money to the poor")
    print("yes or no")
    giveaway = input("")

if giveaway == "yes":
    print("you gave 1 tenth of your money to the poor")
    print("a lot of people including the poor like you")
    print("and they helped you reach become the most richest person")
    print("who ever leaved in the universe")
    print("you won the game,congratulation!")
else:
    print("nothing happened but you stil got nothing")
    print("so you lose")
    exit()