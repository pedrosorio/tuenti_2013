In order to find the words that have the same character counts efficiently, it is possible to preprocess a dictionary by doing:

    ./prob2 dictionary_name

* The character counts are represented in 52 bytes, allowing up to 65535 (2^16) occurrences of each character in a word
* The dictionary in the file dictionary_name is preprocessed, generating a hash map between character counts and vectors of word positions in the dictionary (0-based)
* The hash map is saved in a file dictionary_name"_preprocessed"

Running:

    ./prob2
    
* The program reads from the standard input, and loads the hash map of the preprocessed dictionary, as well as the dictionary itself
* For each word in the input, the character counts are computed and the hash map is used to find the words that have the same counts in O(1)
* The words are sorted lexicographically and printed


For greater efficiency it would be possible to keep a dictionary with fixed
word-width and use seek functions to retrieve the wanted words, instead of
reading the whole dicionary to memory prior to processing the inputs. 

