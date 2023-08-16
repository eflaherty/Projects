## Explanation: In the program, first take input from the user (using input OR raw_input() method) to check for palindrome.
#  Then using slice operation [start:end:step], check whether the string is reversed or not.
#  Here, step value of -1 reverses a string. If yes, it prints a palindrome else, not a palindrome.

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")
