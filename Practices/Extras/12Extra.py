N = int(input('Enter the N: '))
Names = input('Enter names: ').split(" ")
for i in range(0, N):
    for j in reversed(range(0, i)):
        print(Names[i] + ": Salam " + Names[j] + "!")
for i in range(0, N):
    print(Names[i] + ": Khodafez bacheha!")
    for j in range(i+1, N):
        print(Names[j] + ": Kodafez " + Names[i] + "!")
