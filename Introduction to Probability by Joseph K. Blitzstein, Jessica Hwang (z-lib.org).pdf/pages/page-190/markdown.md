if $\operatorname{Var}(X)>0$ (which will be true unless $X$ is a constant, as the next property shows).
- $\operatorname{Var}(X)\geq 0$, with equality if and only if $P(X=a)=1$ for some constant $a$. In other words, the only random variables that have zero variance are constants (which can be thought of as degenerate r.v.s); all other r.v.s have positive variance.

To prove the last property, note that $\operatorname{Var}(X)$ is the expectation of the *nonnegative* r.v. $(X-EX)^{2}$, so $\operatorname{Var}(X)\geq 0$. If $P(X=a)=1$ for some constant $a$, then $E(X)=a$ and $E(X^{2})=a^{2}$, so $\operatorname{Var}(X)=0$. Conversely, suppose that $\operatorname{Var}(X)=0$. Then $E(X-EX)^{2}=0$, which shows that $(X-EX)^{2}=0$ has probability $1$, which in turn shows that $X$ equals its mean with probability $1$.

#### 4.6.3 (Variance is not linear).

Unlike expectation, variance is *not* linear. The constant comes out *squared* in $\operatorname{Var}(cX)=c^{2}\operatorname{Var}(X)$, and the variance of the sum of r.v.s may not be the sum of their variances if they are dependent.

###### Example 4.6.4 (Geometric and Negative Binomial variance).

In this example we’ll use LOTUS to compute the variance of the Geometric distribution.

Let $X\sim\operatorname{Geom}(p)$. We already know $E(X)=q/p$. By LOTUS,

$E(X^{2})=\sum_{k=0}^{\infty}k^{2}P(X=k)=\sum_{k=0}^{\infty}k^{2}pq^{k}=\sum_{k=1}^{\infty}k^{2}pq^{k}.$

We’ll find this using a tactic similar to how we found the expectation, starting from the geometric series

$\sum_{k=0}^{\infty}q^{k}=\frac{1}{1-q}$

and taking derivatives. After differentiating once with respect to $q$, we have

$\sum_{k=1}^{\infty}kq^{k-1}=\frac{1}{(1-q)^{2}}.$

We start the sum from $k=1$ since the $k=0$ term is $0$ anyway. If we differentiate again, we’ll get $k(k-1)$ instead of $k^{2}$ as we want, so let’s replenish our supply of $q$’s by multiplying both sides by $q$. This gives

$\sum_{k=1}^{\infty}kq^{k}=\frac{q}{(1-q)^{2}}.$

Now we are ready to take another derivative:

$\sum_{k=1}^{\infty}k^{2}q^{k-1}=\frac{1+q}{(1-q)^{3}},$

so

$E(X^{2})=\sum_{k=1}^{\infty}k^{2}pq^{k}=pq\frac{1+q}{(1-q)^{3}}=\frac{q(1+q)}{p^{2}}.$