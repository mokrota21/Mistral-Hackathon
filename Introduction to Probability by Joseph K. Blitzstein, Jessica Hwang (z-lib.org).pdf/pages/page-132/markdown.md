###### Theorem 3.3.7.

Let $X\sim\mathrm{Bin}(n,p)$, and $q=1-p$ (we often use $q$ to denote the failure probability of a Bernoulli trial). Then $n-X\sim\mathrm{Bin}(n,q)$.

###### Proof.

Using the story of the Binomial, interpret $X$ as the number of successes in $n$ independent Bernoulli trials. Then $n-X$ is the number of failures in those trials. Interchanging the roles of success and failure, we have $n-X\sim\mathrm{Bin}(n,q)$. Alternatively, we can check that $n-X$ has the $\mathrm{Bin}(n,q)$ PMF. Let $Y=n-X$. The PMF of $Y$ is

$P(Y=k)=P(X=n-k)={n\choose n-k}p^{n-k}q^{k}={n\choose k}q^{k}p^{n-k},$

for $k=0,1,\ldots,n$. ∎

###### Corollary 3.3.8.

Let $X\sim\mathrm{Bin}(n,p)$ with $p=1/2$ and $n$ even. Then the distribution of $X$ is symmetric about $n/2$, in the sense that $P(X=n/2+j)=P(X=n/2-j)$ for all nonnegative integers $j$.

###### Proof.

By Theorem 3.3.7, $n-X$ is also $\mathrm{Bin}(n,1/2)$, so

$P(X=k)=P(n-X=k)=P(X=n-k)$

for all nonnegative integers $k$. Letting $k=n/2+j$, the desired result follows. This explains why the $\mathrm{Bin}(10,1/2)$ PMF is symmetric about $5$ in Figure 3.6. ∎

###### Example 3.3.9 (Coin tosses continued).

Going back to Example 3.1.2, we now know that $X\sim\mathrm{Bin}(2,1/2)$, $Y\sim\mathrm{Bin}(2,1/2)$, and $I\sim\mathrm{Bern}(1/2)$. Consistent with Theorem 3.3.7, $X$ and $Y=2-X$ have the same distribution, and consistent with Corollary 3.3.8, the distribution of $X$ (and of $Y$) is symmetric about $1$. ∎

### 3.4 Hypergeometric

If we have an urn filled with $w$ white and $b$ black balls, then drawing $n$ balls out of the urn *with replacement* yields a $\mathrm{Bin}(n,w/(w+b))$ distribution for the number of white balls obtained in $n$ trials, since the draws are independent Bernoulli trials, each with probability $w/(w+b)$ of success. If we instead sample *without replacement*, as illustrated in Figure 3.7, then the number of white balls follows a *Hypergeometric distribution*.

###### Story 3.4.1 (Hypergeometric distribution).

Consider an urn with $w$ white balls and $b$ black balls. We draw $n$ balls out of the urn at random without replacement, such that all ${w+b\choose n}$ samples are equally likely. Let $X$ be the number of white balls in the sample. Then $X$ is said to have the *Hypergeometric distribution* with parameters $w$, $b$, and $n$; we denote this by $X\sim\mathrm{HGeom}(w,b,n)$. ∎