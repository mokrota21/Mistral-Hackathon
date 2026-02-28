Problems 26 and 27 show that the birthday problem is much more than a fun party game, and much more than a way to build intuition about coincidences; there are also important applications in statistics and computer science. Problem 62 explores the more general setting in which the probability is not necessarily $1/365$ for each day. It turns out that in the non-equal probability case, having at least one match becomes even *more* likely. ∎

#### 1.4.11 (Labeling objects).

Drawing a sample from a population is a very fundamental concept in statistics. It is important to think of the objects or people in the population as *named* or *labeled*. For example, if there are $n$ balls in a jar, we can imagine that they have labels from $1$ to $n$, even if the balls look the same to the human eye. In the birthday problem, we can give each person an ID (identification) number, rather than thinking of the people as indistinguishable particles or a faceless mob.

A related example is an instructive blunder made by Leibniz in a seemingly simple problem (see Gorroochurn *[14]* for discussion of this and a variety of other probability problems from a historical perspective).

###### Example 1.4.12 (Leibniz’s mistake).

If we roll two fair dice, which is more likely: a sum of $11$ or a sum of $12$?

*Solution*:

Label the dice A and B, and consider each die to be a sub-experiment. By the multiplication rule, there are $36$ possible outcomes for ordered pairs of the form (value of A, value of B), and they are equally likely by symmetry. Of these, $(5,6)$ and $(6,5)$ are favorable to a sum of $11$, while only $(6,6)$ is favorable to a sum of $12$. Therefore a sum of $11$ is twice as likely as a sum of $12$; the probability is $1/18$ for the former, and $1/36$ for the latter.

However, Leibniz wrongly argued that a sum of $11$ and a sum of $12$ are equally likely, claiming that each of these sums can be attained in only one way. Here Leibniz was making the mistake of treating the two dice as indistinguishable objects, viewing $(5,6)$ and $(6,5)$ as the same outcome.

What are the antidotes to Leibniz’s mistake? First, as explained in 1.4.11, we should *label* the objects in question instead of treating them as indistinguishable. If Leibniz had labeled his dice A and B, or green and orange, or left and right, he would not have made this mistake. Second, before we use counting for probability, we should ask ourselves whether the naive definition applies (see 1.4.23 for another example showing that caution is needed before applying the naive definition). ∎

#### 1.4.2 Adjusting for overcounting

In many counting problems, it is not easy to directly count each possibility once and only once. If, however, we are able to count each possibility exactly $c$ times