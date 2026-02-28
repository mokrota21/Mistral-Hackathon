Introduction to Probability

of rain today, $P(R)$, on the fraction of days in the past on which it rained. But which days in the past should we look at? If it’s November 1, should we only count past rainy days in autumn, thus conditioning on the season? What about conditioning on the exact month, or the exact day? We could ask the same about location: should we look at days when it rained in our exact location, or is it enough for it to have rained somewhere nearby?

In order to determine the seemingly unconditional probability $P(R)$, we actually have to make decisions about what background information to condition on! These choices require careful thought and different people may come up with different prior probabilities $P(R)$ (though everyone can agree on how to update based on new evidence).

Since all probabilities are conditional on background information, we can imagine that there is always a vertical conditioning bar, with background knowledge $K$ to the right of the vertical bar. Then the unconditional probability $P(A)$ is just shorthand for $P(A|K)$; the background knowledge is absorbed into the letter $P$ instead of being written explicitly.

To summarize our discussion in a nutshell:

Conditional probabilities are probabilities, and all probabilities are conditional.

We now state conditional forms of Bayes’ rule and the law of total probability. These are obtained by taking the ordinary forms of Bayes’ rule and LOTP and adding $E$ to the right of the vertical bar everywhere.

###### Theorem 2.4.2 (Bayes’ rule with extra conditioning).

Provided that $P(A\cap E)&gt;0$ and $P(B\cap E)&gt;0$, we have

$P(A|B,E)=\frac{P(B|A,E)P(A|E)}{P(B|E)}.$

###### Theorem 2.4.3 (LOTP with extra conditioning).

Let $A_{1},\ldots,A_{n}$ be a partition of $S$. Provided that $P(A_{i}\cap E)&gt;0$ for all $i$, we have

$P(B|E)=\sum_{i=1}^{n}P(B|A_{i},E)P(A_{i}|E).$

The extra conditioning forms of Bayes’ rule and LOTP can be proved similarly to how we verified that $\hat{P}$ satisfies the axioms of probability, but they also follow directly from the “metatheorem” that conditional probabilities are probabilities.

###### Example 2.4.4 (Random coin, continued).

Continuing with the scenario from Example 2.3.7, suppose that we have now seen our chosen coin land Heads three times. If we toss the coin a fourth time, what is the probability that it will land Heads once more?