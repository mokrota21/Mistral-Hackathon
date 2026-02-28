chance that another ball in the sample is white. However, linearity still holds for dependent random variables! Thus,

$E(X)=nw/(w+b).\qed$

As another example of the power of linearity, we can give a quick proof of the intuitive idea that “bigger r.v.s have bigger expectations”.

###### Proposition 4.2.4 (Monotonicity of expectation).

Let $X$ and $Y$ be r.v.s such that $X\geq Y$ with probability 1. Then $E(X)\geq E(Y)$, with equality holding if and only if $X=Y$ with probability 1.

###### Proof.

This result holds for all r.v.s, but we will prove it only for discrete r.v.s since this chapter focuses on discrete r.v.s. The r.v. $Z=X-Y$ is nonnegative (with probability 1), so $E(Z)\geq 0$ since $E(Z)$ is defined as a sum of nonnegative terms. By linearity,

$E(X)-E(Y)=E(X-Y)\geq 0,$

as desired. If $E(X)=E(Y)$, then by linearity we also have $E(Z)=0$, which implies that $P(X=Y)=P(Z=0)=1$ since if even one term in the sum defining $E(Z)$ is positive, then the whole sum is positive. ∎

### 4.3 Geometric and Negative Binomial

We now introduce two more famous discrete distributions, the Geometric and Negative Binomial, and calculate their expected values.

###### Story 4.3.1 (Geometric distribution).

Consider a sequence of independent Bernoulli trials, each with the same success probability $p\in(0,1)$, with trials performed until a success occurs. Let $X$ be the number of *failures* before the first successful trial. Then $X$ has the *Geometric distribution* with parameter $p$; we denote this by $X\sim\operatorname{Geom}(p)$. ∎

For example, if we flip a fair coin until it lands Heads for the first time, then the number of Tails before the first occurrence of Heads is distributed as $\operatorname{Geom}(1/2)$.

To get the Geometric PMF from the story, imagine the Bernoulli trials as a string of 0’s (failures) ending in a single 1 (success). Each 0 has probability $q=1-p$ and the final 1 has probability $p$, so a string of $k$ failures followed by one success has probability $q^{k}p$.

###### Theorem 4.3.2 (Geometric PMF).

If $X\sim\operatorname{Geom}(p)$, then the PMF of $X$ is

$P(X=k)=q^{k}p$

for $k=0,1,2,\dots$, where $q=1-p$.

######