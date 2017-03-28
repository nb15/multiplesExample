
# Ask for user input
userNum = input("Tell me a number. ")

# Convert to float
userNum = float(userNum)

# Example #1 : Do the doubling
# print("Double that number is {}.".format(userNum * 2))

# Do the computation
for multiple in range(0, 11):
	answer = userNum * multiple
	print("{} times {} is {}.".format(userNum, multiple, answer))