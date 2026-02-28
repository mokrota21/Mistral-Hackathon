number of successes in a particular region or interval of time, and there are a large number of trials, each with a small probability of success. For example, the following random variables could follow a distribution that is approximately Poisson.
- The number of emails you receive in an hour. There are a lot of people who could potentially email you in that hour, but it is unlikely that any specific person will actually email you in that hour. Alternatively, imagine subdividing the hour into milliseconds. There are $3.6\times 10^{6}$ seconds in an hour, but in any specific millisecond it is unlikely that you will get an email.
- The number of chips in a chocolate chip cookie. Imagine subdividing the cookie into small cubes; the probability of getting a chocolate chip in a single cube is small, but the number of cubes is large.
- The number of earthquakes in a year in some region of the world. At any given time and location, the probability of an earthquake is small, but there are a large number of possible times and locations for earthquakes to occur over the course of the year.

The parameter $\lambda$ is interpreted as the *rate* of occurrence of these rare events; in the examples above, $\lambda$ could be 20 (emails per hour), 10 (chips per cookie), and 2 (earthquakes per year). The *Poisson paradigm* says that in applications similar to the ones above, we can approximate the distribution of the number of events that occur by a Poisson distribution.

###### Approximation 4.7.3 (Poisson paradigm).

Let $A_{1},\ldots,A_{n}$ be events with $p_{j}=P(A_{j})$, where $n$ is large, the $p_{j}$ are small, and the $A_{j}$ are independent or weakly dependent. Let

$X=\sum_{j=1}^{n}I(A_{j})$

count how many of the $A_{j}$ occur. Then $X$ is approximately distributed as $\mathrm{Pois}(\lambda)$, with $\lambda=\sum_{j=1}^{n}p_{j}$.

Proving that the above approximation is good is difficult, and would require first giving precise definitions of weak dependence (there are various ways to measure dependence of r.v.s) and of good approximations (there are various ways to measure how good an approximation is). A remarkable theorem is that if the $A_{j}$ are independent, $N\sim\mathrm{Pois}(\lambda)$, and $B$ is any set of nonnegative integers, then

$|P(X\in B)-P(N\in B)|\leq\min\left(1,\frac{1}{\lambda}\right)\sum_{j=1}^{n}p_{j}^{2}.$

This gives an upper bound on how much error is incurred from using a Poisson approximation. It also makes more precise how small the $p_{j}$ should be: we want $\sum_{j=1}^{n}p_{j}^{2}$ to be very small, or at least very small compared to $\lambda$. The result can be shown using an advanced technique known as the *Stein-Chen method*.