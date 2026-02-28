will discuss a strategy known as *first-step analysis*, which often allows us to obtain recursive solutions to problems where the experiment has multiple stages.

Due to the central importance of conditioning, both as the means by which we update beliefs to reflect evidence and as a problem-solving strategy, we say that

*Conditioning is the soul of statistics.*

### 2.2 Definition and intuition

###### Definition 2.2.1 (Conditional probability).

If $A$ and $B$ are events with $P(B)>0$, then the *conditional probability* of $A$ given $B$, denoted by $P(A|B)$, is defined as

$P(A|B)=\frac{P(A\cap B)}{P(B)}.$

Here $A$ is the event whose uncertainty we want to update, and $B$ is the evidence we observe (or want to treat as given). We call $P(A)$ the *prior* probability of $A$ and $P(A|B)$ the *posterior* probability of $A$ (“prior” means before updating based on the evidence, and “posterior” means after updating based on the evidence).

It is important to interpret the event appearing after the vertical conditioning bar as the evidence that we have observed or that is being conditioned on: $P(A|B)$ is the probability of $A$ given the evidence $B$, *not* the probability of some entity called $A|B$. As discussed in 2.4.1, there is no such event as $A|B$.

For any event $A$, $P(A|A)=P(A\cap A)/P(A)=1$. Upon observing that $A$ has occurred, our updated probability for $A$ is $1$. If this weren’t the case, we would demand a new definition of conditional probability!

###### Example 2.2.2 (Two cards).

A standard deck of cards is shuffled well. Two cards are drawn randomly, one at a time without replacement. Let $A$ be the event that the first card is a heart, and $B$ be the event that the second card is red. Find $P(A|B)$ and $P(B|A)$.

*Solution*:

By the naive definition of probability and the multiplication rule,

$P(A\cap B)=\frac{13\cdot 25}{52\cdot 51}=\frac{25}{204},$

since a favorable outcome is determined by choosing any of the 13 hearts and then any of the remaining 25 red cards. Also, $P(A)=1/4$ since the 4 suits are equally likely, and

$P(B)=\frac{26\cdot 51}{52\cdot 51}=\frac{1}{2}$