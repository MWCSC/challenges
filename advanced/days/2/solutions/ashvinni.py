FILE = open("input.txt", "r").readlines()

# find and add the position of h on each line to list
hpos = []
for line in FILE:
    hpos.append(line.find("h"))

# sum of all the h positions
sum_hpos = 0
for i in hpos:
    sum_hpos += i

# find and store the value after each letter h for each line
values = []
for line in range(len(FILE)):
    values.append(FILE[line][hpos[line] + 1])
# convert the value list into one string
int_values = "".join(values)

# find the product of all the values
product_values = 1
for i in int_values:
    product_values *= int(i)

print(sum_hpos * product_values)
           
