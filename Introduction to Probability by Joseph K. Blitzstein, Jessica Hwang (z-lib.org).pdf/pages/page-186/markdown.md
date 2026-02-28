continue drawing balls until the urn is empty. First consider the case $r=1$. Label the black balls as $1,2,\ldots,b$, and let $I_{j}$ be the indicator of black ball $j$ being drawn before any white balls have been drawn. Then $P(I_{j}=1)=1/(w+1)$ since, listing out the order in which black ball $j$ and the white balls are drawn (ignoring the other balls), all orders are equally likely by symmetry, and $I_{j}=1$ is equivalent to black ball $j$ being first in this list. So by linearity,

$E\left(\sum_{j=1}^{b}I_{j}\right)=\sum_{j=1}^{b}E(I_{j})=b/(w+1).$

Sanity check: This answer makes sense since it is increasing in $b$, decreasing in $w$, and correct in the extreme cases $b=0$ (when no black balls will be drawn) and $w=0$ (when all the black balls will be exhausted before drawing a nonexistent white ball). Moreover, note that $b/(w+1)$ looks similar to, but is strictly smaller than, $b/w$, which is the expected value of a $\text{Geom}(w/(w+b))$ r.v. It makes sense that sampling without replacement should give a smaller expected waiting time than sampling with replacement. Similarly, if you are searching for something you lost, it makes more sense to choose locations to check without replacement, rather than wasting time looking over and over again in locations you already ruled out.

For general $r$, write $X=X_{1}+X_{2}+\cdots+X_{r}$, where $X_{1}$ is the number of black balls before the first white ball, $X_{2}$ is the number of black balls after the first white ball but before the second white ball, etc. By essentially the same argument we used to handle the $r=1$ case, we have $E(X_{j})=b/(w+1)$ for each $j$. So by linearity,

$E(X)=rb/(w+1).\qed$

Closely related to indicator r.v.s is an alternative expression for the expectation of a nonnegative integer-valued r.v. $X$. Rather than summing up values of $X$ times values of the PMF of $X$, we can sum up probabilities of the form $P(X>n)$ (known as tail probabilities), over nonnegative integers $n$.

###### Theorem 4.4.8 (Expectation via survival function).

Let $X$ be a nonnegative integer-valued r.v. Let $F$ be the CDF of $X$, and $G(x)=1-F(x)=P(X>x)$. The function $G$ is called the survival function of $X$. Then

$E(X)=\sum_{n=0}^{\infty}G(n).$

That is, we can obtain the expectation of $X$ by summing up the survival function (or, stated otherwise, summing up tail probabilities of the distribution).

###### Proof.

For simplicity, we will prove the result only for the case that $X$ is bounded, i.e., there is a nonnegative integer $b$ such that $X$ is always at most $b$. We can represent $X$ as a sum of indicator r.v.s: $X=I_{1}+I_{2}+\cdots+I_{b}$, where $I_{n}=I(X\geq n)$. For