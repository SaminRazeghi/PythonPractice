key = int(input("Please enter the key:"))
text = input("please enter the text:")
ans = []
for i in range(len(text)):
    if text[i] == " ":
        ans.append(" ")
    else:
        ans.append(chr((ord(text[i]) + key - 65) % 26 + 65))
        #chr(ord(text[i]) + key)
    i = i+1
print(''.join(ans))
