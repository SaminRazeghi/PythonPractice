from pickletools import string4
Chocolate = input('Enter the numbers: ').split(" ")
for i in range(0, len(Chocolate)):
    Chocolate[i] = int(Chocolate[i])
temp = 0
max = sum(Chocolate)
table = {0: 0, 1: 0, 2: 0, 3: 0}
print("     " + str(table[0]) + "\n" + "     " + str(Chocolate[0]) + "\n" + str(table[3]) + "  " + str(Chocolate[3]) + "    " + str(Chocolate[1]) + "  " +
      str(table[1]) + "\n" + "     " + str(Chocolate[2]) + "\n" + "     " + str(table[2]))
print("**********")
for x in range(0, max):
    i = x % 4
    if Chocolate[i] == 0:
        break
    else:
        table[i] = table[i] + 1
        Chocolate[i] = Chocolate[i] - 1
        temp = Chocolate[0]
        Chocolate[0] = Chocolate[1]
        Chocolate[1] = Chocolate[2]
        Chocolate[2] = Chocolate[3]
        Chocolate[3] = temp
        print("     " + str(table[0]) + "\n" + "     " + str(Chocolate[0]) + "\n" + str(table[3]) + "  " + str(Chocolate[3]) +
              "    " + str(Chocolate[1]) + "  " + str(table[1]) + "\n" + "     " + str(Chocolate[2]) + "\n" + "     " + str(table[2]))
        print("************")
if i - 1 == -1:
    table[3] = table[3] - 1
else:
    table[i - 1] = table[i - 1] - 1
print(table)
