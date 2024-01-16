# Formatting Output using modulo operator


num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

#solving for each operation
sum = num1 + num2
diff = num1 - num2
qou = num1 // num2
pro = num1 * num2

# Displaying output for each operation
print("\nThe sum of %d and %d is %d." % (num1, num2, sum))
print("The difference of %d and %d is %d." % (num1, num2, diff))
print("The product of %d and %d is %d." % (num1, num2, pro))
print("The qoutient of %d and %d is %d." % (num1, num2, qou))


