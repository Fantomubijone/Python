file = open("Python/sandbox/UserInput.txt", 'w')
for i in range(3):
    name = input("Enter the name of the employee: ")
    file.write(name)
    file.write("\n")

file.close()

print("Data is written into the file")