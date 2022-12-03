# Global Variables
bruhWhatIsThisFile = open("input.txt", "r") 
lines = bruhWhatIsThisFile.readlines()
hpos = 0
nums = 1

# Find Letter H And Number in Each Line
for line in lines:
  for char in line:
      if char.__eq__("h"):
        hpos += (line.index("h"))
      if char.isdigit():
        nums *= int(char)

finalNum = hpos * nums
print(finalNum)
