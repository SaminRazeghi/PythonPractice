def Reverse(number):
    final = 0
    while number != 0:
        temp = number % 10
        final = final * 10 + temp
        number //= 10
    return final


print("Give me a number:")
r = int(input())
ans = 0
while r != -1:
    ans = ans + Reverse(r) * 2
    print("Give me a number:")
    r = int(input())
print(ans)
