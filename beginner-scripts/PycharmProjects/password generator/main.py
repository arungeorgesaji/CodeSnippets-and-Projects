import random
print("this program generates 20 digit password")
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
         "u", "v", "w", "x", "y", "z"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["#", "*", "@", "&"]
password1 = random.choice(lower)
password2 = random.choice(lower)
password3 = random.choice(num)
password4 = random.choice(lower)
password5 = random.choice(lower)
password6 = random.choice(num)
password7 = random.choice(num)
password8 = random.choice(lower)
password9 = random.choice(symbol)
password10 = random.choice(lower)
password11 = random.choice(symbol)
password12 = random.choice(num)
password13 = random.choice(symbol)
password14 = random.choice(symbol)
password15 = random.choice(lower)
password16 = random.choice(lower)
password17 = random.choice(num)
password18 = random.choice(num)
password19 = random.choice(lower)
password20 = random.choice(lower)
upper1 = str(password2.upper())
upper2 = str(password4.upper())
upper3 = str(password5.upper())
upper4 = str(password19.upper())
upper5: str = str(password20.upper())
print("your password is " + password1 + upper1+password3 + upper2+upper3 + password6 + password7 +
      password8 + password9 + password10 + password11 + password12 + password13 + password14 + password15 +
      password16 + password17 + password18 + upper4 + upper5)
