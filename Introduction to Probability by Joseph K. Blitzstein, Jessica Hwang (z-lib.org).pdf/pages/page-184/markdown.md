$J_{i}$ is the indicator of the $i$th pair of people having the same birthday. We create an indicator for each *pair of people* since $Y$ counts the number of *pairs of people* with the same birthday. The probability of any two people having the same birthday is $1/365$, so again by the fundamental bridge and linearity,

$E(Y)=\frac{\binom{n}{2}}{365}.\qed$

In addition to the fundamental bridge and linearity, the last two examples used a basic form of symmetry to simplify the calculations greatly: within each sum of indicator r.v.s, each indicator had the same expected value. For example, in the matching problem the probability of the $j$th card being a match does not depend on $j$, so we can just take $n$ times the expected value of the first indicator r.v.

Other forms of symmetry can also be extremely helpful when available. The next two examples showcase a form of symmetry that stems from having equally likely permutations. Note how symmetry, linearity, and the fundamental bridge are used in tandem to make seemingly very hard problems manageable.

###### Example 4.4.6 (Putnam problem).

A permutation $a_{1},a_{2},\ldots,a_{n}$ of $1,2,\ldots,n$ has a *local maximum* at $j$ if $a_{j}>a_{j-1}$ and $a_{j}>a_{j+1}$ (for $2\leq j\leq n-1$; for $j=1$, a local maximum at $j$ means $a_{1}>a_{2}$ while for $j=n$, it means $a_{n}>a_{n-1}$). For example, $4,2,5,3,6,1$ has $3$ local maxima, at positions $1$, $3$, and $5$. The Putnam exam (a famous, hard math competition, on which the median score is often a $0$) from 2006 posed the following question: for $n\geq 2$, what is the average number of local maxima of a random permutation of $1,2,\ldots,n$, with all $n!$ permutations equally likely?

*Solution*:

This problem can be solved quickly using indicator r.v.s, symmetry, and the fundamental bridge. Let $I_{1},\ldots,I_{n}$ be indicator r.v.s, where $I_{j}$ is $1$ if there is a local maximum at position $j$, and $0$ otherwise. We are interested in the expected value of $\sum_{j=1}^{n}I_{j}$. For $1<j<n$, $EI_{j}=1/3$ since having a local maximum at $j$ is equivalent to $a_{j}$ being the largest of $a_{j-1},a_{j},a_{j+1}$, which has probability $1/3$ since all orders are equally likely. For $j=1$ or $j=n$, we have $EI_{j}=1/2$ since then there is only one neighbor. Thus, by linearity,

$E\left(\sum_{j=1}^{n}I_{j}\right)=2\cdot\frac{1}{2}+(n-2)\cdot\frac{1}{3}=\frac{n+1}{3}.\qed$

The next example introduces the *Negative Hypergeometric* distribution, which completes the following table. The table shows the distributions for four sampling schemes: the sampling can be done with or without replacement, and the stopping rule can require a fixed number of draws or a fixed number of successes.