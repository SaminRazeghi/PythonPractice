M, N = input('M and N: ').split(" ")
if int(M) % int(N) == 0:
    ans = int(M)/int(N)
else:
    ans = int(M)/int(N) + 1
print(int(ans))
