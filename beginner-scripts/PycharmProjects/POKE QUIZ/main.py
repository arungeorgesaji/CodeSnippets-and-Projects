print("POKE QUIZ")
print("which difficulty would you like")
print("1 for easy")
print("2 for medium")
print("3 for hard")
print("4 for insane")

i = 0

e1 = ("")
e2 = ("")
e3 = ("")
e4 = ("")
e5 = ("")

m1 = ("")
m2 = ("")
m3 = ("")
m4 = ("")
m5 = ("")

h1 = ("")
h2 = ("")
h3 = ("")
h4 = ("")
h5 = ("")

s1 = ("")
s2 = ("")
s3 = ("")
s4 = ("")
s5 = ("")
s6 = ("")

difficulty = ("")

print("choose a difficulty by using the number corresponding to the difficulty you want")

try:
    difficulty = input("")
except:
    pass

while difficulty == "":
    print("you have to choose a difficulty")
    try:
        difficulty = input("")
    except:
        pass

if difficulty == "1":
    print("you chose  easy difficulty")
    difficulty = ("easy")
    print("Q.1-which pokemon is considered god of pokemon")
    print("please type on full lowercase")
    e1 = input("")
    if e1 == "arceus":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the corrrect answer is arceus")

    print("Q.2-what is the full form of pokemon")
    print("please type in full lowercase and there should be s at the end")
    e2 = input("")
    if e2 == "pocket monsters":
        print("your answer is corrrect")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is pocket monsters")
    print("Q.3-what colour is charizard shiny sprite")
    print("type in full lowercase")
    e3 = input("")
    if e3 == "black":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is black")
        print("Q.4-ability which triggers ash greninja")
        print("type in full lowercase")
        e4 = input("")
        if e4 == "battle bond":
            print("you answer is correct")
            i += 1
        else:
            print("your answer is wrong")
            print("the correct answer is battle bond")
    print("Q.5-is there a beta version of gible")
    print("yes or no")
    print("type in full lowercase")
    e5 = input("")
    if e5 == "yes":
        print("you are correct")
        print("your points")
        i += 1
        print(i)
        exit()
    else:
        print("you are wrong")
        print("the correct answer is yes")
        print("your points")
        print(i)
        exit()

if difficulty == "2":
    print("you chose medium difficulty")
    difficulty = ("medium")
    print("Q.1-what is dark type called in japansese")
    print("type in full lowercase")
    print("only write the name like dark")
    m1 = input("")
    if m1 == "evil":
        print("your answer is correct")
        i += 1
    else:
        print("you are wrong")
        print("the correct answer is evil")
    print("Q.2-what is ash called in japanese")
    print("type in full lowercase")
    m2 = input("")
    if m2 == "satoshi":
        print("you are correct")
        i += 1
    else:
        print("you are wrong")
        print("the correct answer is sathoshi")
    print("Q.3-what is greninja called japanese ")
    print("type in full lowercase")
    m3 = input("")
    if m3 == "gekkouga":
        print("you answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the corrrect answer is gekkouga")
    print("Q.4-what is the signsture move dark mane necrozoma and solgaleo")
    print("type in full lowercase with no spaces")
    m4 = input("")
    if m4 == "sunsteelstrike":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is sunsteelstrike")
    print("Q.5-what is the signature move of zamazenta")
    print("type in full lowercase and one space(you know where)")
    m5 = input("")
    if m5 == "behemoth bash":
        print("your answer is correct")
        i += 1
        print("your points")
        print(i)
        exit()
    else:
        print("your answer is wrong")
        print("the correct answer is behemoth bash")
        print(i)
        exit()

if difficulty == "3":
    print("you chose hard difficulty")
    difficulty = ("hard")
    print("Q.1-what is the signature move of yvetal")
    print("please type full lowercase with only 1 space")
    print("type in full lowercase with one lowercase")
    h1 = input("")
    if h1 == "oblivion wing":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is oblivion wing")
    print("Q.2-what is the signature move of darkrai")
    print("please type in lowercase with one space")
    h2 = input("")
    if h2 == "dark void":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is dark void")
    print("Q.3-what is the singature move of xerneas")
    print("type in full lowercase")
    h3 = input("")
    if h3 == "geomancy":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong ")
        print("the correct answer is geomancy")
    print("Q.4-which pokemon has one of its signature moves as lands wrath")
    print("type in full lowercase")
    h4 = input("")
    if h4 == "zygarde":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is zygarde")
    print("Q.5-which pokemon has the signature move king's shield")
    print("type in full lowercase")
    h5 = input("")
    if h5 == "aegislash":
        print("your answer is correct")
        i += 1
        print(i)
        exit()
    else:
        print("your answer is wrong")
        print("the correct answer is aegislash")
        print(i)
        exit()

if difficulty == ("4"):
    print("you chose insane difficulty")
    difficulty = ("insane")
    print("Q.1-which pokemon was in place of ashs pickachu at first")
    print("type in full lowercase")
    s1 = input("")
    if s1 == "clefairy":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is clefairy")
    print("Q.2-which was the first pokemon made by the devs")
    print("type in full lowercase")
    s2 = input("")
    if s2 == "rhydon":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is rhydon")
    print("Q.3-who is the composer of pokemon")
    print("type in lowercase with one space")
    s3 = input("")
    if s3 == "junichi masuda":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is junichi masuda")
    print("Q.4-who is the director of pokemon")
    print("type in lower case with one space")
    s4 = input("")
    if s4 == "satoshi tajiri":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is satoshi tajiri")
    print("Q.5-what is the pokemon raichu should have evolved into but got scraped")
    print("type in full lowercase")
    s6 = input("")
    if s6 == "gorochu":
        print("your answer is correct")
        i += 1
    else:
        print("your answer is wrong")
        print("the correct answer is gorochu")
    print("Q.6-which is the first pokemon in pokedex")
    print("type in full lowercase")
    s5 = input("")
    if s5 == "bulbasaur":
        print("your answer is correct")
        i += 1
        print("your points")
        print(i)
        exit()
    else:
        print("your answer is wrong")
        print("the correct answer is bulbasaur")
        print("your points")
        print(i)
        exit()