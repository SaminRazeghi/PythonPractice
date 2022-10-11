x, n = input('Enter x and n: ').split(" ")
x = int(x)
L = 0
M = 0
R = 0
if n == "L":
    L = 1
elif n == "M":
    M = 1
elif n == "R":
    R = 1
for i in range(x):
    move = input('Enter your move: ')
    if move == "L M ":
        temp = L
        L = M
        M = temp
    elif move == "L R":
        temp = L
        L = R
        R = temp
    elif move == "M R":
        temp = M
        M = R
        R = temp
    elif move == "R M":
        temp = R
        R = M
        M = temp
    elif move == "R L":
        temp = R
        R = L
        L = temp
    elif move == "M L":
        temp = M
        M = L
        L = temp

if M == 1:
    print("M")
elif L == 1:
    print("L")
else:
    print("R")
