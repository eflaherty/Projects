low = input('Please enter the low ended number: ')
high = input('Please enter the high ended number: ')

for n in range(low, high+1):
    if ((n % 3 == 0) & (n % 5 == 0)):
        print("fizzbuzz")
        continue
    elif n % 3 == 0:
        print("fizz")
        continue
    elif n % 5 == 0:
        print("buzz")
        continue
    else:
        print(n)
        continue
