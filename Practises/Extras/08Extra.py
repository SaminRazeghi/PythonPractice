X = input('Please give me the coordinates: ').split(" ")
for i in range(0, len(X)):
    X[i] = int(X[i])
if X[0] == X[2]:
    print("Vertical")
elif X[1] == X[3]:
    print("Horizontal")
else:
    print("Try again")
