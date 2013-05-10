Run the executable generated from prob4.cpp, giving as input the path to the integers file.
This uses an array with 2^28 bytes, which is indexed bit-by-bit (8 * 2^28 = 2^31) to check all the integers in the file.

A loop over the 2^31 integers finds the unset bits and outputs the 100 missing integers (saved in a file).

Given this pre-processing, it is possible to use prob4.py to process the input and return any of the 100 integers instantaneously.