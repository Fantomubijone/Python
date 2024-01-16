import math

# Solving for Heron

# Getting user input
sideA = float(input("Enter the length side a: "))
sideB = float(input("Enter the length side b: "))
sideC = float(input("Enter the length side c: "))

# Solving for semi-perimeter
semi = (sideA + sideB + sideC) / 2.0

# Soling for the Area
area = math.sqrt(semi * (semi-sideA) * (semi-sideB) * (semi-sideC))

print("The area of the triangle is: %.2f" % area)