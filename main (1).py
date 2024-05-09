x = int(input("what do you want the staring number to be?"))
y = int(input("what do you want the ending number to be?"))
with open("output.txt", "w") as file:
  for number in range(x, y + 1):
      file.write("DELAY 100\nSTRING " + str(number) + "\n")
      print("DELAY 100\nSTRING " + str(number) + "\n")
