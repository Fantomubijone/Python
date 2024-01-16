# Formatting Output using F

# Getting user input
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

#solving for each operation
sum = num1 + num2
diff = num1 - num2
qou = num1 // num2
pro = num1 * num2

# Displaying output for each operation
print(f"\nThe sum of {num1} and {num2} is {sum}.")
print(f"The difference of {num1} and {num2} is {diff}.")
print(f"The product of {num1} and {num2} is {pro}.")
print(f"The qoutient of {num1} and {num2} is {qou}.")
