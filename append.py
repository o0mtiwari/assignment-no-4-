user_input = input("Enter text to write to the file")

with open('output.txt', 'r+')as file:
    file.write(user_input)

additional_input = input("Enter additional text to append to the file:")

with open("output.txt","r+") as file:
    file.write(additional_input)

print("Final content of output.txt")
with open("output.txt", "r+") as file:
    for line in file:
        print(line.strip())