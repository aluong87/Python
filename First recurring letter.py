"""
A simple function that finds the first recurring letter found in a given string.
It returns a new string with letters that appears more than once.
If the function does not find any recurring letters, then it will return another string.
The function first creates a frequency table for a given string, and an empty string.
Then iterates through the table to find if the value of that key (character) is more than one.
If the value is indeed greater than one, it will add the key (character) to the new string.
Otherwise, the new string will be empty.
If the new string is empty, the function returns 'No recurring letters.'
I chose to create a frequency table rather than iterating through a given string because looping
character by character takes more time than iterating through a dictionary.
"""

# function for finding first recurring letter and takes in a string argument
def recurring_letter(a_str):
    
    # initialize empty dictionary for frequency table
    counts = {}
    
    # initialize empty string
    new_str = ""
    
    # interate through characters of given string
    for char in a_str:
        
        # if the character(key) is already in the table
        # increment the value count by one
        # otherwise, give the key a value of one
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            
    # iterate through the keys and values in frequency table
    for key, val in counts.items():
        
        # if the value of the key is greater than one, meaning it occurred more than once
        # add the key to the new string
        if val > 1:
            new_str += key
            
    # after both iterations finish and if the new string did not find characters > one
    # return a string: 'No recurring letters.'
    if new_str == "":
        return 'No recurring letters.'
    return new_str
      

# examples
first = 'ABCA'
second = 'BCABA'
third = 'ABC'
fourth = 'DEDDGILOJEHBKJHDFLKJFKGJKLDFJKHKJGHVCMLSIIIENGSJDKJICUYWKEJBF'

d, e, f, g = recurring_letter(first), recurring_letter(second), recurring_letter(third), recurring_letter(fourth)
print('Finding recurring letters...\n')
print(first)
print(d + '\n')
print(second)
print(e + '\n')
print(third)
print(f + '\n')
print(fourth)
print(g)


# Output:
"""
Finding recurring letters...

First string: ABCA
A

Second string: BCABA
BA

Third string: ABC
No recurring letters.

Fourth string: DEDDGILOJEHBKJHDFLKJFKGJKLDFJKHKJGHVCMLSIIIENGSJDKJICUYWKEJBF
DEGILJHBKFCS
"""
