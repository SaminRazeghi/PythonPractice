squer = input('Please give me the coordinates: ').split(" ")
for i in range(0, len(squer)):
    squer[i] = int(squer[i])
print(squer)
length = input('Please enter the length: ')
print(length)
Glass = input('Please give me the glass coordinates: ').split(" ")
for i in range(0, len(Glass)):
    Glass[i] = int(Glass[i])
print(Glass)
if (squer[0] <= Glass[0]) and (Glass[0] <= squer[0] + int(length)):
    if (squer[1] - int(length) <= Glass[1]) and (Glass[1] <= squer[1]):
        print("Mehdi")
    else:
        print("Parsa")
else:
    print("Parsa")
