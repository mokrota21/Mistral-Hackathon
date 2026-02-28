Just as a Binomial r.v. can be represented as a sum of i.i.d. Bernoullis, a Negative Binomial r.v. can be represented as a sum of i.i.d. Geometrics.

###### Theorem 4.3.10.

Let $X\sim\text{NBin}(r,p)$, viewed as the number of failures before the $r$th success in a sequence of independent Bernoulli trials with success probability $p$. Then we can write $X=X_{1}+\cdots+X_{r}$ where the $X_{i}$ are i.i.d. $\text{Geom}(p)$.

###### Proof.

Let $X_{1}$ be the number of failures until the first success, $X_{2}$ be the number of failures between the first success and the second success, and in general, $X_{i}$ be the number of failures between the $(i-1)$st success and the $i$th success.

Then $X_{1}\sim\text{Geom}(p)$ by the story of the Geometric distribution. After the first success, the number of additional failures until the next success is still Geometric! So $X_{2}\sim\text{Geom}(p)$, and similarly for all the $X_{i}$. Furthermore, the $X_{i}$ are independent because the trials are all independent of each other. Adding the $X_{i}$, we get the total number of failures before the $r$th success, which is $X$. ∎

Using linearity, the expectation of the Negative Binomial now follows without any additional calculations.

###### Example 4.3.11 (Negative Binomial expectation).

Let $X\sim\text{NBin}(r,p)$. By the previous theorem, we can write $X=X_{1}+\cdots+X_{r}$, where the $X_{i}$ are i.i.d. $\text{Geom}(p)$. By linearity,

$E(X)=E(X_{1})+\cdots+E(X_{r})=r\cdot\frac{q}{p}.\qed$

The next example is a famous problem in probability and an instructive application of the Geometric and First Success distributions. It is usually stated as a problem about collecting coupons, hence its name, but we’ll use toys instead of coupons.

###### Example 4.3.12 (Coupon collector).

Suppose there are $n$ types of toys, which you are collecting one by one, with the goal of getting a complete set. When collecting toys, the toy types are random (as is sometimes the case, for example, with toys included in cereal boxes or included with kids’ meals from a fast food restaurant). Assume that each time you collect a toy, it is equally likely to be any of the $n$ types. What is the expected number of toys needed until you have a complete set?

*Solution*:

Let $N$ be the number of toys needed; we want to find $E(N)$. Our strategy will be to break up $N$ into a sum of simpler r.v.s so that we can apply linearity. So write

$N=N_{1}+N_{2}+\cdots+N_{n},$

where $N_{1}$ is the number of toys until the first toy type you haven’t seen before (which is always $1$, as the first toy is always a new type), $N_{2}$ is the additional number of toys until the second toy type you haven’t seen before, and so forth. Figure 6 illustrates these definitions with $n=3$ toy types.