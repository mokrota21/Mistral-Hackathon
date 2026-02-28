Finally,

$\mathrm{Var}(X)=E(X^{2})-(EX)^{2}=\frac{q(1+q)}{p^{2}}-\left(\frac{q}{p}\right)^{2}=\frac{q}{p^{2}}.$

This is also the variance of the First Success distribution, since shifting by a constant does not affect the variance.

Since an $\mathrm{NBin}(r,p)$ r.v. can be represented as a sum of $r$ i.i.d. $\mathrm{Geom}(p)$ r.v.s by Theorem 4.3.10, and since variance is additive for independent random variables, it follows that the variance of the $\mathrm{NBin}(r,p)$ distribution is $r\cdot\frac{q}{p^{2}}$. ∎

LOTUS is an all-purpose tool for computing $E(g(X))$ for any $g$, but as it usually leads to complicated sums, it should be used as a last resort. For variance calculations, our trusty indicator r.v.s can sometimes be used in place of LOTUS, as in the next example.

###### Example 4.6.5 (Binomial variance).

Let’s find the variance of $X\sim\mathrm{Bin}(n,p)$ using indicator r.v.s to avoid tedious sums. Represent $X=I_{1}+I_{2}+\cdots+I_{n}$, where $I_{j}$ is the indicator of the $j$th trial being a success. Each $I_{j}$ has variance

$\mathrm{Var}(I_{j})=E(I_{j}^{2})-(E(I_{j}))^{2}=p-p^{2}=p(1-p).$

(Recall that $I_{j}^{2}=I_{j}$, so $E(I_{j}^{2})=E(I_{j})=p$.)

Since the $I_{j}$ are independent, we can add their variances to get the variance of their sum:

$\mathrm{Var}(X)=\mathrm{Var}(I_{1})+\cdots+\mathrm{Var}(I_{n})=np(1-p).$

Alternatively, we can find $E(X^{2})$ by first finding $E\binom{X}{2}$. The latter sounds more complicated, but actually it is simpler since $\binom{X}{2}$ is the number of *pairs* of successful trials. Creating an indicator r.v. for each pair of trials, we have

$E\binom{X}{2}=\binom{n}{2}p^{2}.$

Thus,

$n(n-1)p^{2}=E(X(X-1))=E(X^{2})-E(X)=E(X^{2})-np,$

which again gives

$\mathrm{Var}(X)=E(X^{2})-(EX)^{2}=(n(n-1)p^{2}+np)-(np)^{2}=np(1-p).$

Exercise 48 uses this strategy to find the variance of the Hypergeometric. ∎

### 4.7 Poisson

The last discrete distribution that we’ll introduce in this chapter is the Poisson, which is an extremely popular distribution for modeling discrete data. We’ll introduce its PMF, mean, and variance, and then discuss its story in more detail.