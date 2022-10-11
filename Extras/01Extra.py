def pooya():
    A = int(input('How many days does the first person come to quera?'))
    Aa = input('Which days are they?').split(" ")
    B = int(input('How many days does the second person come to quera?'))
    Bb = input('Which days are they?').split(" ")
    C = int(input('How many days does the second person come to quera?'))
    Cc = input('Which days are they?').split(" ")
    days = ["shanbe", "1shanbe", "2shanbe",
            "3shanbe", "4shanbe", "5shanbe", "jome"]
    final = set(days) - set(Aa) - set(Bb) - set(Cc)
    # print(len(final))
    return len(final)


pooya()
