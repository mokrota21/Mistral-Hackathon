The square root of the variance is called the *standard deviation* (SD):

$\mathrm{SD}(X)=\sqrt{\mathrm{Var}(X)}.$

Recall that when we write $E(X-EX)^{2}$, we mean the expectation of the random variable $(X-EX)^{2}$, *not* $(E(X-EX))^{2}$ (which is 0 by linearity).

The variance of $X$ measures how far $X$ is from its mean on average, but instead of simply taking the average difference between $X$ and its mean $EX$, we take the average *squared* difference. To see why, note that the average deviation from the mean, $E(X-EX)$, always equals 0 by linearity; positive and negative deviations cancel each other out. By squaring the deviations, we ensure that both positive and negative deviations contribute to the overall variability. However, because variance is an average squared distance, it has the wrong units: if $X$ is in dollars, $\mathrm{Var}(X)$ is in squared dollars. To get back to our original units, we take the square root; this gives us the standard deviation.

One might wonder why variance isn’t defined as $E|X-EX|$, which would achieve the goal of counting both positive and negative deviations while maintaining the same units as $X$. This measure of variability isn’t nearly as popular as $E(X-EX)^{2}$, for a variety of reasons. Most notably, the absolute value function isn’t differentiable at 0, whereas the squaring function is differentiable everywhere and is central in various fundamental mathematical results such as the Pythagorean theorem.

An equivalent expression for variance is $\mathrm{Var}(X)=E(X^{2})-(EX)^{2}$. This formula is often easier to work with when doing actual calculations. Since this is the variance formula we will use over and over again, we state it as its own theorem.

###### Theorem 4.6.2.

For any r.v. $X$,

$\mathrm{Var}(X)=E(X^{2})-(EX)^{2}.$

###### Proof.

Let $\mu=EX$. Expanding $(X-\mu)^{2}$ and using linearity, the variance of $X$ is

$E(X-\mu)^{2}=E(X^{2}-2\mu X+\mu^{2})=E(X^{2})-2\mu EX+\mu^{2}=E(X^{2})-\mu^{2}.\qed$

Variance has the following properties. The first two are easily verified from the definition, the third will be addressed in a later chapter, and the last one is proven just after stating it.

- $\mathrm{Var}(X+c)=\mathrm{Var}(X)$ for any constant $c$. Intuitively, if we shift a distribution to the left or right, that should affect the center of mass of the distribution but not its spread.
- $\mathrm{Var}(cX)=c^{2}\mathrm{Var}(X)$ for any constant $c$.
- If $X$ and $Y$ are independent, then $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$. We prove this and discuss it more in Chapter 7. This is not true in general if $X$ and $Y$ are dependent. For example, in the extreme case where $X$ always equals $Y$, we have

$\mathrm{Var}(X+Y)=\mathrm{Var}(2X)=4\mathrm{Var}(X)>2\mathrm{Var}(X)=\mathrm{Var}(X)+\mathrm{Var}(Y)$