the second set of tags. Both $X$ and $Y$ count the number of white sampled balls, so they have the same distribution.

Alternatively, we can check algebraically that $X$ and $Y$ have the same PMF:

$P(X=k)=\frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}=\frac{w!b!n!(w+b-n)!}{k!(w+b)!(w-k)!(n-k)!(b-n+k)!},$
$P(Y=k)=\frac{\binom{n}{k}\binom{w+b-n}{w-k}}{\binom{w+b}{w}}=\frac{w!b!n!(w+b-n)!}{k!(w+b)!(w-k)!(n-k)!(b-n+k)!}.$

We prefer the story proof because it is less tedious and more memorable. $\blacksquare$

#### 3.4.6 (Binomial vs. Hypergeometric).

The Binomial and Hypergeometric distributions are often confused. Both are discrete distributions taking on integer values between $0$ and $n$ for some $n$, and both can be interpreted as the number of successes in $n$ Bernoulli trials (for the Hypergeometric, each tagged elk in the recaptured sample can be considered a success and each untagged elk a failure). However, a crucial part of the Binomial story is that the Bernoulli trials involved are independent. The Bernoulli trials in the Hypergeometric story are dependent, since the sampling is done without replacement: knowing that one elk in our sample is tagged decreases the probability that the second elk will also be tagged.

### 3.5 Discrete Uniform

A very simple story, closely connected to the naive definition of probability, describes picking a random number from some finite set of possibilities.

###### Story 3.5.1 (Discrete Uniform distribution).

Let $C$ be a finite, nonempty set of numbers. Choose one of these numbers uniformly at random (i.e., all values in $C$ are equally likely). Call the chosen number $X$. Then $X$ is said to have the Discrete Uniform distribution with parameter $C$; we denote this by $X\sim\text{DUnif}(C)$. $\square$

The PMF of $X\sim\text{DUnif}(C)$ is

$P(X=x)=\frac{1}{|C|}$

for $x\in C$ (and $0$ otherwise), since a PMF must sum to $1$. As with questions based on the naive definition of probability, questions based on a Discrete Uniform distribution reduce to counting problems. Specifically, for $X\sim\text{DUnif}(C)$ and any $A\subseteq C$, we have

$P(X\in A)=\frac{|A|}{|C|}.$