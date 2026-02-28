Before proving LOTUS in general, let’s see why it is true in some special cases. Let $X$ have support $0,1,2,\dots$ with probabilities $p_{0},p_{1},p_{2},\dots$, so the PMF is $P(X=n)=p_{n}$. Then $X^{3}$ has support $0^{3},1^{3},2^{3},\dots$ with probabilities $p_{0},p_{1},p_{2},\dots$, so

$E(X)$ $=\sum_{n=0}^{\infty}np_{n},$
$E(X^{3})$ $=\sum_{n=0}^{\infty}n^{3}p_{n}.$

As claimed by LOTUS, to edit the expression for $E(X)$ into an expression for $E(X^{3})$, we can just change the $n$ in front of the $p_{n}$ to an $n^{3}$. This was an easy example since the function $g(x)=x^{3}$ is one-to-one. But LOTUS holds much more generally. The key insight needed for the proof of LOTUS for general $g$ is the same as the one we used for the proof of linearity: the expectation of $g(X)$ can be written in ungrouped form as

$E(g(X))=\sum_{s}g(X(s))P(\{s\}),$

where the sum is over all the pebbles in the sample space, but we can also group the pebbles into super-pebbles according to the value that $X$ assigns to them. Within the super-pebble $X=x$, $g(X)$ always takes on the value $g(x)$. Therefore,

$E(g(X))$ $=\sum_{s}g(X(s))P(\{s\})$
$=\sum_{x}\sum_{s:X(s)=x}g(X(s))P(\{s\})$
$=\sum_{x}g(x)\sum_{s:X(s)=x}P(\{s\})$
$=\sum_{x}g(x)P(X=x).$

In the last step, we used the fact that $\sum_{s:X(s)=x}P(\{s\})$ is the weight of the super-pebble $X=x$.

### 4.6 Variance

One important application of LOTUS is for finding the variance of a random variable. Like expected value, variance is a single-number summary of the distribution of a random variable. While the expected value tells us the center of mass of a distribution, the variance tells us how spread out the distribution is.

###### Definition 4.6.1 (Variance and standard deviation).

The variance of an r.v. $X$ is

$\mathrm{Var}(X)=E(X-EX)^{2}.$