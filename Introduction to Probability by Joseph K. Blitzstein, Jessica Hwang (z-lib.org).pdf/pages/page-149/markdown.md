Introduction to Probability

In the second line, we used the independence of $X$ and $Y$ to justify dropping the conditioning in

$P(X+Y=k|X=j)=P(Y=k-j|X=j)=P(Y=k-j),$

and in the last line, we used the fact that

$\sum_{j=0}^{k}{m\choose k-j}{n\choose j}={n+m\choose k}$

by Vandermonde’s identity. The resulting expression is the Bin$(n+m,p)$ PMF, so $X+Y\sim$ Bin$(n+m,p)$.

2. Representation: A much simpler proof is to represent both $X$ and $Y$ as the sum of i.i.d. Bern$(p)$ r.v.s: $X=X_{1}+\cdots+X_{n}$ and $Y=Y_{1}+\cdots+Y_{m}$, where the $X_{i}$ and $Y_{j}$ are all i.i.d. Bern$(p)$. Then $X+Y$ is the sum of $n+m$ i.i.d. Bern$(p)$ r.v.s, so its distribution, by the previous theorem, is Bin$(n+m,p)$.

3. Story: By the Binomial story, $X$ is the number of successes in $n$ independent trials and $Y$ is the number of successes in $m$ additional independent trials, all with the same success probability, so $X+Y$ is the total number of successes in the $n+m$ trials, which is the story of the Bin$(n+m,p)$ distribution.

Of course, if we have a definition for independence of r.v.s, we should have an analogous definition for conditional independence of r.v.s.

###### Definition 3.8.10 (Conditional independence of r.v.s).

Random variables $X$ and $Y$ are *conditionally independent* given an r.v. $Z$ if for all $x,y\in\mathbb{R}$ and all $z$ in the support of $Z$,

$P(X\leq x,Y\leq y|Z=z)=P(X\leq x|Z=z)P(Y\leq y|Z=z).$

For discrete r.v.s, an equivalent definition is to require

$P(X=x,Y=y|Z=z)=P(X=x|Z=z)P(Y=y|Z=z).$

As we might expect from the name, this is the definition of independence, except that we condition on $Z=z$ everywhere, and require the equality to hold for all $z$ in the support of $Z$.

###### Definition 3.8.11 (Conditional PMF).

For any discrete r.v.s $X$ and $Z$, the function $P(X=x|Z=z)$, when considered as a function of $x$ for fixed $z$, is called the *conditional PMF of $X$ given $Z=z$*.

Independence of r.v.s does not imply conditional independence, nor vice versa. First let us show why independence does not imply conditional independence.