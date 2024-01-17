# Use with as automatically closes the file without putting f.close()
with open("Python/sandbox/withAs.txt", 'w') as f:
    f.write("my first file\n")
    f.write("This file\n")
    f.write("contains three lines\n")

# Dynamic with as 
file_path = "Python/sandbox/dynaWithAs.txt"
with open(file_path, 'w') as file:
    file.write("Welcome to Python!!")

print(f"Content has been written to {file_path}")
