an infinite sample space. To generalize the notion of probability, we’ll write down a short wish list of how we want probability to behave (in math, the items on the wish list are called *axioms*), and then define a probability function to be something that satisfies the properties we want!

Here is the general definition of probability that we’ll use for the rest of this book. It requires just two axioms, but from these axioms it is possible to prove a vast array of results about probability.

###### Definition 1.6.1 (General definition of probability).

A *probability space* consists of a sample space $S$ and a *probability function* $P$ which takes an event $A\subseteq S$ as input and returns $P(A)$, a real number between $0$ and $1$, as output. The function $P$ must satisfy the following axioms:

1. $P(\emptyset)=0$, $P(S)=1$.
2. If $A_{1},A_{2},\dots$ are disjoint events, then

$P\left(\bigcup_{j=1}^{\infty}A_{j}\right)=\sum_{j=1}^{\infty}P(A_{j}).$

(Saying that these events are *disjoint* means that they are *mutually exclusive*: $A_{i}\cap A_{j}=\emptyset$ for $i\neq j$.)

In Pebble World, the definition says that probability behaves like mass: the mass of an empty pile of pebbles is $0$, the total mass of all the pebbles is $1$, and if we have non-overlapping piles of pebbles, we can get their combined mass by adding the masses of the individual piles. Unlike in the naive case, we can now have pebbles of differing masses, and we can also have a countably infinite number of pebbles as long as their total mass is $1$.

We can even have uncountable sample spaces, such as having $S$ be an area in the plane. In this case, instead of pebbles, we can visualize mud spread out over a region, where the total mass of the mud is $1$.

Any function $P$ (mapping events to numbers in the interval $[0,1]$) that satisfies the two axioms is considered a valid probability function. However, the axioms don’t tell us how probability should be *interpreted*; different schools of thought exist.

The *frequentist* view of probability is that it represents a long-run frequency over a large number of repetitions of an experiment: if we say a coin has probability $1/2$ of Heads, that means the coin would land Heads $50\%$ of the time if we tossed it over and over and over.

The *Bayesian* view of probability is that it represents a degree of belief about the event in question, so we can assign probabilities to hypotheses like “candidate A will win the election” or “the defendant is guilty” even if it isn’t possible to repeat the same election or the same crime over and over again.