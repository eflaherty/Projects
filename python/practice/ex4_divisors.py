
user_num = int(input('Please enter a number: '))

listRange = list(range(1,user_num + 1)) # creates a list of numbers 1-50

divisorList = []

# Find all the divisors of the user entered number and add them to a list
for number in listRange:
    if user_num % number == 0:
        divisorList.append(number)

print(divisorList)
