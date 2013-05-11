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

A more mathematical approach, we can prove by induction that at the end of each day **d** we achieve the largest amount of euros **(euros = E[d], bitcoins = 0)** and the largest amount of bitcoins **(euros = e[d], bitcoins = B[d])** - *breaking ties by largest amount of euros when there are two situations with the same amount of bitcoins* - by selling all of the bitcoins we have or buying all the bitcoins we can at each previous day:

* Base case: at the end of "day 0", we know the situation with maximum amount of euros **(N, 0)** and the maximum amount of bitcoins **(N, 0)**

* Induction step:

1. Assume at the end of day **i** we know the situations with the largest amount of euros **(E[i], 0)** and the largest amount of bitcoins **(e[i], B[i])**.

2. At the end of day **i** there is another situation **(m[i], b[i])**, which by definition has **m[i] < E[i]** and either **b[i] < B[i]** or **b[i] == B[i] and m[i] < e[i]**. The proof by contradiction shows that regardless of the values of **m[i]** and **b[i]**, it may not achieve a largest amount of bitcoins or euros at the end of day **i+1** than **(E[i], 0)** and **(e[i], B[i])**.

2.1. Assume **(m[i], b[i])** can achieve the largest amount of euros at the end of day **i+1**. This means (with bitcoin price of **p[i+1]** on day **i+1**): 

```
(1) b[i] * p[i+1] + m[i] > B[i] * p[i+1] + e[i]     
    
(2) b[i] * p[i+1] + m[i] > E[i]
```
    
* If **p[i] > p[i+1]**, we could have sold all our bitcoins on day **i** to get **b[i] * p[i] + m[i] > b[i] * p[i+1] + m[i] > E[i]** (the second inequality is equation (2)). This contradicts our original hypothesis that **E[i]** was the largest amount of euros we could have achieved at the end of day **i**.

* If **p[i+1] >= p[i]**, we could have bought more bitcoins on day **i** to get **b[i] + floor(m[i] / p[i])** bitcoins and be left with **e[i]%p[i]** euros. Equation (1) above implies (because **0 <= b[i] <= B[i]** and **0 <= p[i] <= p[i+1]**) that:

```
(3) b[i] * p[i] + m[i] > B[i] * p[i] + e[i] < = > B[i] < b[i] + m[i] / p[i] - e[i] / p[i]
```
       
Since, **e[i] / p[i] < 1** (or we would have bought more bitcoins on day **i** and B[i] wouldn't be the largest amount of bitcoins), there are two possible situations:

* **m[i] / p[i] < 1**. Using (3), this means **b[i] == B[i]** and **m[i] > e[i]**, which contradict our hypothesis that **B[i]** was the largest amount of bitcoins breaking ties by the amount of euros **e[i]** that could be achieved at the end of day **i**

* **m[i] / p[i] >= 1**. In this case (3) implies that **b[i] + floor(m[i] / p[i]) > B[i]**, which contradicts our hypothesis that **B[i]** was the largest amount of bitcoins we could have achieved at the end of day **i**.

This serves to prove that no other situation **(m[i], b[i])** can achieve a larger amount of euros at the end of day **i+1**.

2.2. Assume **(m[i], b[i])** can achieve the largest amount of bitcoins at the end of day **i+1**. The approach to prove that this is impossible is quite similar to the one presented above and is left as an exercise to the reader =)

(2.1) and (2.2) taken together show that there is no situation besides **(E[i], 0)** and **(e[i], B[i])** that could achieve a larger amount of bitcoins or euros at then end of day **i+1** thus completing the induction step and the proof.