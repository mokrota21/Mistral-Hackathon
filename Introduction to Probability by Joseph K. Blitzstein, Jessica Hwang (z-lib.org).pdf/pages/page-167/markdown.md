$x_{1},x_{2},\dots$ is defined by

$E(X)=\sum_{j=1}^{\infty}x_{j}P(X=x_{j}).$

If the support is finite, then this is replaced by a finite sum. We can also write

$E(X)=\sum_{x}\underbrace{x}_{\text{value}}\underbrace{P(X=x)}_{\text{PMF at }x},$

where the sum is over the support of $X$ (in any case, $xP(X=x)$ is $0$ for any $x$ not in the support). The expectation is undefined if $\sum_{j=1}^{\infty}|x_{j}|P(X=x_{j})$ diverges, since then the series for $E(X)$ diverges or its value depends on the order in which the $x_{j}$ are listed.

In words, the expected value of $X$ is a weighted average of the possible values that $X$ can take on, weighted by their probabilities. Let’s check that the definition makes sense in a few simple examples:

1. Let $X$ be the result of rolling a fair $6$-sided die, so $X$ takes on the values $1,2,3,4,5,6$, with equal probabilities. Intuitively, we should be able to get the average by adding up these values and dividing by $6$. Using the definition, the expected value is

$E(X)=\frac{1}{6}(1+2+\dots+6)=3.5,$

as we expected. Note that $X$ *never* equals its mean in this example. This is similar to the fact that the average number of children per household in some country could be $1.8$, but that doesn’t mean that a typical household has $1.8$ children!
2. Let $X\sim\text{Bern}(p)$ and $q=1-p$. Then

$E(X)=1p+0q=p,$

which makes sense intuitively since it is between the two possible values of $X$, compromising between $0$ and $1$ based on how likely each is. This is illustrated in Figure 4.1 for a case with $p<1/2$: two pebbles are being balanced on a seesaw. For the seesaw to balance, the fulcrum (shown as a triangle) must be at $p$, which in physics terms is the *center of mass*.

The frequentist interpretation would be to consider a large number of independent Bernoulli trials, each with probability $p$ of success. Writing $1$ for “success” and $0$ for “failure”, in the long run we would expect to have data consisting of a list of numbers where the proportion of $1$’s is very close to $p$. The average of a list of $0$’s and $1$’s *is* the proportion of $1$’s.
3. Let $X$ have $3$ distinct possible values, $a_{1},a_{2},a_{3}$, with probabilities $p_{1},p_{2},p_{3}$, respectively. Imagine running a simulation where $n$ independent draws