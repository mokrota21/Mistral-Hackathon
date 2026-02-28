###### Theorem 1.6.3 (Inclusion-exclusion).

For any events $A_{1},\ldots,A_{n}$,

\[ P\left(\bigcup_{i=1}^{n}A_{i}\right)=\sum_{i}P(A_{i})-\sum_{i<j}P(A_{i}\cap A_{j})+\sum_{i<j<k}P(A_{i}\cap A_{j}\cap A_{k})-\ldots\\
+(-1)^{n+1}P(A_{1}\cap\cdots\cap A_{n}). \]

This formula can be proven by induction using just the axioms, but instead we’ll present a shorter proof in Chapter 4 after introducing some additional tools. The rationale behind the alternating addition and subtraction in the general formula is analogous to the special cases we’ve already considered.

The next example, de Montmort’s matching problem, is a famous application of inclusion-exclusion. Pierre Rémond de Montmort was a French mathematician who studied probability in the context of gambling and wrote a treatise *[19]* devoted to the analysis of various card games. He posed the following problem in 1708, based on a card game called Treize.

###### Example 1.6.4 (de Montmort’s matching problem).

Consider a well-shuffled deck of $n$ cards, labeled $1$ through $n$. You flip over the cards one by one, saying the numbers $1$ through $n$ as you do so. You win the game if, at some point, the number you say aloud is the same as the number on the card being flipped over (for example, if the $7$th card in the deck has the label $7$). What is the probability of winning?

*Solution*:

Let $A_{i}$ be the event that the $i$th card in the deck has the number $i$ written on it. We are interested in the probability of the union $A_{1}\cup\cdots\cup A_{n}$: as long as at least one of the cards has a number matching its position in the deck, you will win the game. (An ordering for which you lose is called a *derangement*, though hopefully no one has ever become deranged due to losing at this game.)

To find the probability of the union, we’ll use inclusion-exclusion. First,

$P(A_{i})=\frac{1}{n}$

for all $i$. One way to see this is with the naive definition of probability, using the full sample space: there are $n!$ possible orderings of the deck, all equally likely, and $(n-1)!$ of these are favorable to $A_{i}$ (fix the card numbered $i$ to be in the $i$th position in the deck, and then the remaining $n-1$ cards can be in any order). Another way to see this is by symmetry: the card numbered $i$ is equally likely to be in any of the $n$ positions in the deck, so it has probability $1/n$ of being in the $i$th spot. Second,

$P(A_{i}\cap A_{j})=\frac{(n-2)!}{n!}=\frac{1}{n(n-1)},$

since we require the cards numbered $i$ and $j$ to be in the $i$th and $j$th spots in the