Random variables and their distributions

- Claiming that because $X$ and $Y$ have the same distribution, $X$ must always equal $Y$, i.e., $P(X=Y)=1$. Just because two r.v.s have the same distribution does not mean they are always equal, or *ever* equal. We saw this in Example 3.2.5. As another example, consider flipping a fair coin once. Let $X$ be the indicator of Heads and $Y=1-X$ be the indicator of Tails. Both $X$ and $Y$ have the $\operatorname{Bern}(1/2)$ distribution, but the event $X=Y$ is impossible. The PMFs of $X$ and $Y$ are the same function, but $X$ and $Y$ are different mappings from the sample space to the real numbers.

If $Z$ is the indicator of Heads in a second flip (independent of the first flip), then $Z$ is also $\operatorname{Bern}(1/2)$, but $Z$ is not the same r.v. as $X$. Here

$P(Z=X)=P(HH\text{ or }TT)=1/2.$

### 3.8 Independence of r.v.s

Just as we had the notion of independence of events, we can define independence of random variables. Intuitively, if two r.v.s $X$ and $Y$ are independent, then knowing the value of $X$ gives no information about the value of $Y$, and vice versa. The definition formalizes this idea.

###### Definition 3.8.1 (Independence of two r.v.s).

Random variables $X$ and $Y$ are said to be *independent* if

$P(X\leq x,Y\leq y)=P(X\leq x)P(Y\leq y),$

for all $x,y\in\mathbb{R}$.

In the discrete case, this is equivalent to the condition

$P(X=x,Y=y)=P(X=x)P(Y=y),$

for all $x,y$ with $x$ in the support of $X$ and $y$ in the support of $Y$.

The definition for more than two r.v.s is analogous.

###### Definition 3.8.2 (Independence of many r.v.s).

Random variables $X_{1},\ldots,X_{n}$ are *independent* if

$P(X_{1}\leq x_{1},\ldots,X_{n}\leq x_{n})=P(X_{1}\leq x_{1})\ldots P(X_{n}\leq x_{n}),$

for all $x_{1},\ldots,x_{n}\in\mathbb{R}$. For infinitely many r.v.s, we say that they are independent if every finite subset of the r.v.s is independent.

Comparing this to the criteria for independence of $n$ events, it may seem strange that the independence of $X_{1},\ldots,X_{n}$ requires just one equality, whereas for events we