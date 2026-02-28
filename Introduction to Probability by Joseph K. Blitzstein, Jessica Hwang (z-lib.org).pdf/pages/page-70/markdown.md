possible to find conditional probabilities without going back to the definition, and in such cases Theorem 2.3.1 can help us more easily find $P(A\cap B)$.

Applying Theorem 2.3.1 repeatedly, we can generalize to the intersection of $n$ events.

###### Theorem 2.3.2 (Probability of the intersection of $n$ events).

For any events $A_{1},\ldots,A_{n}$ with $P(A_{1},A_{2},\ldots,A_{n-1})>0$,

$P(A_{1},A_{2},\ldots,A_{n})=P(A_{1})P(A_{2}|A_{1})P(A_{3}|A_{1},A_{2})\cdots P(A_{n}|A_{1},\ldots,A_{n-1}),$

The commas denote intersections, e.g., $P(A_{3}|A_{1},A_{2})$ is $P(A_{3}|A_{1}\cap A_{2})$.

In fact, this is $n!$ theorems in one, since we can permute $A_{1},\ldots,A_{n}$ however we want without affecting the left-hand side. Often the right-hand side will be much easier to compute for some orderings than for others. For example,

$P(A_{1},A_{2},A_{3})=P(A_{1})P(A_{2}|A_{1})P(A_{3}|A_{1},A_{2})=P(A_{2})P(A_{3}|A_{2})P(A_{1}|A_{2},A_{3}),$

and there are 4 other expansions of this form too. It often takes practice and thought to be able to know which ordering to use.

We are now ready to introduce the two main theorems of this chapter—Bayes’ rule and the law of total probability—which will allow us to compute conditional probabilities in a wide range of problems. Bayes’ rule is an extremely famous, extremely useful result that relates $P(A|B)$ to $P(B|A)$.

###### Theorem 2.3.3 (Bayes’ rule).

$P(A|B)=\frac{P(B|A)P(A)}{P(B)}.$

This follows immediately from Theorem 2.3.1, which in turn followed immediately from the definition of conditional probability. Yet Bayes’ rule has important implications and applications in probability and statistics, since it is so often necessary to find conditional probabilities, and often $P(B|A)$ is much easier to find directly than $P(A|B)$ (or vice versa).

Another way to write Bayes’ rule is in terms of *odds* rather than probability.

###### Definition 2.3.4 (Odds).

The *odds* of an event $A$ are

$\text{odds}(A)=P(A)/P(A^{c}).$

For example, if $P(A)=2/3$, we say the odds in favor of $A$ are 2 to 1. (This is sometimes written as $2:1$, and is sometimes stated as 1 to 2 odds against $A$; care is needed since some sources do not explicitly state whether they are referring to odds in favor or odds against an event.) Of course we can also convert from odds back to probability:

$P(A)=\text{odds}(A)/(1+\text{odds}(A)).$