list_1 = input('Enter your integers, sepatate them by , example: 3,4,5 \n')
list_1 = list_1.split(",")
list_1 = [int(n) for n in list_1]
i = 0
while list_1[i] % 2 == 0:
    if i == len(list_1) - 1:
        print('all numbers are even')
        break
    i = i + 1
    continue

else:
    print('NO')
