This problem can be solved using simple DP (dynamic programming).

The insight needed to solve the problem is that in each day we should either sell all our bitcoins or buy the maximum amount of bitcoins we can.

Suppose that in the optimal solution at some day **i**, we have **B** bitcoins and we must sell **b < B** bitcoins. The only reason to hold on to bitcoins is if we can sell them for profit later at day **j**. On the other hand, we are selling some of them now which must mean we "need" the money. The only explanation for needing the money is that we want to buy bitcoins at a low price before day **j**. It is easy to see that these two goals are in contradiction. If there is some day when we can get bitcoins at a better price, we should sell all our bitcoins before that so that we can spend the largest amount of money on the bitcoins then. 

This means that, at each day we should consider two cases:
1. Sell all the bitcoins we have
2. Buy all the bitcoins we can

We should then keep track of:
1. The largest amount of money we can have at any day (this is our ultimate goal)
2. The largest number of bitcoins we can have at any day (in case an awesome deal appears and we sell them for a huge profit)

This takes into account every possible optimal case (if the "best deal" is to buy coins at a price of 2 on day 6, we will use the largest amount of money we could get until day 5 to buy all of them).