Number_of_children = int(input('Enter the number of children: '))
Chocolate_milk = input('How much each kid wants milk ').split(" ")
for i in range(0, len(Chocolate_milk)):
    Chocolate_milk[i] = int(Chocolate_milk[i])
print(sum(Chocolate_milk))
