###### Example 4.4.3 (Boole, Bonferroni, and inclusion-exclusion).

Let $A_{1},A_{2},\ldots,A_{n}$ be events. Note that

$I(A_{1}\cup\cdots\cup A_{n})\leq I(A_{1})+\cdots+I(A_{n}),$

since if the left-hand side is 0 this is immediate, and if the left-hand side is 1 then at least one term on the right-hand side must be 1. Taking the expectation of both sides and using linearity and the fundamental bridge, we have

$P(A_{1}\cup\cdots\cup A_{n})\leq P(A_{1})+\cdots+P(A_{n}),$

which is called *Boole’s inequality* or *Bonferroni’s inequality*. To prove inclusion-exclusion for $n=2$, we can take the expectation of both sides in Property 4 of Theorem 4.4.1. For general $n$, we can use properties of indicator r.v.s as follows:

$1-I(A_{1}\cup\cdots\cup A_{n})$ $=I(A_{1}^{c}\cap\cdots\cap A_{n}^{c})$
$=(1-I(A_{1}))\cdots(1-I(A_{n}))$
$=1-\sum_{i}I(A_{i})+\sum_{i<j}I(A_{i})I(A_{j})-\cdots+(-1)^{n}I(A_{1})\cdots I(A_{n}).$

Taking the expectation of both sides, by the fundamental bridge we have proven the inclusion-exclusion theorem. ∎

Conversely, the fundamental bridge is also extremely useful in many expected value problems. We can often express a complicated discrete r.v. whose distribution we don’t know as a sum of indicator r.v.s, which are extremely simple. The fundamental bridge lets us find the expectation of the indicators; then, using linearity, we obtain the expectation of our original r.v. This strategy is extremely useful and versatile—in fact, we already used it when deriving the expectations of the Binomial and Hypergeometric distributions earlier in this chapter!

Recognizing problems that are amenable to this strategy and then defining the indicator r.v.s takes practice, so it is important to study a lot of examples and solve a lot of problems. In applying the strategy to a random variable that counts the number of [noun]s, we should have an indicator for each potential [noun]. This [noun] could be a person, place, or thing; we will see examples of all three types.

We’ll start by revisiting two problems from Chapter 1, de Montmort’s matching problem and the birthday problem.

###### Example 4.4.4 (Matching continued).

We have a well-shuffled deck of $n$ cards, labeled 1 through $n$. A card is a *match* if the card’s position in the deck matches the card’s label. Let $X$ be the number of matches; find $E(X)$.

*Solution*:

First let’s check whether $X$ could have any of the named distributions we have studied. The Binomial and Hypergeometric are the only two candidates since the value of $X$ must be an integer between 0 and $n$. But neither of these distributions