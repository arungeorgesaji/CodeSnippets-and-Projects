y=("2")
ans=("")
x2=("")
lp=("yes")
"""skips a line"""
skipper=("")

while lp=="yes":
	print("this software can only handle numbers upto 15 digits")
	x=(input("please insert a number:"))
	while x.isnumeric()==False:
		print(skipper)
		print("error_thats not a numeric number _error")
		x=(input("please insert a number:"))
	if x.isnumeric()==True:
		x=float(x)
		y=float(y)
		ans=x%y
		print(ans)
		ans=str(ans)
	if ans=="0.0":
		print('thats an even number')
	else:
		print('that an odd number')
		print(skipper)
	print("do you want to do it again")
	lp=input("yes or no:")
	if lp=="yes":
		pass
	elif lp=="no":
		print("thankyou for using this app,we hope to see you again")
		exit()
	else:
		print("tell yes or no you want to  do it again or we will have to stop the program")
		lp=input("yes or no:")
		if lp=="yes":
			pass
		elif lp=="no":
			print("thankyou for using this app,hope we see you again")
		else:
			exit()


