file = open("bgyo.txt", 'r')

# setting a counter to indicate the lines that deosnt start with T
isnotT = 0

print("\n==========================================")
print(" ACTIVITY 3.2 NOT MY T")

# accessing the file bgyo.txt
for line in file:  
    # checking if the line not starts with T
    if line and not line.startswith("T"):
        isnotT += 1 # increament the counter to one if the line doesnt start with T

file.close()

# displaying how many line doesnt starts with T
print(f" Number of lines not starting with 'T': {isnotT}")
print("==========================================\n")
