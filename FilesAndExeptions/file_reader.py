with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    lines = file_object.readlines()

for line in lines:
    print(line)

print(lines)

