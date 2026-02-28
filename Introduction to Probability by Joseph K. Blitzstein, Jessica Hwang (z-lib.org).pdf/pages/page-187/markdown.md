example, if $X=7$ occurs, then $I_{1}$ through $I_{7}$ equal 1 while the other indicators equal 0.

By linearity and the fundamental bridge, and the fact that $\{X\geq k\}$ is the same event as $\{X>k-1\}$,

$E(X)=\sum_{k=1}^{b}E(I_{k})=\sum_{k=1}^{b}P(X\geq k)=\sum_{n=0}^{b-1}P(X>n)=\sum_{n=0}^{\infty}G(n).$

As a quick example, we use the above result to give another derivation of the mean of a Geometric r.v.

###### Example 4.4.9 (Geometric expectation redux).

Let $X\sim\text{Geom}(p)$, and $q=1-p$. Using the Geometric story, $\{X>n\}$ is the event that the first $n+1$ trials are all failures. So by Theorem 4.4.8,

$E(X)=\sum_{n=0}^{\infty}P(X>n)=\sum_{n=0}^{\infty}q^{n+1}=\frac{q}{1-q}=\frac{q}{p},$

confirming what we already knew about the mean of a Geometric. $\square$

### 4.5 Law of the unconscious statistician (LOTUS)

As we saw in the St. Petersburg paradox, $E(g(X))$ does *not* equal $g(E(X))$ in general if $g$ is not linear. So how do we correctly calculate $E(g(X))$? Since $g(X)$ is an r.v., one way is to first find the distribution of $g(X)$ and then use the definition of expectation. Perhaps surprisingly, it turns out that it is possible to find $E(g(X))$ directly using the distribution of $X$, without first having to find the distribution of $g(X)$. This is done using the *law of the unconscious statistician* (LOTUS).

###### Theorem 4.5.1 (LOTUS).

If $X$ is a discrete r.v. and $g$ is a function from $\mathbb{R}$ to $\mathbb{R}$, then

$E(g(X))=\sum_{x}g(x)P(X=x),$

where the sum is taken over all possible values of $X$.

This means that we can get the expected value of $g(X)$ knowing only $P(X=x)$, the PMF of $X$; we don’t need to know the PMF of $g(X)$. The name comes from the fact that in going from $E(X)$ to $E(g(X))$ it is tempting just to change $x$ to $g(x)$ in the definition, which can be done very easily and mechanically, perhaps in a state of unconsciousness. On second thought, it may sound too good to be true that finding the distribution of $g(X)$ is not needed for this calculation, but LOTUS says it *is* true.