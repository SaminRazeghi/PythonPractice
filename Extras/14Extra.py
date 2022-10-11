N = int(input('Number of keys: '))
keys = []
for i in range(N):
    keys.append(input('Enter the key: '))
i = 0
ans = ""
flag = False
for i in range(0, len(keys)):
    if flag == True:
        keys[i] = keys[i].upper()
    elif flag == False:
        pass
    if keys[i] == "CAPS":
        flag = not flag
keys = [value for value in keys if value != 'CAPS']
print("".join(keys))
