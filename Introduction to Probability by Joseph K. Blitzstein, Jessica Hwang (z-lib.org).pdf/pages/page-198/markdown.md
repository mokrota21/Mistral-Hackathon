The command pbirthday(1600, classes = 8760, coincident=4) in R gives that the correct answer is 0.296. So Method 2 is more accurate than Method 1.

An intuitive explanation for why Method 1 is less accurate is that there is a more substantial dependence in the indicators in that method. For example, being given that sophomores 1, 2, 3, 4 share the same birth day-hour greatly increases the chance that sophomores 1, 2, 3, 5 share the same birth day-hour. In contrast, knowing that at least 4 sophomores were born on a specific day-hour provides very little information about whether at least 4 were born on a different specific day-hour. ∎

### 4.8 Connections between Poisson and Binomial

The Poisson and Binomial distributions are closely connected, and their relationship is exactly parallel to the relationship between the Binomial and Hypergeometric distributions that we examined in the previous chapter: we can get from the Poisson to the Binomial by *conditioning*, and we can get from the Binomial to the Poisson by *taking a limit*.

Our results will rely on the fact that the sum of independent Poissons is Poisson, just as the sum of independent Binomials is Binomial. We’ll prove this result using the law of total probability for now; in Chapter 6 we’ll learn a faster method that uses a tool called the moment generating function. Chapter 13 gives further insight into these results.

###### Theorem 4.8.1 (Sum of independent Poissons).

If $X\sim\mathrm{Pois}(\lambda_{1})$, $Y\sim\mathrm{Pois}(\lambda_{2})$, and $X$ is independent of $Y$, then $X+Y\sim\mathrm{Pois}(\lambda_{1}+\lambda_{2})$.

###### Proof.

To get the PMF of $X+Y$, condition on $X$ and use the law of total probability:

$P(X+Y=k)$ $=\sum_{j=0}^{k}P(X+Y=k|X=j)P(X=j)$
$=\sum_{j=0}^{k}P(Y=k-j)P(X=j)$
$=\sum_{j=0}^{k}\frac{e^{-\lambda_{2}}\lambda_{2}^{k-j}}{(k-j)!}\frac{e^{-\lambda_{1}}\lambda_{1}^{j}}{j!}$
$=\frac{e^{-(\lambda_{1}+\lambda_{2})}}{k!}\sum_{j=0}^{k}\binom{k}{j}\lambda_{1}^{j}\lambda_{2}^{k-j}$
$=\frac{e^{-(\lambda_{1}+\lambda_{2})}(\lambda_{1}+\lambda_{2})^{k}}{k!}.$