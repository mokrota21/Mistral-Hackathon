Introduction to Probability

(other than door 1), revealing a goat, and then offers you the option to switch to another door. Monty then opens *another* door (other than your currently selected door), revealing another goat. So now there are two open doors (with goats) and two unopened doors. Again Monty offers you the option to switch.

You decide in advance to use one of the following four strategies: stay-stay, stay-switch, switch-stay, switch-switch, where, for example, “stay-switch” means that the first time Monty offers you the choice of switching, you stay with your current selection, but then the second time Monty offers you the choice, you do switch doors. In each part below the goal is to find or compare *unconditional* probabilities, i.e., from a vantage point of before the game has started.

1. Find the probability of winning the car if you follow the stay-stay strategy.
2. Find the probability of winning the car if you follow the stay-switch strategy.
3. Find the probability of winning the car if you follow the switch-stay strategy.
4. Find the probability of winning the car if you follow the switch-switch strategy.
5. Which of these four strategies is the best?

### First-step analysis and gambler’s ruin

1. $\circledS$ A fair die is rolled repeatedly, and a running total is kept (which is, at each time, the total of all the rolls up until that time). Let $p_{n}$ be the probability that the running total is ever *exactly* $n$ (assume the die will always be rolled enough times so that the running total will eventually exceed $n$, but it may or may not ever equal $n$).

1. Write down a recursive equation for $p_{n}$ (relating $p_{n}$ to earlier terms $p_{k}$ in a simple way). Your equation should be true for all positive integers $n$, so give a definition of $p_{0}$ and $p_{k}$ for $k&lt;0$ so that the recursive equation is true for small values of $n$.
2. Find $p_{7}$.
3. Give an intuitive explanation for the fact that $p_{n}\to 1/3.5=2/7$ as $n\to\infty$.
2. A sequence of $n\geq 1$ independent trials is performed, where each trial ends in “success” or “failure” (but not both). Let $p_{i}$ be the probability of success in the $i$th trial, $q_{i}=1-p_{i}$, and $b_{i}=q_{i}-1/2$, for $i=1,2,\ldots,n$. Let $A_{n}$ be the event that the number of successful trials is even.

1. Show that for $n=2$, $P(A_{2})=1/2+2b_{1}b_{2}$.
2. Show by induction that

$P(A_{n})=1/2+2^{n-1}b_{1}b_{2}\ldots b_{n}.$

(This result is very useful in cryptography. Also, note that it implies that if $n$ coins are flipped, then the probability of an even number of Heads is $1/2$ if and only if at least one of the coins is fair.) Hint: Group some trials into a supertrial.

1. Check directly that the result of (b) is true in the following simple cases: $p_{i}=1/2$ for some $i$; $p_{i}=0$ for all $i$; $p_{i}=1$ for all $i$.
3. Calvin and Hobbes play a match consisting of a series of games, where Calvin has probability $p$ of winning each game (independently). They play with a “win by two” rule: the first player to win two games more than his opponent wins the match. Find the probability that Calvin wins the match (in terms of $p$), in two different ways:

1. by conditioning, using the law of total probability.
2. by interpreting the problem as a gambler’s ruin problem.