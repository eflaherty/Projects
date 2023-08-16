def check_anagrams(string1, string2):
    print(f'original string1 is: {string1}')
    sorted_string1 = sorted(string1)
    print(f'sorted_string1 is: {sorted_string1}')
    print(f'original string2 is: {string2}')
    sorted_string2 = sorted(string2)
    print(f'sorted_string2 is: {sorted_string2}')

    if (sorted_string1 == sorted_string2):
        print("\nThe strings are anagrams.")
    else:
        print("\nThe strings are not anagrams.")

s1 = 'evil2'
s2 = 'live'
check_anagrams(s1, s2)
