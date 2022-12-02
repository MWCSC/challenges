import math

Password = "jh0g45j0jfgm40fghy7ut03d20fhn0gf400057q0wd12vcx4089pyi231400gjh0"

Characters = []

for index in range(len(Password)):
  try:
    if (int(Password[index]) > 0):
      Characters.append(Password[index])
  except:
    continue

encrypted_passcode = ""

initial_passcode_length = len(Characters)

for iterations in range(initial_passcode_length):

  greatest_value = 0
  index_to_remove = -1

  for index in range(len(Characters)):
    if (int(Characters[index]) > greatest_value):
      greatest_value = int(Characters[index])
      index_to_remove = index
  encrypted_passcode += Characters[index_to_remove]
  
  Characters.pop(index_to_remove)


print(encrypted_passcode)
