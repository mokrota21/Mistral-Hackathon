Random variables and their distributions

- dependent and identically distributed. Let $X$ be the number of Heads in $n$ independent fair coin tosses, and let $Y$ be the number of Tails in those same $n$ tosses. Then $X$ and $Y$ are both distributed $\operatorname{Bin}(n, 1/2)$, but they are highly dependent: if we know $X$, then we know $Y$ perfectly.
- dependent and not identically distributed. Let $X$ be the indicator of whether the majority party retains control of the House of Representatives in the U.S. after the next election, and let $Y$ be the average favorability rating of the majority party in polls taken within a month of the election. Then $X$ and $Y$ are dependent, and $X$ and $Y$ do not have the same distribution.

By taking a sum of i.i.d. Bernoulli r.v.s, we can write down the story of the Binomial distribution in an algebraic form.

Theorem 3.8.8. If $X \sim \operatorname{Bin}(n, p)$, viewed as the number of successes in $n$ independent Bernoulli trials with success probability $p$, then we can write $X = X_{1} + \dots + X_{n}$ where the $X_{i}$ are i.i.d. $\operatorname{Bern}(p)$.

Proof. Let $X_{i} = 1$ if the $i$th trial was a success, and 0 if the $i$th trial was a failure. It's as though we have a person assigned to each trial, and we ask each person to raise their hand if their trial was a success. If we count the number of raised hands (which is the same as adding up the $X_{i}$), we get the total number of successes.

An important fact about the Binomial distribution is that the sum of independent Binomial r.v.s with the same success probability is also Binomial.

Theorem 3.8.9. If $X \sim \operatorname{Bin}(n, p)$, $Y \sim \operatorname{Bin}(m, p)$, and $X$ is independent of $Y$, then $X + Y \sim \operatorname{Bin}(n + m, p)$.

Proof. We present three proofs, since each illustrates a useful technique.

1. LOTP: We can directly find the PMF of $X + Y$ by conditioning on $X$ (or $Y$, whichever we prefer) and using the law of total probability:

$$
\begin{array}{l}
P (X + Y = k) = \sum_ {j = 0} ^ {k} P (X + Y = k | X = j) P (X = j) \\
= \sum_ {j = 0} ^ {k} P (Y = k - j) P (X = j) \\
= \sum_ {j = 0} ^ {k} \binom {m} {k - j} p ^ {k - j} q ^ {m - k + j} \binom {n} {j} p ^ {j} q ^ {n - j} \\
= p ^ {k} q ^ {n + m - k} \sum_ {j = 0} ^ {k} \binom {m} {k - j} \binom {n} {j} \\
= \binom {n + m} {k} p ^ {k} q ^ {n + m - k}.
\end{array}
$$