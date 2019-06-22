"""
A simple function that finds the first recurring letter found in a given string.
It returns a new string with letters that appears more than once.
If the function does not find any recurring letters, then it will return None.
The function first creates a frequency table for a given string and an empty string.
Then goes through a loop to find if the value of that key (letter) is more than one.
If the value is indeed greater than one, it will add the key to the empty string.
If the new string is empty, the function returns 'No recurring letters.'
I chose to create a frequency table rather than looping through a given string
character by character as it takes less time to iterate through a dictionary.
"""

# given short strings examples
first = 'ABCA'
second = 'BCABA'
third = 'ABC'

# long string
fourth = 'DEDDGILOJEHBKJHDFLKJFKGJKLDFJKHKJGHVCMLSIIIENGSJDKJICUYWKEJBF'

# function for finding first recurring letter and takes in a string argument
def recurring_letter(a_str):
    
    # initialize empty dictionary for frequency table
    counts = {}
    
    # initialize empty string
    new_str = ""
    
    # loop through characters of given string
    for char in a_str:
        
        # if the character(key) is already in the table
        # increment the value count by one
        # otherwise, give the key a value of one
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            
    # loop through the keys and values in frequency table
    for key, val in counts.items():
        
        # if the value of the key is greater than one, meaning it occurred more than once
        # add the key to the new string
        if val > 1:
            new_str += key
            
    # after both loops finish and if the new string did not find any recurring letters
    # return string statement: 'No recurring letters.'
    if new_str == "":
        return 'No recurring letters.'
    return new_str
      
# short strings  
d, e, f = recurring_letter(first), recurring_letter(second), recurring_letter(third)
print(d)
print(e)
print(f)

# long string
g = recurring_letter(fourth)
print(g)