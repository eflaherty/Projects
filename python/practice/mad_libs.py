""" Mad Libs Generator
---------------------------
"""
# Loop back to this point once code finishes
loop = 1
while (loop < 10):
    # All the questions to ask the user
    noun = input("choose a noun: ")
    p_noun = input("choose a plural noun: ")
    noun_2 = input("choose a noun: ")
    place = input("name a place: ")
    adjective = input("choose an adjective (describing word): ")
    noun_3 = input("choose a noun: ")
    # Display the story based on the users input
    print ('---------------------------------------------')
    print (f'Be kind to your {noun}-footed {p_noun}')
    print (f'For a duck may be somebody\'s {noun_2},')
    print (f'Be kind to your {p_noun} in {place}')
    print (f'Where the weather is always {adjective},')
    print ()
    print (f'You may think that is this the {noun_3},')
    print (f'Well it is.')
    print ('---------------------------------------------')
    # Loop back
    loop = loop + 1
