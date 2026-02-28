Conditional probability

51.  A gambler repeatedly plays a game where in each round, he wins a dollar with probability $1/3$ and loses a dollar with probability $2/3$. His strategy is “quit when he is ahead by $2”. Suppose that he starts with a million dollars. Show that the probability that he’ll ever be ahead by $2 is less than $1/4$.

52. As in the gambler’s ruin problem, two gamblers, A and B, make a series of bets, until one of the gamblers goes bankrupt. Let A start out with $i$ dollars and B start out with $N - i$ dollars, and let $p$ be the probability of A winning a bet, with $0 &lt; p &lt; \frac{1}{2}$. Each bet is for $\frac{1}{k}$ dollars, with $k$ a positive integer, e.g., $k = 1$ is the original gambler’s ruin problem and $k = 20$ means they’re betting nickels. Find the probability that A wins the game, and determine what happens to this as $k \to \infty$.

53. There are 100 equally spaced points around a circle. At 99 of the points, there are sheep, and at 1 point, there is a wolf. At each time step, the wolf randomly moves either clockwise or counterclockwise by 1 point. If there is a sheep at that point, he eats it. The sheep don’t move. What is the probability that the sheep who is initially opposite the wolf is the last one remaining?

54. An immortal drunk man wanders around randomly on the integers. He starts at the origin, and at each step he moves 1 unit to the right or 1 unit to the left, with probabilities $p$ and $q = 1 - p$ respectively, independently of all his previous steps. Let $S_{n}$ be his position after $n$ steps.

(a) Let $p_k$ be the probability that the drunk ever reaches the value $k$, for all $k \geq 0$. Write down a difference equation for $p_k$ (you do not need to solve it for this part).

(b) Find $p_k$, fully simplified; be sure to consider all 3 cases: $p &lt; 1/2, p = 1/2$, and $p &gt; 1/2$. Feel free to assume that if $A_1, A_2, \ldots$ are events with $A_j \subseteq A_{j+1}$ for all $j$, then $P(A_n) \to P(\cup_{j=1}^{\infty} A_j)$ as $n \to \infty$ (because it is true; this is known as continuity of probability).

## Simpson’s paradox

55.  (a) Is it possible to have events $A, B, C$ such that $P(A|C) &lt; P(B|C)$ and $P(A|C^c) &lt; P(B|C^c)$, yet $P(A) &gt; P(B)$? That is, $A$ is less likely than $B$ given that $C$ is true, and also less likely than $B$ given that $C$ is false, yet $A$ is more likely than $B$ if we’re given no information about $C$. Show this is impossible (with a short proof) or find a counterexample (with a story interpreting $A, B, C$).

(b) If the scenario in (a) is possible, is it a special case of Simpson’s paradox, equivalent to Simpson’s paradox, or neither? If it is impossible, explain intuitively why it is impossible even though Simpson’s paradox is possible.

56.  $\odot$ Consider the following conversation from an episode of *The Simpsons*:

Lisa: Dad, I think he’s an ivory dealer! His boots are ivory, his hat is ivory, and I’m pretty sure that check is ivory.

Homer: Lisa, a guy who has lots of ivory is less likely to hurt Stampy than a guy whose ivory supplies are low.

Here Homer and Lisa are debating the question of whether or not the man (named Blackheart) is likely to hurt Stampy the Elephant if they sell Stampy to him. They clearly disagree about how to use their observations about Blackheart to learn about the probability (conditional on the evidence) that Blackheart will hurt Stampy.

(a) Define clear notation for the various events of interest here.

(b) Express Lisa’s and Homer’s arguments (Lisa’s is partly implicit) as conditional probability statements in terms of your notation from (a).