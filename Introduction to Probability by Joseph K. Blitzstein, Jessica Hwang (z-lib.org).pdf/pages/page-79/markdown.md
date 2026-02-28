(b) Now suppose that all $n$ judges vote to convict. Given this information, find the probability that the suspect is guilty.

(c) Is the answer to (b), viewed as a function of $n$, an increasing function? Give a short, intuitive explanation in words.

Solution:

(a) Since $k<n$, a systemic error didn’t occur. We will implicitly condition on this in this part. Let $G$ be the event that the suspect is guilty and $X$ be the number of judges who vote to convict. Using Bayes’ rule, LOTP, and the Binomial PMF,

$P(G|X=k)=\frac{P(X=k|G)P(G)}{P(X=k)}=\frac{pc^{k}(1-c)^{n-k}}{pc^{k}(1-c)^{n-k}+(1-p)w^{k}(1-w)^{n-k}}.$

(b) Let $U$ be the event $X=n$ and $B$ be the event that a systemic error occurs. Then

$P(G|U)=\frac{P(U|G)P(G)}{P(U)}=\frac{pP(U|G)}{pP(U|G)+(1-p)P(U|G^{c})}.$

By LOTP with extra conditioning,

$P(U|G)$ $=P(U|G,B)P(B|G)+P(U|G,B^{c})P(B^{c}|G)=s+(1-s)c^{n},$
$P(U|G^{c})$ $=P(U|G^{c},B)P(B|G^{c})+P(U|G^{c},B^{c})P(B^{c}|G^{c})=s+(1-s)w^{n}.$

Thus,

$P(G|U)=\frac{p(s+(1-s)c^{n})}{p(s+(1-s)c^{n})+(1-p)(s+(1-s)w^{n})}.$

(c) No, since a large value of $n$ yields a high chance of systemic error, and if a systemic error occurs then the judges’ votes are uninformative about whether the suspect is guilty. The answer to (b) reverts to the prior probability $p$ as $n\to\infty$. ∎

We often want to condition on more than one piece of information, and we now have several ways of doing that. For example, here are some approaches for finding $P(A|B,C)$:

1. We can think of $B,C$ as the single event $B\cap C$ and use the definition of conditional probability to get

$P(A|B,C)=\frac{P(A,B,C)}{P(B,C)}.$

This is a natural approach if it’s easiest to think about $B$ and $C$ in tandem. We can then try to evaluate the numerator and denominator. For example, we can use LOTP in both the numerator and the denominator, or we can write the numerator as $P(B,C|A)P(A)$ (which would give us a version of Bayes’ rule) and use LOTP to help with the denominator.

2. We can use Bayes’ rule with extra conditioning on $C$ to get

$P(A|B,C)=\frac{P(B|A,C)P(A|C)}{P(B|C)}.$