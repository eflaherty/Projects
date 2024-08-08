i = 4
d = 4.0
s = 'HackerRank '

import sys

# Declare second integer, double, and String variables.
# not necessary in python
second_int = 0
double_number = 0.0
string = 'Second string'

# Read and save an integer, double, and String to your variables.
# for line in sys.stdin:
#    print(line.rstrip())
#    if 'q' == line.rstrip():
#        break

S = sys.stdin.readlines()
print(S)
for i in S:
    second_int = S[0]
    print(second_int)
    double_number = S[1]
    print(double_number)
    string = S[2]
    print(string)

# second_int = int(input("Please enter an integer:\n"))
# double_number = float(input("Please enter a double number:\n"))
# string = input("Please enter a string:\n")

# Print the sum of both integer variables on a new line.
print(i + second_int)

# Print the sum of the double variables on a new line.
print(d + double_number)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + string)
