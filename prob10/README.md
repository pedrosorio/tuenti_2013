The inputs are interleaved strings and recursive strings (which are found between [] and preceded by integers). 

For example aa2[b3[2[e]d]]4[fg] is aabeedeedeedbeedeedeedfgfgfgfg. 

The output is the md5 hash of the "unrolled string".

Since the input may be too big to contain in memory at once, in order to solve this problem, a class ImpStr (Implicit String) is created. 

Essentially, each implicit string contains an interleaved sequence of strings and Implicit Strings (with the associated number of times it is repeated).

The fundamental (recursive) method in the class is "get" which appends to an array the first **ilen** characters starting at the **istart-th** character of the implicit string. 

Since python provides a method to compute the md5 hash of a string, and update this hash by passing the suffixes iteratively, the get method is used to fetch the string by parts, until the final answer is computed.