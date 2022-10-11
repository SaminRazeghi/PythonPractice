XL = input('Please give me the shirt sizes: ').split(" ")
for i in range(0, len(XL)):
    XL[i] = int(XL[i])
Sizes = input('Please give me the winner sizes: ').split(" ")
for i in range(0, len(Sizes)):
    Sizes[i] = int(Sizes[i])
if Sizes[0] <= XL[0]:
    if Sizes[1] <= XL[1]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
