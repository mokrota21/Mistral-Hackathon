Pebble World can help us visualize sample spaces and events when the sample space is finite. In Pebble World, each outcome is a pebble, and an event is a set of pebbles. If all the pebbles have the same mass (i.e., are equally likely), we can apply the naive definition of probability, which lets us calculate probabilities by counting.

To this end, we discussed several tools for counting. When counting the number of possibilities, we often use the multiplication rule. For example, there are $n!$ permutations of the numbers $1,2,\ldots,n$ and there are $2^{n}$ subsets of a set with $n$ elements. If we can’t directly use the multiplication rule, we can sometimes count each possibility exactly $c$ times for some $c$, and then divide by $c$ to get the actual number of possibilities. For example, this strategy is useful for finding an expression for binomial coefficients in terms of factorials.

An important pitfall to avoid is misapplying the naive definition of probability, implicitly or explicitly assuming equally likely outcomes without justification. One technique to help avoid this is to give objects labels, for precision and so that we are not tempted to treat them as indistinguishable.

Moving beyond the naive definition, we define probability to be a function that takes an event and assigns to it a real number between $0$ and $1$. We require a valid probability function to satisfy two axioms:

1. $P(\emptyset)=0$, $P(S)=1$.

2. If $A_{1},A_{2},\ldots$ are disjoint events, then

$P\left(\bigcup_{j=1}^{\infty}A_{j}\right)=\sum_{j=1}^{\infty}P(A_{j}).$

Many useful properties can be derived from these axioms. For example,

$P(A^{c})=1-P(A)$

for any event $A$, and we have the inclusion-exclusion formula

\[ P\left(\bigcup_{i=1}^{n}A_{i}\right)=\sum_{i}P(A_{i})-\sum_{i<j}P(A_{i}\cap A_{j})+\sum_{i<j<k}P(A_{i}\cap A_{j}\cap A_{k})-\ldots\\
+(-1)^{n+1}P(A_{1}\cap\cdots\cap A_{n}) \]

for any events $A_{1},\ldots,A_{n}$. For $n=2$, this is the much nicer-looking result

$P(A_{1}\cup A_{2})=P(A_{1})+P(A_{2})-P(A_{1}\cap A_{2}).$

Figure 7 illustrates how a probability function maps events to numbers between $0$ and $1$. We’ll add many new concepts to this diagram as we continue our journey through the field of probability.