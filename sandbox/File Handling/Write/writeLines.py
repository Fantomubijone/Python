lines = ["Hello\n", "World"]
f = open("Python/sandbox/WriteLines.txt", "w")
f.writelines(lines)
f.close
print(f"Content has been written.")
