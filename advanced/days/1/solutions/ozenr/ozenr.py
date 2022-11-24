# Variables
encryptedPasswd = "jh0g45j0jfgm40fghy7ut03d20fhn0gf400057q0wd12vcx4089pyi231400gjh0"
nums = []
passwd = 0;

# Get All Numbers 
for num in encryptedPasswd:
  if num.isdigit() and int(num) > 0:
    nums.append(num)

# Sort Numbers From Descending Order
nums.sort(reverse=True)

# Final Password
passwd = int(''.join(nums))
print(passwd)
