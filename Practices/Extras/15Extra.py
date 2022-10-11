import operator as op
from collections import Counter


def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


N = int(input('Enter number of employees: '))
names = []
for i in range(N):
    temp = input('Enter the names: ').split(" ")
    names.append(temp[0])
print(op.countOf(names, most_frequent(names)))
