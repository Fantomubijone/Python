# pag isa lang gusto ko 
file = open("Python/sandbox/UserInput.txt", 'r')
line = file.readlines()
for words in line:
    print(words)

file.close()


# read per line
file = open("Python/sandbox/UserInput.txt", 'r')
line = file.readline()
while line != '':
    print(line,end='')
    line = file.readline()
file.close