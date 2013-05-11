Each cipher text is the result of a key XOR'ed with the plaintext. The problem resides in finding this key.

In order to do so, findkey has a scoring function for each character (how likely it would be to find it in the plaintext). There is nothing fancy here like character frequencies and so on, simply "lowercase letters and spaces should be very likely, punctuation and uppercase letters less likely".

With this information, for each character the code tries every possible byte (0-255) as key and chooses the one that gives the largest score to the plaintext derived from all the keys found in cyphers.txt. Any byte that results in a character outside of the accepted ones (although the code is not exactly that, it should be anything in the ASCII range 32-126), is rejected altogether as a possible key (even if the other cyphertexts would have resulted in a higher score).

After this, the key and the resulting plaintexts are output. Eyeballing the results gives an idea of the characters that are mistaken in certain positions. These are included in the code until the key that makes all the plaintexts correct is found.

After this, receiving input and decoding is trivial.

Fun improvement: actually use a dictionary to improve the key selection greatly and make the process fully automatic.