import random

rarity = ['common', 'rare', 'epic', 'legendary']
print("how many spins you want to do 1 or 10")
spins = input("spins:")
got = ("")
if spins == "1":
    print("you chose to do 1 spin")
    got = random.choices(rarity, weights=[50,
                                          40, 9, 1], k=1)
elif spins == "10":
    print("you chose to do 10 spins")
    got = random.choices(rarity, weights=[50, 40, 9, 1], k=10)
else:
    got == ("")
    print("this field is required")
    print("how many spins you want to do")
    spins = input("")
    got = ("")

print("you got" + str(got))