###### Definition 2.5.6 (Independence of many events).

For $n$ events $A_{1},A_{2},\ldots,A_{n}$ to be *independent*, we require any pair to satisfy $P(A_{i}\cap A_{j})=P(A_{i})P(A_{j})$ (for $i\neq j$), any triplet to satisfy $P(A_{i}\cap A_{j}\cap A_{k})=P(A_{i})P(A_{j})P(A_{k})$ (for $i,j,k$ distinct), and similarly for all quadruplets, quintuplets, and so on. This can quickly become unwieldy, but later we will discuss other ways to think about independence. For infinitely many events, we say that they are independent if every finite subset of the events is independent.

Conditional independence is defined analogously to independence.

###### Definition 2.5.7 (Conditional independence).

Events $A$ and $B$ are said to be *conditionally independent* given $E$ if $P(A\cap B|E)=P(A|E)P(B|E)$.

It is easy to make terrible blunders stemming from confusing independence and conditional independence. Two events can be conditionally independent given $E$, but not independent given $E^{c}$. Two events can be conditionally independent given $E$, but not independent. Two events can be independent, but not conditionally independent given $E$.

In particular, $P(A,B)=P(A)P(B)$ does *not* imply $P(A,B|E)=P(A|E)P(B|E)$; we can’t just insert “given $E$” everywhere, as we did in going from LOTP to LOTP with extra conditioning. This is because LOTP *always* holds (it is a consequence of the axioms of probability), whereas $P(A,B)$ may or may not equal $P(A)P(B)$, depending on what $A$ and $B$ are.

The next few examples illustrate these distinctions. Great care is needed in working with conditional probabilities and conditional independence!

###### Example 2.5.9 (Conditional independence given $E$ vs. given $E^{c}$).

Suppose there are two types of classes: good classes and bad classes. In good classes, if you work hard, you are very likely to get an A. In bad classes, the professor randomly assigns grades to students regardless of their effort. Let $G$ be the event that a class is good, $W$ be the event that you work hard, and $A$ be the event that you receive an A. Then $W$ and $A$ are conditionally independent given $G^{c}$, but they are not conditionally independent given $G$. ∎

###### Example 2.5.10 (Conditional independence doesn’t imply independence).

Returning once more to the scenario from Example 2.3.7, suppose we have chosen either a fair coin or a biased coin with probability $3/4$ of Heads, but we do not know which one we have chosen. We flip the coin a number of times. Conditional on choosing the fair coin, the coin tosses are independent, with each toss having probability $1/2$ of Heads. Similarly, conditional on choosing the biased coin, the tosses are independent, each with probability $3/4$ of Heads.

However, the coin tosses are not unconditionally independent, because if we don’t know which coin we’ve chosen, then observing the sequence of tosses gives us information about whether we have the fair coin or the biased coin in our hand. This in turn helps us to predict the outcomes of future tosses from the same coin.