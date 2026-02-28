24. Let $X$ be the number of Heads in 10 fair coin tosses.

1. Find the conditional PMF of $X$, given that the first two tosses both land Heads.
2. Find the conditional PMF of $X$, given that at least two tosses land Heads.
25. Alice flips a fair coin $n$ times and Bob flips another fair coin $n+1$ times, resulting in independent $X\sim{\rm Bin}(n,\frac{1}{2})$ and $Y\sim{\rm Bin}(n+1,\frac{1}{2})$.

1. Show that $P(X<Y)=P(n-X<n+1-Y)$.
2. Compute $P(X<Y)$.

Hint: Use (a) and the fact that $X$ and $Y$ are integer-valued.
26. If $X\sim{\rm HGeom}(w,b,n)$, what is the distribution of $n-X$? Give a short proof.
27. Recall de Montmort’s matching problem from Chapter 1: in a deck of $n$ cards labeled 1 through $n$, a match occurs when the number on the card matches the card’s position in the deck. Let $X$ be the number of matching cards. Is $X$ Binomial? Is $X$ Hypergeometric?
28. There are $n$ eggs, each of which hatches a chick with probability $p$ (independently). Each of these chicks survives with probability $r$, independently. What is the distribution of the number of chicks that hatch? What is the distribution of the number of chicks that survive? (Give the PMFs; also give the names of the distributions and their parameters, if applicable.)
29. A sequence of $n$ independent experiments is performed. Each experiment is a success with probability $p$ and a failure with probability $q=1-p$. Show that conditional on the number of successes, all valid possibilities for the list of outcomes of the experiment are equally likely.
30. A certain company has $n+m$ employees, consisting of $n$ women and $m$ men. The company is deciding which employees to promote.

1. Suppose for this part that the company decides to promote $t$ employees, where $1\leq t\leq n+m$, by choosing $t$ random employees (with equal probabilities for each set of $t$ employees). What is the distribution of the number of women who get promoted?
2. Now suppose that instead of having a predetermined number of promotions to give, the company decides independently for each employee, promoting the employee with probability $p$. Find the distributions of the number of women who are promoted, the number of women who are not promoted, and the number of employees who are promoted.
3. In the set-up from (b), find the conditional distribution of the number of women who are promoted, given that exactly $t$ employees are promoted.
31. Once upon a time, a famous statistician offered tea to a lady. The lady claimed that she could tell whether milk had been added to the cup before or after the tea. The statistician decided to run some experiments to test her claim.

1. The lady is given 6 cups of tea, where it is known in advance that 3 will be milk-first and 3 will be tea-first, in a completely random order. The lady gets to taste each and then guess which 3 were milk-first. Assume for this part that she has no ability whatsoever to distinguish milk-first from tea-first cups of tea. Find the probability that at least 2 of her 3 guesses are correct.
2. Now the lady is given one cup of tea, with probability $1/2$ of it being milk-first. She needs to say whether she thinks it was milk-first. Let $p_{1}$ be the lady’s probability of being correct given that it was milk-first, and $p_{2}$ be her probability of being correct given that it was tea-first. She claims that the cup was milk-first. Find the posterior odds that the cup is milk-first, given this information.