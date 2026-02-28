Conditional probability

- *Health effects of smoking*: Cochran *[4]* found that within any age group, cigarette smokers had higher mortality rates than cigar smokers, but because cigarette smokers were on average younger than cigar smokers, overall mortality rates were lower for cigarette smokers. ∎

### 2.9 Recap

The conditional probability of $A$ given $B$ is

$P(A|B)=\frac{P(A\cap B)}{P(B)}.$

Conditional probability has exactly the same properties as probability, but $P(\cdot|B)$ updates our uncertainty about events to reflect the observed evidence $B$. Events whose probabilities are unchanged after observing the evidence $B$ are said to be independent of $B$. Two events can also be conditionally independent given a third event $E$. Conditional independence does not imply unconditional independence, nor does unconditional independence imply conditional independence.

Two important results about conditional probability are Bayes’ rule, which relates $P(A|B)$ to $P(B|A)$, and the law of total probability, which allows us to get unconditional probabilities by partitioning the sample space and calculating conditional probabilities within each slice of the partition.

Bayes’ rule says that

$P(A|B)=\frac{P(B|A)P(A)}{P(B)},$

while LOTP says that

$P(B)=\sum_{i=1}^{n}P(B|A_{i})P(A_{i}),$

for any partition $A_{1},\ldots,A_{n}$ of the sample space. Bayes’ rule and LOTP are often used in tandem.

Conditioning is extremely helpful for problem-solving because it allows us to break a problem into smaller pieces, consider all possible cases separately, and then combine them. When using this strategy, we should try to condition on the information that, if known, would make the problem simpler, hence the saying *condition on what you wish you knew*. When a problem involves multiple stages, it can be helpful to *condition on the first step* to obtain a recursive relationship.

Common mistakes in thinking conditionally include:

- confusion of the prior probability $P(A)$ with the posterior probability $P(A|B)$;