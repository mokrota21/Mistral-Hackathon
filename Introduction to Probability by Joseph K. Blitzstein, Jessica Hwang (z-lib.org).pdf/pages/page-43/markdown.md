ck and allow the remaining $n-2$ cards to be in any order, so $(n-2)!$ out of $n!$ possibilities are favorable to $A_{i}\cap A_{j}$. Similarly,

$P(A_{i}\cap A_{j}\cap A_{k})=\frac{1}{n(n-1)(n-2)},$

and the pattern continues for intersections of 4 events, etc.

In the inclusion-exclusion formula, there are $n$ terms involving one event, $\binom{n}{2}$ terms involving two events, $\binom{n}{3}$ terms involving three events, and so forth. By the symmetry of the problem, all $n$ terms of the form $P(A_{i})$ are equal, all $\binom{n}{2}$ terms of the form $P(A_{i}\cap A_{j})$ are equal, and the whole expression simplifies considerably:

$P\left(\bigcup_{i=1}^{n}A_{i}\right)$ $=\frac{n}{n}-\frac{\binom{n}{2}}{n(n-1)}+\frac{\binom{n}{3}}{n(n-1)(n-2)}-\cdots+(-1)^{n+1}\cdot\frac{1}{n!}$
$=1-\frac{1}{2!}+\frac{1}{3!}-\cdots+(-1)^{n+1}\cdot\frac{1}{n!}.$

Comparing this to the Taylor series for $1/e$ (see Section A.8 of the math appendix),

$e^{-1}=1-\frac{1}{1!}+\frac{1}{2!}-\frac{1}{3!}+\ldots,$

we see that for large $n$, the probability of winning the game is extremely close to $1-1/e$, or about $0.63$. Interestingly, as $n$ grows, the probability of winning approaches $1-1/e$ instead of going to $0$ or $1$. With a lot of cards in the deck, the number of possible locations for matching cards increases while the probability of any particular match decreases, and these two forces offset each other and balance to give a probability of about $1-1/e$. $\square$

Inclusion-exclusion is a very general formula for the probability of a union of events, but it helps us the most when there is symmetry among the events $A_{j}$; otherwise the sum can be extremely tedious. In general, when symmetry is lacking, we should try to use other tools before turning to inclusion-exclusion as a last resort.

### 1.7 Recap

Probability allows us to quantify uncertainty and randomness in a principled way. Probabilities arise when we perform an experiment: the set of all possible outcomes of the experiment is called the sample space, and a subset of the sample space is called an event. It is useful to be able to go back and forth between describing events in English and writing them down mathematically as sets (often using unions, intersections, and complements).