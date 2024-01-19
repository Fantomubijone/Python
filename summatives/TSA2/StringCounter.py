text = input("Enter a word: ")

# Setting a list of vowels for basis
vowels = ['a','e','i','o','u']

vowelCount = 0
spaces = 0
totalChar = 0


for i in text:
    # Counter for spaces
    if(' ' in i):
        spaces += 1

    # For counting ALPHABETS AND NUMBERS 
    if(i.isalnum()):
        totalChar += 1

    # Counting Vowels
    if(i.lower() in vowels):
        vowelCount += 1


print(f"\nNumber of characters: {totalChar}")
print(f"Number of vowels: {vowelCount}")
print(f"Number of spaces: {spaces}")
print(f"Number of commas: {text.count(',')}")
print(f"Number of periods: {text.count('.')}")

