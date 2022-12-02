my_list = []
password = "jh0g45j0jfgm40fghy7ut03d20fhn0gf400057q0wd12vcx4089pyi231400gjh0"

for n in password:
  if n.isdigit() and int(n) > 0:
    my_list.append(int(n))
    
my_list.sort(reverse = True)
result = "".join(str(n) for n in my_list)
print(int(result))
