from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_file = open(file_path)
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



    indiv_words = text_string.split()

    for num in range(0, len(indiv_words)- 2):
        first_key = indiv_words[num]
        second_key = indiv_words[num + 1]
        third_word = indiv_words[num + 2]
        tuple_key = (first_key, second_key)
        if tuple_key not in dict_chains:
            dict_chains[tuple_key] = []
            dict_chains[tuple_key].append(third_word)
        else:
            dict_chains[tuple_key].append(third_word)

    return dict_chains
    

    

   

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    list_of_keys = chains.keys()        # Create a variable that lists all the keys. 

    random_key = choice(list_of_keys)   # Create variable that generates one random key.

    text = random_key[0]

    while random_key in chains:
        text = text + " " + random_key[1]

        list_associated_with_key = chains[random_key] #this var references the list associated
                                                        #with the random_key
        word = choice(list_associated_with_key)     #word is a random word from the list

        random_key = (random_key[1], word)         # Create a key out of the second word in the first
    
                                            # key and a random word from the list of words.
    return text




input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

#print chains

# Produce random text
random_text = make_text(chains)

print random_text
