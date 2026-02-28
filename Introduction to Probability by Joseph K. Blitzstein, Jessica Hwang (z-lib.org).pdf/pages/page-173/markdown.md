Linearity is an extremely handy tool for calculating expected values, often allowing us to bypass the definition of expected value altogether. Let’s use linearity to find the expectations of the Binomial and Hypergeometric distributions.

###### Example 4.2.2 (Binomial expectation).

For $X\sim\text{Bin}(n,p)$, let’s find $E(X)$ in two ways. By definition of expectation,

$E(X)=\sum_{k=0}^{n}kP(X=k)=\sum_{k=0}^{n}k\binom{n}{k}p^{k}q^{n-k}.$

From Example 1.5.2, we know $k\binom{n}{k}=n\binom{n-1}{k-1}$, so

$\sum_{k=0}^{n}k\binom{n}{k}p^{k}q^{n-k}$ $=n\sum_{k=0}^{n}\binom{n-1}{k-1}p^{k}q^{n-k}$
$=np\sum_{k=1}^{n}\binom{n-1}{k-1}p^{k-1}q^{n-k}$
$=np\sum_{j=0}^{n-1}\binom{n-1}{j}p^{j}q^{n-1-j}$
$=np.$

The sum in the penultimate line equals $1$ because it is the sum of the $\text{Bin}(n-1,p)$ PMF (or by the binomial theorem). Therefore, $E(X)=np$.

This proof required us to remember combinatorial identities and manipulate binomial coefficients. Using linearity of expectation, we obtain a *much* shorter path to the same result. Let’s write $X$ as the sum of $n$ independent $\text{Bern}(p)$ r.v.s:

$X=I_{1}+\cdots+I_{n},$

where each $I_{j}$ has expectation $E(I_{j})=1p+0q=p$. By linearity,

$E(X)=E(I_{1})+\cdots+E(I_{n})=np.\qed$

###### Example 4.2.3 (Hypergeometric expectation).

Let $X\sim\text{HGeom}(w,b,n)$, interpreted as the number of white balls in a sample of size $n$ drawn without replacement from an urn with $w$ white and $b$ black balls. As in the Binomial case, we can write $X$ as a sum of Bernoulli random variables,

$X=I_{1}+\cdots+I_{n},$

where $I_{j}$ equals $1$ if the $j$th ball in the sample is white and $0$ otherwise. By symmetry, $I_{j}\sim\text{Bern}(p)$ with $p=w/(w+b)$, since unconditionally the $j$th ball drawn is equally likely to be any of the balls.

Unlike in the Binomial case, the $I_{j}$ are not independent, since the sampling is without replacement: given that a ball in the sample is white, there is a lower