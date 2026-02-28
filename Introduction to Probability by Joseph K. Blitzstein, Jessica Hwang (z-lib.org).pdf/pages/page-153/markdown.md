from sampling $n$ balls from the urn with replacement, while the Hypergeometric arises from sampling without replacement. As the number of balls in the urn grows very large relative to the number of balls that are drawn, sampling with replacement and sampling without replacement become essentially equivalent. In practical terms, this theorem tells us that if $N=w+b$ is large relative to $n$, we can approximate the HGeom$(w,b,n)$ PMF by the Bin$(n,w/(w+b))$ PMF.

The birthday problem implies that it is surprisingly likely that some ball will be sampled more than once if sampling with replacement; for example, if 1,200 out of 1,000,000 balls are drawn randomly with replacement, then there is about a 51% chance that some ball will be drawn more than once! But this becomes less and less likely as $N$ grows, and even if it is likely that there will be a few coincidences, the approximation can still be reasonable if it is very likely that the vast majority of balls in the sample are sampled only once each.

### 3.10 Recap

A random variable (r.v.) is a function assigning a real number to every possible outcome of an experiment. The distribution of an r.v. $X$ is a full specification of the probabilities for the events associated with $X$, such as $\{X=3\}$ and $\{1\leq X\leq 5\}$. The distribution of a discrete r.v. can be defined using a PMF, a CDF, or a story. The PMF of $X$ is the function $P(X=x)$ for $x\in\mathbb{R}$. The CDF of $X$ is the function $P(X\leq x)$ for $x\in\mathbb{R}$. A story for $X$ describes an experiment that could give rise to a random variable with the same distribution as $X$.

For a PMF to be valid, it must be nonnegative and sum to 1. For a CDF to be valid, it must be increasing, right-continuous, converge to 0 as $x\to-\infty$, and converge to 1 as $x\to\infty$.

It is important to distinguish between a random variable and its distribution: the distribution is a blueprint for building the r.v., but different r.v.s can have the same distribution, just as different houses can be built from the same blueprint.

Four named discrete distributions are the Bernoulli, Binomial, Hypergeometric, and Discrete Uniform. Each of these is actually a *family* of distributions, indexed by parameters; to fully specify one of these distributions, we need to give both the name and the parameter values.

- A Bern($p$) r.v. is the indicator of success in a Bernoulli trial with probability of success $p$.
- A Bin($n,p$) r.v. is the number of successes in $n$ independent Bernoulli trials, all with the same probability $p$ of success.