from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Open the file.
    open_file = open(file_path)

    # Turn the file into one long string.
    whole_file = open_file.read()

    return whole_file

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    dict_chains = {}

    #  Split the words by spaces in the file that is now a string.
    indiv_words = text_string.split()

    #  For every value in the string, up to and including the last word.
    for num in range(0, len(indiv_words)- 2):

        # The word at the current index becomes the first word in the key.
        first_key = indiv_words[num]      

        # The word at the following index becomes the second word in the key.      
        second_key = indiv_words[num + 1]

        # The word following second_key will be called third_word.
        third_word = indiv_words[num + 2]

        # We will make a key using the first and second words grabbed.
        tuple_key = (first_key, second_key)

        # If the tuple key is not already in our dictionary,
        if tuple_key not in dict_chains:

            # Our current empty dictionary
            dict_chains[tuple_key] = []

            # Add the key to and the value (third_word) to the dictionary.
            dict_chains[tuple_key].append(third_word)

        # If the key is already in the dictionary, add the third_word to its 
        # value.    
        else:
            dict_chains[tuple_key].append(third_word)

    # Return our dictionary.
    return dict_chains
   

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # Create a variable that lists all the keys.
    list_of_keys = chains.keys()         

    # Create variable that generates one random key.
    random_key = choice(list_of_keys)   

    # Initialize our text with a single random key.
    text = random_key[0]

    # While the key exists in our dictionary,
    while random_key in chains:

        # Add it to our text.
        text = text + " " + random_key[1]

        # Grab the list of values associated with the random_key.
        list_associated_with_key = chains[random_key]
                                  
        # Grab a random word from that list.                                               
        word = choice(list_associated_with_key)     

        # Set a new random key using the second word in the key and the word
        # that was just used.
        random_key = (random_key[1], word)         
    
    # Show us the text.
    return text



# Put the file that you want to apply Markov Magic to.
input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
