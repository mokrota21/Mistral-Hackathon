Random variables and their distributions

interested in the distribution of the number of tagged elk in the recaptured sample. By analogy, think of women as tagged elk and men as untagged elk. Instead of recapturing  $r$  elk at random from the forest, we infect  $X + Y = r$  people with the disease; under the null hypothesis, the set of diseased people is equally likely to be any set of  $r$  people. Thus, conditional on  $X + Y = r$ ,  $X$  represents the number of women among the  $r$  diseased individuals. This is exactly analogous to the number of tagged elk in the recaptured sample, which is distributed  $\mathrm{HGeom}(n,m,r)$ .

An interesting fact, which turns out to be useful in statistics, is that the conditional distribution of  $X$  does not depend on  $p$ : unconditionally,  $X \sim \operatorname{Bin}(n,p)$ , but  $p$  disappears from the parameters of the conditional distribution! This makes sense upon reflection, since once we know  $X + Y = r$ , we can work directly with the fact that we have a population with  $r$  diseased and  $n + m - r$  healthy people, without worrying about the value of  $p$  that originally generated the population.

This motivating example serves as a proof of the following theorem.

Theorem 3.9.2. If  $X \sim \operatorname{Bin}(n,p)$ ,  $Y \sim \operatorname{Bin}(m,p)$ , and  $X$  is independent of  $Y$ , then the conditional distribution of  $X$  given  $X + Y = r$  is  $\mathrm{HGeom}(n,m,r)$ .

In the other direction, the Binomial is a limiting case of the Hypergeometric.

Theorem 3.9.3. If  $X \sim \mathrm{HGeom}(w, b, n)$  and  $N = w + b \to \infty$  such that  $p = w / (w + b)$  remains fixed, then the PMF of  $X$  converges to the  $\operatorname{Bin}(n, p)$  PMF.

Proof. We take the stated limit of the  $\mathrm{HGeom}(w,b,n)$  PMF:

$$
\begin{array}{l} P (X = k) = \frac {\binom {w} {k} \binom {b} {n - k}}{\binom {w + b} {n}} \\ = \binom {n} {k} \frac {\binom {w + b - n} {w - k}}{\binom {w + b} {w}} \quad \text {by Theorem 3.4.5} \\ = \binom {n} {k} \frac {w !}{(w - k) !} \frac {b !}{(b - n + k) !} \frac {(w + b - n) !}{(w + b) !} \\ = \binom {n} {k} \frac {w (w - 1) \dots (w - k + 1) b (b - 1) \dots (b - n + k + 1)}{(w + b) (w + b - 1) \dots (w + b - n + 1)} \\ = \binom {n} {k} \frac {p \left(p - \frac {1}{N}\right) \dots \left(p - \frac {k - 1}{N}\right) q \left(q - \frac {1}{N}\right) \dots \left(q - \frac {n - k - 1}{N}\right)}{\left(1 - \frac {1}{N}\right) \left(1 - \frac {2}{N}\right) \dots \left(1 - \frac {n - 1}{N}\right)}. \\ \end{array}
$$

As  $N\to \infty$  , the denominator goes to 1, and the numerator goes to  $p^k q^{n - k}$  . Thus

$$
P (X = k) \to \left( \begin{array}{c} n \\ k \end{array} \right) p ^ {k} q ^ {n - k},
$$

which is the  $\operatorname{Bin}(n,p)$  PMF.

The stories of the Binomial and Hypergeometric provide intuition for this result: given an urn with  $w$  white balls and  $b$  black balls, the Binomial distribution arises