a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for number in a:
    if(number < 5):
        #print(number)
        b.append(number)

print('b list is: ' + str(b))
