
print("Printing current and previous number sum in a range(10)")

prev = 0
for x in range (0,10):
    print(f"Current Number {x} Previous Number is {prev} Sum = {x + prev}")
    prev = x