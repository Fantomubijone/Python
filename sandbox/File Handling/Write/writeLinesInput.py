file = open("Python/sandbox/listInput.txt", 'w')
lst = []
for i in range(3):
    name = input("Enter the name of the employee: ")
    lst.append(name + "\n")

file.writelines(lst)
file.close()

print("Data has been added to the file")