By taking the Bayes’ rule expression for $P(A|B)$ and dividing it by the Bayes’ rule expression for $P(A^{c}|B)$, we arrive at the odds form of Bayes’ rule.

###### Theorem 2.3.5 (Odds form of Bayes’ rule).

For any events $A$ and $B$ with positive probabilities, the odds of $A$ after conditioning on $B$ are

$\frac{P(A|B)}{P(A^{c}|B)}=\frac{P(B|A)}{P(B|A^{c})}\frac{P(A)}{P(A^{c})}.$

In words, this says that the *posterior odds* $P(A|B)/P(A^{c}|B)$ are equal to the *prior odds* $P(A)/P(A^{c})$ times the factor $P(B|A)/P(B|A^{c})$, which is known in statistics as the *likelihood ratio*. Sometimes it is convenient to work with this form of Bayes’ rule to get the posterior odds, and then if desired we can convert from odds back to probability.

The *law of total probability* (LOTP) relates conditional probability to unconditional probability. It is essential for fulfilling the promise that conditional probability can be used to decompose complicated probability problems into simpler pieces, and it is often used in tandem with Bayes’ rule.

###### Theorem 2.3.6 (Law of total probability).

Let $A_{1},\ldots,A_{n}$ be a partition of the sample space $S$ (i.e., the $A_{i}$ are disjoint events and their union is $S$), with $P(A_{i})>0$ for all $i$. Then

$P(B)=\sum_{i=1}^{n}P(B|A_{i})P(A_{i}).$

###### Proof.

Since the $A_{i}$ form a partition of $S$, we can decompose $B$ as

$B=(B\cap A_{1})\cup(B\cap A_{2})\cup\cdots\cup(B\cap A_{n}).$

This is illustrated in Figure 2.3, where we have chopped $B$ into the smaller pieces $B\cap A_{1}$ through $B\cap A_{n}$. By the second axiom of probability, because these pieces are disjoint, we can add their probabilities to get $P(B)$:

$P(B)=P(B\cap A_{1})+P(B\cap A_{2})+\cdots+P(B\cap A_{n}).$

Now we can apply Theorem 2.3.1 to each of the $P(B\cap A_{i})$:

$P(B)=P(B|A_{1})P(A_{1})+\cdots+P(B|A_{n})P(A_{n}).\qed$

The law of total probability tells us that to get the unconditional probability of $B$, we can divide the sample space into disjoint slices $A_{i}$, find the conditional probability of $B$ within each of the slices, then take a weighted sum of the conditional probabilities, where the weights are the probabilities $P(A_{i})$. The choice of how to divide up the sample space is crucial: a well-chosen partition will reduce a complicated problem into simpler pieces, whereas a poorly chosen partition will only exacerbate our problems, requiring us to calculate $n$ difficult probabilities instead of just one!

The next few examples show how we can use Bayes’ rule together with the law of total probability to update our beliefs based on observed evidence.