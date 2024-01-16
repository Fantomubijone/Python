# Read between the lines

# Getting user input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Solving the slope
slope = (y2-y1) / (x2-x1)
intercept = y1 - slope * x1

if(intercept < 0):
    print("The equation of the line is: y = %.2fx %.2f" % (slope,intercept))
else:
    print("The equation of the line is: y = %.2fx + %.2f" % (slope,intercept))

