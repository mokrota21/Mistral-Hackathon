(where order matters, in the sense that, e.g., choosing object 3 and then object 7 is counted as a different outcome than choosing object 7 and then object 3.)

For example, imagine a jar with $n$ balls, labeled from 1 to $n$. We sample balls one at a time with replacement, meaning that each time a ball is chosen, it is returned to the jar. Each sampled ball is a sub-experiment with $n$ possible outcomes, and there are $k$ sub-experiments. Thus, by the multiplication rule there are $n^{k}$ ways to obtain a sample of size $k$.

###### Theorem 1.4.8 (Sampling without replacement).

Consider $n$ objects and making $k$ choices from them, one at a time *without replacement* (i.e., choosing a certain object precludes it from being chosen again). Then there are $n(n-1)\cdots(n-k+1)$ possible outcomes for $1\leq k\leq n$, and $0$ possibilities for $k>n$ (where order matters). By convention, $n(n-1)\cdots(n-k+1)=n$ for $k=1$.

This result also follows directly from the multiplication rule: each sampled ball is again a sub-experiment, and the number of possible outcomes decreases by 1 each time. Note that for sampling $k$ out of $n$ objects without replacement, we need $k\leq n$, whereas in sampling with replacement the objects are inexhaustible.

###### Example 1.4.9 (Permutations and factorials).

A *permutation* of $1,2,\ldots,n$ is an arrangement of them in some order, e.g., $3,5,1,2,4$ is a permutation of $1,2,3,4,5$. By Theorem 1.4.8 with $k=n$, there are $n!$ permutations of $1,2,\ldots,n$. For example, there are $n!$ ways in which $n$ people can line up for ice cream. (Recall that $n!$ is $n(n-1)(n-2)\cdots 1$ for any positive integer $n$, and $0!=1$.) ∎

Theorems 1.4.7 and 1.4.8 are theorems about *counting*, but when the naive definition applies, we can use them to calculate *probabilities*. This brings us to our next example, a famous problem in probability called the *birthday problem*. The solution incorporates both sampling with replacement and sampling without replacement.

###### Example 1.4.10 (Birthday problem).

There are $k$ people in a room. Assume each person’s birthday is equally likely to be any of the 365 days of the year (we exclude February 29), and that people’s birthdays are independent (we will define *independence* formally later, but intuitively it means that knowing some people’s birthdays gives us no information about other people’s birthdays; this would not hold if, e.g., we knew that two of the people were twins). What is the probability that at least one pair of people in the group have the same birthday?

*Solution*:

There are $365^{k}$ ways to assign birthdays to the people in the room, since we can imagine the 365 days of the year being sampled $k$ times, with replacement. By assumption, all of these possibilities are equally likely, so the naive definition of probability applies.

Used directly, the naive definition says we just need to count the number of ways to assign birthdays to $k$ people such that there are two people who share a birthday.