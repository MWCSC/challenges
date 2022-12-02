file = open(
    "/Users/AnthonyToyco/Documents/challenges/advanced/days/2/input.txt", "r"
).readlines()

h_positions = []
for line in file:
    h_positions.append(line.find("h"))

values = []
for line, i in enumerate(file):
    values.append(file[line][h_positions[line] + 1])
int_values = "".join(values)

sum_values = 0
product_values = 1
for i in int_values:
    sum_values += int(i)
    product_values *= int(i)

print(sum_values * product_values)
