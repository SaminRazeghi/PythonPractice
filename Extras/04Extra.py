Numbers = input('Enter the numbers: ').split(" ")
TvChannels = []
CurrentChannel = int(Numbers[1])
Presses = int(Numbers[2])
for i in range(0, int(Numbers[0])):
    temp = input('Enter the channel name:')
    TvChannels.append(temp)
print(TvChannels[CurrentChannel + (Presses % int(Numbers[0])) - 1])
