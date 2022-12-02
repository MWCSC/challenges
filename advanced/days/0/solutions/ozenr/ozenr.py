import math
# Side Lengths
measure_1 = 2546375247
measure_2 = 45987482082
# Formulas
hypotenuse = int(math.sqrt((measure_1**2) + (measure_2**2)))
perimeter = measure_1 + measure_2 + hypotenuse
area = (measure_1 * measure_2) / 2
# Output
print(perimeter)
print(area)
