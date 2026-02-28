Finally, if we multiply both sides by $pq$, we recover the original sum we wanted to find:

$E(X)=\sum_{k=0}^{\infty}kq^{k}p=pq\sum_{k=0}^{\infty}kq^{k-1}=pq\frac{1}{(1-q)^{2}}=\frac{q}{p}.$

In Example 9.1.8, we will give a story proof of the same result, based on first-step analysis: condition on the result of the first trial in the story interpretation of $X$. If the first trial is a success, we know $X=0$ and if it’s a failure, we have one wasted trial and then are back where we started. ∎

###### Example 4.3.7 (First Success expectation).

Since we can write $Y\sim\text{FS}(p)$ as $Y=X+1$ where $X\sim\text{Geom}(p)$, we have

$E(Y)=E(X+1)=\frac{q}{p}+1=\frac{1}{p}.\qed$

The Negative Binomial distribution generalizes the Geometric distribution: instead of waiting for just one success, we can wait for any predetermined number $r$ of successes.

###### Story 4.3.8 (Negative Binomial distribution).

In a sequence of independent Bernoulli trials with success probability $p$, if $X$ is the number of *failures* before the $r$th success, then $X$ is said to have the *Negative Binomial distribution* with parameters $r$ and $p$, denoted $X\sim\text{NBin}(r,p)$. ∎

Both the Binomial and the Negative Binomial distributions are based on independent Bernoulli trials; they differ in the *stopping rule* and in what they are counting. The Binomial counts the number of successes in a fixed number of *trials*; the Negative Binomial counts the number of failures until a fixed number of *successes*.

In light of these similarities, it comes as no surprise that the derivation of the Negative Binomial PMF bears a resemblance to the corresponding derivation for the Binomial.

###### Theorem 4.3.9 (Negative Binomial PMF).

If $X\sim\text{NBin}(r,p)$, then the PMF of $X$ is

$P(X=n)=\binom{n+r-1}{r-1}p^{r}q^{n}$

for $n=0,1,2\ldots$, where $q=1-p$.

###### Proof.

Imagine a string of 0’s and 1’s, with 1’s representing successes. The probability of any *specific* string of $n$ 0’s and $r$ 1’s is $p^{r}q^{n}$. How many such strings are there? Because we stop as soon as we hit the $r$th success, the string must terminate in a 1. Among the other $n+r-1$ positions, we choose $r-1$ places for the remaining 1’s to go. So the overall probability of exactly $n$ failures before the $r$th success is

$P(X=n)=\binom{n+r-1}{r-1}p^{r}q^{n},\quad n=0,1,2,\ldots.$