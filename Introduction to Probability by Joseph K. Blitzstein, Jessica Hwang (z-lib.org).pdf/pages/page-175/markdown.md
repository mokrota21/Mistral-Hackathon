This is a valid PMF because, summing a geometric series (see the math appendix for a review of geometric series), we have

$\sum_{k=0}^{\infty}q^{k}p=p\sum_{k=0}^{\infty}q^{k}=p\cdot\frac{1}{1-q}=1.$

Just as the binomial theorem shows that the Binomial PMF is valid, a geometric series shows that the Geometric PMF is valid! A geometric series can also be used to obtain the Geometric CDF.

###### Theorem 4.3.3 (Geometric CDF).

If $X\sim\mathrm{Geom}(p)$, then the CDF of $X$ is

\[ F(x)=\begin{cases}1-q^{\lfloor x\rfloor+1},\text{ if }x\geq 0;\\
0,\text{ if }x<0,\end{cases} \]

where $q=1-p$ and $\lfloor x\rfloor$ is the greatest integer less than or equal to $x$.

###### Proof.

Let $F$ be the CDF of $X$. We will find $F(x)$ first for the case $x<0$, then for the case that $x$ is a nonnegative integer, and lastly for the case that $x$ is a nonnegative real number. For $x<0$, $F(x)=0$ since $X$ can’t be negative. For $n$ a nonnegative integer,

$F(n)=\sum_{k=0}^{n}P(X=k)=p\sum_{k=0}^{n}q^{k}=p\cdot\frac{1-q^{n+1}}{1-q}=1-q^{n+1}.$

We can also get the same result from the fact that the event $X\geq n+1$ means that the first $n+1$ trials were failures:

$F(n)=1-P(X>n)=1-P(X\geq n+1)=1-q^{n+1}.$

For real $x\geq 0$,

$F(x)=P(X\leq x)=P(X\leq\lfloor x\rfloor),$

since $X$ always takes on integer values. For example,

$P(X\leq 3.7)=P(X\leq 3)+P(3<X\leq 3.7)=P(X\leq 3).$

Therefore, $F$ is as claimed. ∎

Figure 4.3 displays the $\mathrm{Geom}(0.5)$ PMF and CDF from $0$ to $6$. All Geometric PMFs have a similar shape; the greater the success probability $p$, the more quickly the PMF decays to $0$.

$\text{\text{✳ 4.3.4 (Conventions for the Geometric).}$ There are differing conventions for the definition of the Geometric distribution; some sources define the Geometric as the total number of *trials*, including the success. In this book, the Geometric distribution excludes the success, and the *First Success* distribution includes the success.