print("Enter the number of rounds:")
n = int(input())
i = 1
print("START")
while i in range(n+1):
    if i % 5 == 0:
        print("HOP!")
    else:
        print(i)
    i = i + 1
