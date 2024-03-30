str=input("enter a string:")
str.split
for val in str:
	c=str.count(val)
	print(f"{(val)}:{(c)}")