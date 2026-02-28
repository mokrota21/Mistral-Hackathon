###### Example 3.5.2 (Random slips of paper).

There are 100 slips of paper in a hat, each of which has one of the numbers $1,2,\ldots,100$ written on it, with no number appearing more than once. Five of the slips are drawn, one at a time.

First consider random sampling with replacement (with equal probabilities).

(a) What is the distribution of how many of the drawn slips have a value of at least 80 written on them?

(b) What is the distribution of the value of the $j$th draw (for $1\leq j\leq 5)$?

(c) What is the probability that the number 100 is drawn at least once?

Now consider random sampling without replacement (with all sets of five slips equally likely to be chosen).

(d) What is the distribution of how many of the drawn slips have a value of at least 80 written on them?

(e) What is the distribution of the value of the $j$th draw (for $1\leq j\leq 5)$?

(f) What is the probability that the number 100 is drawn in the sample?

Solution:

(a) By the story of the Binomial, the distribution is $\mathrm{Bin}(5,0.21)$.

(b) Let $X_{j}$ be the value of the $j$th draw. By symmetry, $X_{j}\sim\mathrm{DUnif}(1,2,\ldots,100)$. There aren’t certain slips that love being chosen on the $j$th draw and others that avoid being chosen then; all are equally likely.

(c) Taking complements,

$P(X_{j}=100\ \mathrm{for\ at\ least\ one\ }j)=1-P(X_{1}\neq 100,\ldots,X_{5}\neq 100).$

By the naive definition of probability, this is

$1-(99/100)^{5}\approx 0.049.$

This solution just uses new notation for concepts from Chapter 1. It is useful to have this new notation since it is compact and flexible. In the above calculation, it is important to see why

$P(X_{1}\neq 100,\ldots,X_{5}\neq 100)=P(X_{1}\neq 100)\ldots P(X_{5}\neq 100).$

This follows from the naive definition in this case, but a more general way to think about such statements is through independence of r.v.s, a concept discussed in detail in Section 3.8.

(d) By the story of the Hypergeometric, the distribution is $\mathrm{HGeom}(21,79,5)$.

(e) Let $Y_{j}$ be the value of the $j$th draw. By symmetry, $Y_{j}\sim\mathrm{DUnif}(1,2,\ldots,100)$.