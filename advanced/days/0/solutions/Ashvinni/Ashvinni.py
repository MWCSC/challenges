import math

b = 2546375247
h = 45987482082

area = (b * h) / 2
c = math.sqrt((b * b) + (h * h))
perimeter = b + h + c

print(int(area))
print(int(perimeter))
