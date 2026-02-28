Conditional probability

round, we have

$$
\begin{array}{l}
p_{i} = P(W|\text{A starts at } i, \text{ wins round } 1) \cdot p + P(W|\text{A starts at } i, \text{ loses round } 1) \cdot q \\
= P(W|\text{A starts at } i + 1) \cdot p + P(W|\text{A starts at } i - 1) \cdot q \\
= p_{i+1} \cdot p + p_{i-1} \cdot q.
\end{array}
$$

This must be true for all $i$ from 1 to $N - 1$, and we also have the boundary conditions $p_0 = 0$ and $p_N = 1$. Now we can solve this equation, called a difference equation, to obtain the $p_i$. Section A.4 of the math appendix discusses how to solve difference equations, so we will omit some of the steps here.

The characteristic equation of the difference equation is $px^2 - x + q = 0$, which has roots 1 and $q/p$. If $p \neq 1/2$, these roots are distinct, and the general solution is

$$
p_{i} = a \cdot 1^{i} + b \cdot \left(\frac{q}{p}\right)^{i}.
$$

Using the boundary conditions $p_0 = 0$ and $p_N = 1$, we get

$$
a = -b = \frac{1}{1 - \left(\frac{q}{p}\right)^N},
$$

and we simply plug these back in to get the specific solution. If $p = 1/2$, the roots of the characteristic polynomial are not distinct, so the general solution is

$$
p_{i} = a \cdot 1^{i} + b \cdot i \cdot 1^{i}.
$$

The boundary conditions give $a = 0$ and $b = 1/N$.

In summary, the probability of A winning with a starting wealth of $i$ is

$$
p_{i} = \left\{
\begin{array}{ll}
\frac{1 - \left(\frac{q}{p}\right)^{i}}{1 - \left(\frac{q}{p}\right)^{N}} &amp; \text{if } p \neq 1/2, \\
\frac{i}{N} &amp; \text{if } p = 1/2.
\end{array}
\right.
$$

The $p = 1/2$ case is consistent with the $p \neq 1/2$ case, in the sense that

$$
\lim_{p \to \frac{1}{2}} \frac{1 - \left(\frac{q}{p}\right)^i}{1 - \left(\frac{q}{p}\right)^N} = \frac{i}{N}.
$$

To see this, let $x = q/p$ and let $x$ approach 1. By L'Hôpital's rule,

$$
\lim_{x \to 1} \frac{1 - x^{i}}{1 - x^{N}} = \lim_{x \to 1} \frac{i x^{i-1}}{N x^{N-1}} = \frac{i}{N}.
$$

The answer for the $p = 1/2$ case has a simple interpretation: A's probability of winning equals the proportion of the wealth that A starts out with. So if $p = 1/2$