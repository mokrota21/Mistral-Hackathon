Introduction to Probability

The last step used the binomial theorem. Since we've arrived at the  $\mathrm{Pois}(\lambda_1 + \lambda_2)$  PMF, we have  $X + Y\sim \mathrm{Pois}(\lambda_1 + \lambda_2)$ .

The story of the Poisson distribution provides intuition for this result. If there are two different types of events occurring at rates  $\lambda_{1}$  and  $\lambda_{2}$ , independently, then the overall event rate is  $\lambda_{1} + \lambda_{2}$ .

Theorem 4.8.2 (Poisson given a sum of Poissons). If  $X \sim \operatorname{Pois}(\lambda_1)$ ,  $Y \sim \operatorname{Pois}(\lambda_2)$ , and  $X$  is independent of  $Y$ , then the conditional distribution of  $X$  given  $X + Y = n$  is  $\operatorname{Bin}(n, \lambda_1 / (\lambda_1 + \lambda_2))$ .

Proof. Exactly as in the corresponding proof for the Binomial and Hypergeometric, we use Bayes' rule to compute the conditional PMF  $P(X = k|X + Y = n)$ :

$$
\begin{array}{l} P (X = k | X + Y = n) = \frac {P (X + Y = n | X = k) P (X = k)}{P (X + Y = n)} \\ = \frac {P (Y = n - k) P (X = k)}{P (X + Y = n)}. \\ \end{array}
$$

Now we plug in the PMFs of  $X$ ,  $Y$ , and  $X + Y$ ; the last of these is distributed  $\mathrm{Pois}(\lambda_1 + \lambda_2)$  by the previous theorem. This gives

$$
\begin{array}{l} P (X = k | X + Y = n) = \frac {\left(\frac {e ^ {- \lambda_ {2}} \lambda_ {2} ^ {n - k}}{(n - k) !}\right) \left(\frac {e ^ {- \lambda_ {1}} \lambda_ {1} ^ {k}}{k !}\right)}{\frac {e ^ {- (\lambda_ {1} + \lambda_ {2})} (\lambda_ {1} + \lambda_ {2}) ^ {n}}{n !}} \\ = \binom {n} {k} \frac {\lambda_ {1} ^ {k} \lambda_ {2} ^ {n - k}}{(\lambda_ {1} + \lambda_ {2}) ^ {n}} \\ = \binom {n} {k} \left(\frac {\lambda_ {1}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {k} \left(\frac {\lambda_ {2}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {n - k}, \\ \end{array}
$$

which is the  $\mathrm{Bin}(n,\lambda_1 / (\lambda_1 + \lambda_2))$  PMF, as desired.

Conversely, if we take the limit of the  $\operatorname{Bin}(n,p)$  distribution as  $n\to \infty$  and  $p\rightarrow 0$  with  $np$  fixed, we arrive at a Poisson distribution. This provides the basis for the Poisson approximation to the Binomial distribution.

Theorem 4.8.3 (Poisson approximation to Binomial). If  $X \sim \operatorname{Bin}(n, p)$  and we let  $n \to \infty$  and  $p \to 0$  such that  $\lambda = np$  remains fixed, then the PMF of  $X$  converges to the  $\operatorname{Pois}(\lambda)$  PMF. More generally, the same conclusion holds if  $n \to \infty$  and  $p \to 0$  in such a way that  $np$  converges to a constant  $\lambda$ .

This is a special case of the Poisson paradigm, where the  $A_{j}$  are independent with the same probabilities, so that  $\sum_{j=1}^{n} I(A_{j})$  has a Binomial distribution. In this special case, we can prove that the Poisson approximation makes sense just by taking a limit of the Binomial PMF.