def stars():
    counter = 0
    m, n = input('Give me M and N:  ').split(" ")
    for i in range(int(m)):
        map = input("Prinet the map:")
        map = [*map]
        for j in range(len(map)):
            if map[j] == "*":
                counter += 1
    return counter


stars()
