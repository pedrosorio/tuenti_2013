At the beginning of turn **T**, **W*T** invaders have appeared. If we have **N** soldiers, **N*(T-1)** invaders have been killed.

There is an invasion on turn **T** if **W*T - N*(T-1) > W*H**, i.e. there is an invasion on the smallest **T > (W*H - N) / (W - N)**.

Knowing the number of soldiers, we know how much gold was spent on them and how many times it is possible to use the crematorium. 

If we can use the crematorium **NC** times, we can survive for **NC * (W*H - N) / (W - N)** turns.

Simply iterating over the number of soldiers (until we have no more gold) allows to compute the largest number of turns. If we have enough gold to pay more than W soliders, we can survive indefinitely. 

In order to make this more optimized, when the price of using the crematorium is larger than that of a soldier (specially if it is much larger), it is sensible to iterate on the number of times the crematorium is used (much smaller) and find the maximum number of soldiers that can be bought with the remaining money.