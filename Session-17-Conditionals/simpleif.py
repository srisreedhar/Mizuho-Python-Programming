 # simple If-else Condition
# collect 2 numbers from the user & print the greatest of these 2


number1 = input("enter any number1 :")
number2 = input("enter any number2 :")

number1=int(number1)
number2=int(number2)

# print the greatest of these 2

if number1>number2:
	print(number1,"is greater")
else:
	print(number2,"is greater")