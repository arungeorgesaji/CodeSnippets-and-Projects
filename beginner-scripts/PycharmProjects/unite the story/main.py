# gives user options which doesnt really change anything but still making it fun
print(" how pokemon unite universe was made(text edition)")
print("hello welcome to the world of pokemon")
print("my name is proffesor oak")
print("and these are pokemon")
print("and now what was your gender")
print("boy or girl")
gender = input(" ")
if gender == "boy":
    print("oh you are a boy")
elif gender == "girl":
    print("oh so your a girl")
elif gender == "boy" or "girl":
    print("sorry i was not listening")
    print("please tell it again")
    gender = input("")
if gender == "boy" or "girl":
    print("hmm not clear but i heard boy")
    print("boy it is")
    gender = ("boy")

print("what was your name")
name = input(" ")
if gender == "boy":
    print("anyway i will call you james")
    name = ("james")
elif gender == "girl":
    print("anyway i will call you sara")
    name = ("sara")

print("this is my son,you were rivals since you were kids")
print("uhh what was his name again")
print("sorry for asking i remember his name already")
print("his name was red")
rival = ("red")

print("red-seems like you woke up early")
print("oak-pick whiever pokemon you like")
print("oak-the first is the first starter charmander")
print("strong and fast evolving it is an overconfident pokemon")
print("oak-the second one is the water starter squirtle")
print("neutral prefers defense over attack while keeping attack high ")
print("oak-the third one is the grass starter bulbasaur")
print("if raised well it is strong you can raise it as you like it to be,itmay be hard to raise")
print("choose 1 for charmander 2 squirtle and 3 for bulbasaur")
starter = input(" ")
if starter == "1":
    print("oak-so you chose the fire starter charmander,take good care of it")
    print("james got charmander from proffesor oak")
elif starter == "2":
    print("oak-so you chose the water starter squirtle,take good care of it ")
    print("james got squirtle from professor oak")
elif starter == "3":
    print("oak-so you chose the grass starter bulbasaur,take good care of it")
    print("james got bulbasaur from professor oak")
else:
    print("oak-hmm you dont seem to be intrested in these pokemon maybe you would like my eevee")
    print("james got eevee from proffesor oak")

james_starter = ("")
red_starter = ("")

if starter == "1":
    james_starter = ("charmander")
elif starter == "2":
    james_starter = ("bulbasaur")
elif starter == "3":
    james_starter = ("squirtle")
else:
    james_starter = ("eevee")

if james_starter == ("charmander"):
    print("red-then i will choose squirtle")
    red_starter = ("squirtle")
    print("red got squirtle from proffesor oak")
if james_starter == ("squirtle"):
    print("red-then i will choose bulbasaur")
    red_starter = ("bulbasaur")
    print("red got bulbasaur from proffesor oak")
if james_starter == ("bulbasaur"):
    print("red-then i will choose charmander")
    print("red got charmander from proffesor oak")
    red_starter = ("charmander")
if james_starter == ("eevee"):
    print("red-father you gave red you eevee")
    print("i also want a special pokemon")
    print("oak-ok son take my pickachu")
    red_starter = ("eevee")
    print("red got eevee from proffesor oak")

print("james let do a quick battle")
print("do you want to do a battle yes or no")
battle_rival = input("")

if battle_rival == "yes":
    print("red-ok lets begin")
    print("red sent out his " + red_starter)
    print("you sent out your " + james_starter)
    print("you-what a level 100 i taught starters were level 5")
    print("oak-red,did you feed ultra rare candy  to level 100 your" + red_starter)
    print("oak-here take these it will make your pokemon level up")
    print("you used candys to make you starter to level 100")
    print("oak-these are ultra rare candys")
    print("these will make your pokemon level 100")
    print("your " + james_starter + "is now level 100")
    print("james-what a wormhole")
else:
    print("red-seems like youre scared")
    print("you-no i am not")
    print("red-then lets start")
    print("red sent out his " + red_starter)
    print("you sent out " + james_starter)
    print("you-what a level 100 i taught starters were level 5")
    print("oak-red,did you feed ultra rare candy  to level 100 your" + red_starter)
    print("oak-here take these it will make your pokemon level up")
    print("you used candys to make you starter to level 100")
    print("oak-these are ultra rare candys")
    print("these will make your pokemon level 100")
    print("your " + james_starter + " is now level 100")
    print("james-a wormhole")
    print("james-arceus!!")
    print("hello child,this universe will soon be called pokemon unite and you will be making it ")
    print("james-umm,how")
    print("arceus-i will show you he rules and everything,people from your universe can test it for now ")
    print("james-wow")
    print("proffesor phorus-and thats how pokemon unite was made")
    print("do you think its a myth or is it real")
m_r = input("")
if m_r == "myth":
    print("phorus-its actually real")
elif m_r == "real":
    print("phorus-yes your right its real")
else:
    print("phorus-i dont really understand you but its real")

print("trainer-that was intresting now let me get back to practising")
print("phorus-ok")