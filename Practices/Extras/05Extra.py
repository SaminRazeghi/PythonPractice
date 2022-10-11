numbers = int(input('Numbers of the alphabets: '))
sample = [*input('Enter the test sample: ')]
answer = [*input('Enter answer: ')]
counter = 0
for i in range(numbers):
    if sample[i] != answer[i]:
        counter += 1
print(counter)
