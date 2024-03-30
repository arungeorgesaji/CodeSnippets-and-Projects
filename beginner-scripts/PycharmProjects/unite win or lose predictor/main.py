apoint=0
opoint=0
ar1=input("your team-1st rotom:")
if ar1=="yes":
    apoint=apoint+5
elif ar1=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()
ar2=input("your team-2nd rotom:")
if ar2=="yes":
    apoint=apoint+5
elif ar2=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()
ad1=input("your team-1st drednaw:")
if ad1=="yes":
    apoint=apoint+5
elif ad1=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()
ad2=input("your team-2nd drednaw:")
if ad2=="yes":
    apoint=apoint+5
elif ad2=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()
az=input("your team-zapdos")
if az=="yes":
    apoint=apoint+15
elif az=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()
or1=input("opponent team-1st rotom:")
if or1=="yes":
    opoint=opoint+5
elif or1=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()
or2=input("opponent team-2nd rotom:")
if or2=="yes":
    opoint=opoint+5
elif or2=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()
od1=input("opponent team-1st drednaw:")
if od1=="yes":
    opoint=opoint+5
elif od1=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()
od2=input("opponent team-2nd drednaw:")
if od2=="yes":
    opoint=opoint+5
elif od2=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()
oz=input("opponent team-zapdos")
if oz=="yes":
    opoint=opoint+15
elif oz=="no":
    pass
else:
    print("some error has occured please make sure everything you typed was in full lowercase and contained the mentioned things only")
    exit()

print(apoint)
print(opoint)

