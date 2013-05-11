Since the trivial implementation of the Turing machine is incredibly slow for some inputs, another way is needed.

Understanding the Turing machine (or finding an automatic way to simplify the algorithm and implement it in an efficient way) is not very easy, we are left with looking at sample inputs and outputs (generated with the naive turing machine implementation - prob.py) to find a pattern. It turns out that the eligible strings are of the form:

    #binary#binary#binary#...#

And the output is always first binary integer * (sum of binary integers from second to the last).

After getting this, the problem is easily solved with prob16.py