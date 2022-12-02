password = "jh0g45j0jfgm40fghy7ut03d20fhn0gf400057q0wd12vcx4089pyi231400gjh0"
nums = []

for i in password:
    if i.isdigit() and int(i) > 0:
      nums.append(int(i))

while password:
  print(nums.pop(0))
  nums.reverse()
