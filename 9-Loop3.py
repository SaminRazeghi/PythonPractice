import math
print("Please enter the radian:")
r = float(input())
print("please enter n:")
n = int(input()) * 2
ans = ["(1/1)"]
sign = -1
i = 2
while i in range(n):
    if sign < 0:
        ans.append("+")
    else:
        ans.append("-")
    temp3 = "(" + str(int((r ** i))) + "/" + str(math.factorial(i)) + ")"
    ans.append(temp3)
    sign = sign * -1
    i = i + 2

print(' '.join(ans))
