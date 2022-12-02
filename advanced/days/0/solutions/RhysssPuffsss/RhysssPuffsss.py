import math
Measurement_1 = 2546375247
Measurement_2 = 45987482082
hyp = math.sqrt(Measurement_1 ** 2 + Measurement_2 ** 2)
Perimeter = Measurement_1 + Measurement_2 + hyp
Area = (Measurement_1 * Measurement_2)/2
print(int(Perimeter))
print(int(Area))
