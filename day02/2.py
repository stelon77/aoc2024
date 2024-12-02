def verif(numbers):
    # verif de la ligne
    sens = 0
    error = 0
    for i in range(len(numbers) - 1):

        if abs(int(numbers[i]) - int(numbers[i + 1])) > 3 or int(numbers[i]) == int(numbers[i+ 1]):
            error = 1
            break
        if (int(numbers[i + 1]) - int(numbers[i])) > 0:
            if sens < 0:
                error = 1
                break
            sens = 1
        if (int(numbers[i + 1]) - int(numbers[i])) < 0:
            if sens > 0:
                error = 1
                break
            sens = -1
    return(not error)


total = 0
with open("input.txt") as fillin:
    lignes = fillin.readlines()
for line in lignes:
    numbers = line.split()
    if verif(numbers):
        total += 1
    else:
        for i in range(len(numbers)):
            number = list(numbers)
            del number[i]
            if verif(number):
                total += 1
                break


print(total)