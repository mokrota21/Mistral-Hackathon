###### Definition 4.7.1 (Poisson distribution).

An r.v. $X$ has the Poisson distribution with parameter $\lambda$, where $\lambda>0$, if the PMF of $X$ is

$P(X=k)=\frac{e^{-\lambda}\lambda^{k}}{k!},\quad k=0,1,2,\ldots.$

We write this as $X\sim\text{Pois}(\lambda)$.

This is a valid PMF because of the Taylor series $\sum_{k=0}^{\infty}\frac{\lambda^{k}}{k!}=e^{\lambda}$.

###### Example 4.7.2 (Poisson expectation and variance).

Let $X\sim\text{Pois}(\lambda)$. We will show that the mean and variance are both equal to $\lambda$. For the mean, we have

$E(X)$ $=e^{-\lambda}\sum_{k=0}^{\infty}k\frac{\lambda^{k}}{k!}$
$=e^{-\lambda}\sum_{k=1}^{\infty}k\frac{\lambda^{k}}{k!}$
$=\lambda e^{-\lambda}\sum_{k=1}^{\infty}\frac{\lambda^{k-1}}{(k-1)!}$
$=\lambda e^{-\lambda}e^{\lambda}=\lambda.$

First we dropped the $k=0$ term because it was $0$. Then we took a $\lambda$ out of the sum so that what was left inside was just the Taylor series for $e^{\lambda}$.

To get the variance, we first find $E(X^{2})$. By LOTUS,

$E(X^{2})=\sum_{k=0}^{\infty}k^{2}P(X=k)=e^{-\lambda}\sum_{k=0}^{\infty}k^{2}\frac{\lambda^{k}}{k!}.$

From here, the derivation is very similar to that of the variance of the Geometric. Differentiate the familiar series

$\sum_{k=0}^{\infty}\frac{\lambda^{k}}{k!}=e^{\lambda}$

with respect to $\lambda$ and replenish:

$\sum_{k=1}^{\infty}k\frac{\lambda^{k-1}}{k!}=e^{\lambda},$
$\sum_{k=1}^{\infty}k\frac{\lambda^{k}}{k!}=\lambda e^{\lambda}.$

Rinse and repeat:

$\sum_{k=1}^{\infty}k^{2}\frac{\lambda^{k-1}}{k!}=e^{\lambda}+\lambda e^{\lambda}=e^{\lambda}(1+\lambda),$
$\sum_{k=1}^{\infty}k^{2}\frac{\lambda^{k}}{k!}=e^{\lambda}\lambda(1+\lambda).$