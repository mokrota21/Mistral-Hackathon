Expectation

Proof. We will prove this for the case that $\lambda = np$ is fixed while $n\to \infty$ and $p\rightarrow 0$, by showing that the $\operatorname {Bin}(n,p)$ PMF converges to the $\mathrm{Pois}(\lambda)$ PMF. For $0\leq k\leq n$

$$
\begin{array}{l}
P (X = k) = \binom {n} {k} p ^ {k} (1 - p) ^ {n - k} \\
= \frac {n (n - 1) \dots (n - k + 1)}{k !} \left(\frac {\lambda}{n}\right) ^ {k} \left(1 - \frac {\lambda}{n}\right) ^ {n} \left(1 - \frac {\lambda}{n}\right) ^ {- k} \\
= \frac {\lambda^ {k}}{k !} \frac {n (n - 1) \dots (n - k + 1)}{n ^ {k}} \left(1 - \frac {\lambda}{n}\right) ^ {n} \left(1 - \frac {\lambda}{n}\right) ^ {- k}.
\end{array}
$$

Letting $n\to \infty$ with $k$ fixed,

$$
\begin{array}{l}
\frac {n (n - 1) \dots (n - k + 1)}{n ^ {k}} \rightarrow 1, \\
\left(1 - \frac {\lambda}{n}\right) ^ {n} \rightarrow e ^ {- \lambda}, \\
\left(1 - \frac {\lambda}{n}\right) ^ {- k} \rightarrow 1,
\end{array}
$$

where the $e^{-\lambda}$ comes from the compound interest formula from Section A.2.5 of the math appendix. So

$$
P (X = k) \rightarrow \frac {e ^ {- \lambda} \lambda^ {k}}{k !},
$$

which is the $\operatorname{Pois}(\lambda)$ PMF.

This theorem implies that if $n$ is large, $p$ is small, and $np$ is moderate, we can approximate the $\operatorname{Bin}(n,p)$ PMF by the $\operatorname{Pois}(np)$ PMF. The main thing that matters here is that $p$ should be small; in fact, the result mentioned after the statement of the Poisson paradigm says in this case that the error in approximating $P(X \in B) \approx P(N \in B)$ for $X \sim \operatorname{Bin}(n,p), N \sim \operatorname{Pois}(np)$ is at most $\min(p, np^2)$.

Example 4.8.4 (Visitors to a website). The owner of a certain website is studying the distribution of the number of visitors to the site. Every day, a million people independently decide whether to visit the site, with probability $p = 2 \times 10^{-6}$ of visiting. Give a good approximation for the probability of getting at least three visitors on a particular day.

Solution:

Let $X \sim \operatorname{Bin}(n, p)$ be the number of visitors, where $n = 10^6$. It is easy to run into computational difficulties or numerical errors in exact calculations with this distribution since $n$ is so large and $p$ is so small. But since $n$ is large, $p$ is small, and $np = 2$ is moderate, $\operatorname{Pois}(2)$ is a good approximation. This gives

$$
P (X \geq 3) = 1 - P (X &lt; 3) \approx 1 - e ^ {- 2} - e ^ {- 2} \cdot 2 - e ^ {- 2} \cdot \frac {2 ^ {2}}{2 !} = 1 - 5 e ^ {- 2} \approx 0. 3 2 3 3,
$$

which turns out to be extremely accurate.