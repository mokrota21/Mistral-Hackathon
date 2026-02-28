for any nonnegative integer $n$. To prove the binomial theorem, expand out the product

$\underbrace{(x+y)(x+y)\ldots(x+y)}_{n\ \text{factors}}.$

Just as $(a+b)(c+d)=ac+ad+bc+bd$ is the sum of terms where we pick the $a$ or the $b$ from the first factor (but not both) and the $c$ or the $d$ from the second factor (but not both), the terms of $(x+y)^{n}$ are obtained by picking either the $x$ or the $y$ (but not both) from each factor. There are $\binom{n}{k}$ ways to choose exactly $k$ of the $x$’s, and each such choice yields the term $x^{k}y^{n-k}$. The binomial theorem follows. ∎

We can use binomial coefficients to calculate probabilities in many problems for which the naive definition applies.

###### Example 1.4.20 (Full house in poker).

A 5-card hand is dealt from a standard, well-shuffled 52-card deck. The hand is called a *full house* in poker if it consists of three cards of some rank and two cards of another rank, e.g., three 7’s and two 10’s (in any order). What is the probability of a full house?

*Solution*:

All of the $\binom{52}{5}$ possible hands are equally likely by symmetry, so the naive definition is applicable. To find the number of full house hands, use the multiplication rule (and imagine the tree). There are 13 choices for what rank we have three of; for concreteness, assume we have three 7’s and focus on that branch of the tree. There are $\binom{4}{3}$ ways to choose which 7’s we have. Then there are 12 choices for what rank we have two of, say 10’s for concreteness, and $\binom{4}{2}$ ways to choose two 10’s. Thus,

$P(\text{full house})=\frac{13\binom{4}{3}12\binom{4}{2}}{\binom{52}{5}}=\frac{3744}{2598960}\approx 0.00144.$

The decimal approximation is more useful when playing poker, but the answer in terms of binomial coefficients is exact and *self-annotating* (seeing $\binom{52}{5}$ is a much bigger hint about its origin than seeing 2598960). ∎

###### Example 1.4.21 (Newton-Pepys problem).

Isaac Newton was consulted about the following problem by Samuel Pepys, who wanted the information for gambling purposes. Which of the following events has the highest probability?

$A$: At least one 6 appears when 6 fair dice are rolled.

$B$: At least two 6’s appear when 12 fair dice are rolled.

$C$: At least three 6’s appear when 18 fair dice are rolled.

*Solution*:

The three experiments have $6^{6}$, $6^{12}$, and $6^{18}$ possible outcomes, respectively, and by symmetry the naive definition applies in all three experiments.