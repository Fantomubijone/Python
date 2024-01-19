row = int(input('Enter a number: '))

if row <= 0:
    print("[INVALID] Enter a Positive Integer!!")
else:
    for i in range(1, row+1):
        for j in range(i):
            print(j + 1, end = " ")
        print("")

