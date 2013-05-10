Since the trivial implementation of the Turing machine is incredibly slow for some inputs, another way is needed.

Since understanding the Turing machine (or finding an automatic way to simplify the algorithm and implement it in an efficient way), we are left with looking at sample inputs and outputs (generated with the naive turing machine implementation) to find a pattern. It turns out that the eligible strings are of the form:

#binary#binary#binary#...

And the output is always first binary integer * (sum of binary integers from second to the last).

Understanding the algorithm to implement this is left as an exercise to the reader ;)