46. Independent Bernoulli trials are performed, with success probability 1/2 for each trial. An important question that often comes up in such settings is how many trials to perform. Many controversies have arisen in statistics over the issue of how to analyze data coming from an experiment where the number of trials can depend on the data collected so far.

For example, if we can follow the rule “keep performing trials until there are more than twice as many failures as successes, and then stop”, then naively looking at the ratio of failures to successes (if and when the process stops) will give more than 2:1 rather than the true theoretical 1:1 ratio; this could be a very misleading result! However, it might *never* happen that there are more than twice as many failures as successes; in this problem, you will find the probability of that happening.

(a) Two gamblers, A and B, make a series of bets, where each has probability 1/2 of winning a bet, but A gets $2 for each win and loses $1 for each loss (a very favorable game for A!). Assume that the gamblers are allowed to borrow money, so they can and do gamble forever. Let $p_{k}$ be the probability that A, starting with $$k, will ever reach $0, for each $k\geq 0$. Explain how this story relates to the original problem, and how the original problem can be solved if we can find $p_{k}$.

(b) Find $p_{k}$.

Hint: As in the gambler’s ruin, set up and solve a difference equation for $p_{k}$. We have $p_{k}\to 0$ as $k\to\infty$ (you don’t need to prove this, but it should make sense since the game is so favorable to A, which will result in A’s fortune going to $\infty$; a formal proof, not required here, could be done using the *law of large numbers*, an important theorem from Chapter 10). The solution can be written neatly in terms of the golden ratio.

(c) Find the probability of ever having more than twice as many failures as successes with independent Bern(1/2) trials, as originally desired.
47. A copy machine is used to make $n$ pages of copies per day. The machine has two trays in which paper gets loaded, and each page used is taken randomly and independently from one of the trays. At the beginning of the day, the trays are refilled so that they each have $m$ pages.

(a) Let pbinom($x,n,p$) be the CDF of the Bin($n,p$) distribution, evaluated at $x$. In terms of pbinom, find a simple expression for the probability that both trays have enough paper on any particular day, when this probability is strictly between 0 and 1 (also specify the values of $m$ for which the probability is 0 and the values for which it is 1).

Hint: Be careful about whether inequalities are strict, since the Binomial is discrete.

(b) Using a computer, find the smallest value of $m$ for which there is at least a 95% chance that both trays have enough paper on a particular day, for $n=10,n=100,n=1000$, and $n=10000$.

Hint: If you use R, you may find the following commands useful:
g <- function(m,n) *[your answer from (a)]* defines a function $g$ such that $g(m,n)$ is your answer from (a), g(1:100,100) gives the vector $(g(1,100),\ldots,g(100,100))$, which(v>0.95) gives the indices of the components of vector v that exceed 0.95, and min(w) gives the minimum of a vector w.