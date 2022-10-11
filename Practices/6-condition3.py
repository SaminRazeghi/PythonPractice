from tokenize import Double
print("What grade are you in?")
Grade = int(input())
Status = True

if Grade == 1:
    print("Frist subject score:")
    Score1 = float(input())
    if Score1 < 10:
        Status = False
    print("Second subject score:")
    Score2 = float(input())
    if Score2 < 10:
        Status = False
    print("Average:", float((Score1 + Score2) / 2))

elif Grade == 2:
    print("Frist subject score:")
    Score1 = float(input())
    if Score1 < 10:
        Status = False
    print("Second subject score:")
    Score2 = float(input())
    if Score2 < 10:
        Status = False
    print("Third subject score:")
    Score3 = float(input())
    if Score3 < 10:
        Status = False
    print("Average:", float((Score1 + Score2 + Score3) / 3))

elif Grade == 3:
    print("Frist subject score:")
    Score1 = float(input())
    if Score1 < 10:
        Status = False
    print("Second subject score:")
    Score2 = float(input())
    if Score2 < 10:
        Status = False
    print("Third subject score:")
    Score3 = float(input())
    if Score3 < 10:
        Status = False
    print("Fourth subject score:")
    Score4 = float(input())
    if Score4 < 10:
        Status = False
    print("Average:", float((Score1 + Score2 + Score3 + Score4) / 4))
if Status == False:
    print("Failed")
else:
    print("Passed")
