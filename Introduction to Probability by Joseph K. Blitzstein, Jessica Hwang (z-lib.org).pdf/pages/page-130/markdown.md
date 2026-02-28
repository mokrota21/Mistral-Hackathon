about the type of experiment that could give rise to a random variable with a Binomial distribution. The most famous distributions in statistics all have stories which explain why they are so often used as models for data, or as the building blocks for more complicated distributions.

Thinking about the named distributions first and foremost in terms of their stories has many benefits. It facilitates pattern recognition, allowing us to see when two problems are essentially identical in structure; it often leads to cleaner solutions that avoid PMF calculations altogether; and it helps us understand how the named distributions are connected to one another. Here it is clear that $\mathrm{Bern}(p)$ is the same distribution as $\mathrm{Bin}(1,p)$: the Bernoulli is a special case of the Binomial.

Using the story definition of the Binomial, let’s find its PMF.

###### Theorem 3.3.5 (Binomial PMF).

If $X\sim\mathrm{Bin}(n,p)$, then the PMF of $X$ is

$P(X=k)={n\choose k}p^{k}(1-p)^{n-k}$

for $k=0,1,\ldots,n$ (and $P(X=k)=0$ otherwise).

$\nLeftrightarrow$ 3.3.6. To save writing, it is often left implicit that a PMF is zero wherever it is not specified to be nonzero, but in any case it is important to understand what the support of a random variable is, and good practice to check that PMFs are valid. If two discrete r.v.s have the same PMF, then they also must have the same support. So we sometimes refer to the support of a discrete distribution; this is the support of any r.v. with that distribution.

###### Proof.

An experiment consisting of $n$ independent Bernoulli trials produces a sequence of successes and failures. The probability of any specific sequence of $k$ successes and $n-k$ failures is $p^{k}(1-p)^{n-k}$. There are ${n\choose k}$ such sequences, since we just need to select where the successes are. Therefore, letting $X$ be the number of successes,

$P(X=k)={n\choose k}p^{k}(1-p)^{n-k}$

for $k=0,1,\ldots,n$, and $P(X=k)=0$ otherwise. This is a valid PMF because it is nonnegative and it sums to $1$ by the binomial theorem. ∎

Figure 3.6 shows plots of the Binomial PMF for various values of $n$ and $p$. Note that the PMF of the $\mathrm{Bin}(10,1/2)$ distribution is symmetric about $5$, but when the success probability is not $1/2$, the PMF is skewed. For a fixed number of trials $n$, $X$ tends to be larger when the success probability is high and lower when the success probability is low, as we would expect from the story of the Binomial distribution. Also recall that in any PMF plot, the sum of the heights of the vertical bars must be $1$.

We’ve used Story 3.3.4 to find the $\mathrm{Bin}(n,p)$ PMF. The story also gives us a straightforward proof of the fact that if $X$ is Binomial, then $n-X$ is also Binomial.