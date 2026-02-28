Introduction to Probability

- the prosecutor’s fallacy, confusing $P(A|B)$ with $P(B|A)$;
- the defense attorney’s fallacy, failing to condition on all the evidence;
- unawareness of Simpson’s paradox and the importance of thinking carefully about whether to aggregate data.

Figure 2.7 illustrates how probabilities can be updated as new evidence comes in sequentially. Imagine that there is some event $A$ that we are interested in. On Monday morning, for example, our prior probability for $A$ is $P(A)$. If we observe on Monday afternoon that $B$ occurred, then we can use Bayes’ rule (or the definition of conditional probability) to compute the posterior probability $P(A|B)$.

We use this posterior probability for $A$ as the new prior on Tuesday morning, and then we continue to collect evidence. Suppose that on Tuesday we observe that $C$ occurred. Then we can compute the new posterior probability $P(A|B,C)$ in various ways (in this context, probably the most natural way is to use Bayes’ rule with extra conditioning on $B$). This in turn becomes the new prior if we are going to continue to collect evidence.

## 2.10 R

### Simulating the frequentist interpretation

Recall that the frequentist interpretation of conditional probability based on a large number $n$ of repetitions of an experiment is $P(A|B) \approx n_{AB} / n_B$, where $n_{AB}$ is the number of times that $A \cap B$ occurs and $n_B$ is the number of times that $B$ occurs. Let’s try this out by simulation, and verify the results of Example 2.2.5. So let’s simulate $n$ families, each with two children.

```
n &lt;- 10^5
child1 &lt;- sample(2,n,replace=TRUE)
child2 &lt;- sample(2,n,replace=TRUE)
```

Here `child1` is a vector of length $n$, where each element is a 1 or a 2. Letting 1 stand for “girl” and 2 stand for “boy”, this vector represents the gender of the elder child in each of the $n$ families. Similarly, `child2` represents the gender of the younger child in each family.

Alternatively, we could have used

```
sample(c("girl","boy"),n,replace=TRUE)
```

but it is more convenient working with numerical values.

Let $A$ be the event that both children are girls and $B$ the event that the elder is a girl.