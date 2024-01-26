print("\n==========================================")
print(" ACTIVITY 3.1 Character Existence")

print("\n ENTER A STRING: ", end = "")
phrase = input()

# declaring a empty dictionary
chars = {}

for x in phrase:
    # checking index or key if it occurs again then add 1 
    if x in chars:
        chars[x] += 1
    # if the key or index we are going to set it by 1 to be included in the dict    
    else:
        chars[x] = 1

# Creating or opening chars.txt
file = open("chars.txt", 'w')

# accesing dictionary using for loop
# k represents the key or the character
# v is for the value or occurances
for k,v in dict.items(chars):
    file.write(f"{k}: {v} times(s)\n")

file.close()
print(f" {phrase} has been added to chars.txt")
print("==========================================\n")
