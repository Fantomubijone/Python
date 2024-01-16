# Formatting Output using String format

# Getting user input
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

#solving for each operation
sum = num1 + num2
diff = num1 - num2
qou = num1 // num2
pro = num1 * num2

# Displaying output for each operation
print("\nThe sum of {} and {} is {}.".format(num1,num2,sum))
print("The difference of {} and {} is {}.".format(num1,num2,diff))
print("The product of {} and {} is {}.".format(num1,num2,pro))
print("The qoutient of {} and {} is {}.".format(num1,num2,qou))



