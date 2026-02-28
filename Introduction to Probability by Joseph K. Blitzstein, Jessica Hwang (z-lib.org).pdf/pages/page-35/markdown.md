$A$: Instead of counting the number of ways to obtain at least one 6, it is easier to count the number of ways to get no 6’s. Getting no 6’s is equivalent to sampling the numbers 1 through 5 with replacement 6 times, so $5^{6}$ outcomes are favorable to $A^{c}$ (and $6^{6}-5^{6}$ are favorable to $A$). Thus

$P(A)=1-\frac{5^{6}}{6^{6}}\approx 0.67.$

$B$: Again we count the outcomes in $B^{c}$ first. There are $5^{12}$ ways to get no 6’s in 12 die rolls. There are $\binom{12}{1}5^{11}$ ways to get exactly one 6: we first choose which die lands 6, then sample the numbers 1 through 5 with replacement for the other 11 dice. Adding these, we get the number of ways to fail to obtain at least two 6’s. Then

$P(B)=1-\frac{5^{12}+\binom{12}{1}5^{11}}{6^{12}}\approx 0.62.$

$C$: We count the outcomes in $C^{c}$, i.e., the number of ways to get zero, one, or two 6’s in 18 die rolls. There are $5^{18}$ ways to get no 6’s, $\binom{18}{1}5^{17}$ ways to get exactly one 6, and $\binom{18}{2}5^{16}$ ways to get exactly two 6’s (choose which two dice will land 6, then decide how the other 16 dice will land).

$P(C)=1-\frac{5^{18}+\binom{18}{1}5^{17}+\binom{18}{2}5^{16}}{6^{18}}\approx 0.60.$

Therefore $A$ has the highest probability.

Newton arrived at the correct answer using similar calculations. Newton also provided Pepys with an intuitive argument for why $A$ was the most likely of the three; however, his intuition was invalid. As explained in Stigler *[24]*, using loaded dice could result in a different ordering of $A,B,C$, but Newton’s intuitive argument did not depend on the dice being fair. ∎

In this book, we care about counting not for its own sake, but because it sometimes helps us to find probabilities. Here is an example of a neat but treacherous counting problem; the solution is elegant, but it is rare that the result can be used with the naive definition of probability.

###### Example 1.4.22 (Bose-Einstein).

How many ways are there to choose $k$ times from a set of $n$ objects with replacement, if order doesn’t matter (we only care about how many times each object was chosen, not the order in which they were chosen)?

Solution:

When order does matter, the answer is $n^{k}$ by the multiplication rule, but this problem is much harder. We will solve it by solving an *isomorphic* problem (the same problem in a different guise).

Let us find the number of ways to put $k$ indistinguishable particles into $n$ distinguishable boxes. That is, swapping the particles in any way is not considered a separate