- Right-continuous: As in Figure 3.8, the CDF is continuous except possibly for having some jumps. Wherever there is a jump, the CDF is continuous from the right. That is, for any $a$, we have

$F(a)=\lim_{x\to a^{+}}F(x).$
- Convergence to $0$ and $1$ in the limits:

$\lim_{x\to-\infty}F(x)=0\text{ and }\lim_{x\to\infty}F(x)=1.$

###### Proof.

The above criteria are true for *all* CDFs, but for simplicity we will only prove it for the case where $F$ is the CDF of a discrete r.v. $X$ whose possible values are $0,1,2,\dots$. As an example of how to visualize the criteria, consider Figure 3.8: the CDF shown there is increasing (with some flat regions), continuous from the right (it is continuous except at jumps, and each jump has an open dot at the bottom and a closed dot at the top), and it converges to $0$ as $x\to-\infty$ and to $1$ as $x\to\infty$ (in this example, it reaches $0$ and $1$; in some examples, one or both of these values may be approached but never reached).

The first criterion is true since the event $\{X\leq x_{1}\}$ is a subset of the event $\{X\leq x_{2}\}$, so $P(X\leq x_{1})\leq P(X\leq x_{2})$.

For the second criterion, note that

$P(X\leq x)=P(X\leq\lfloor x\rfloor),$

where $\lfloor x\rfloor$ is the greatest integer less than or equal to $x$. For example, $P(X\leq 4.9)=P(X\leq 4)$ since $X$ is integer-valued. So $F(a+b)=F(a)$ for any $b>0$ that is small enough so that $a+b<\lfloor a\rfloor+1$, e.g., for $a=4.9$, this holds for $0<b<0.1$. This implies $F(a)=\lim_{x\to a^{+}}F(x)$ (in fact, it’s much stronger since it says $F(x)$ *equals* $F(a)$ when $x$ is close enough to $a$ and on the right).

For the third criterion, we have $F(x)=0$ for $x<0$, and

$\lim_{x\to\infty}F(x)=\lim_{x\to\infty}P(X\leq\lfloor x\rfloor)=\lim_{x\to\infty}\sum_{n=0}^{\lfloor x\rfloor}P(X=n)=\sum_{n=0}^{\infty}P(X=n)=1.$

The converse is true too: we will show in Chapter 5 that given any function $F$ meeting these criteria, we can construct a random variable whose CDF is $F$.

To recap, we have now seen three equivalent ways of expressing the distribution of a random variable. Two of these are the PMF and the CDF: we know these two functions contain the same information, since we can always figure out the CDF from the PMF and vice versa. Generally the PMF is easier to work with for discrete r.v.s, since evaluating the CDF requires a summation.