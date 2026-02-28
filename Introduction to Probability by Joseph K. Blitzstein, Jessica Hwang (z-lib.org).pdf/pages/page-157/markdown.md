Next, we use sample. Here’s how to get 100 draws from the PMF above:

```
sample(x,100,prob=p,replace=TRUE)
```

The inputs are the vector x to sample from, the sample size (100 in this case), the probabilities p to use when sampling from x (if this is omitted, the probabilities are assumed equal), and whether to sample with replacement.

### 3.12 Exercises

Exercises marked with ⑧ have detailed solutions at http://stat110.net.

PMFs and CDFs

1. People are arriving at a party one at a time. While waiting for more people to arrive they entertain themselves by comparing their birthdays. Let $X$ be the number of people needed to obtain a birthday match, i.e., before person $X$ arrives no two people have the same birthday, but when person $X$ arrives there is a match. Find the PMF of $X$.
2. (a) Independent Bernoulli trials are performed, with probability 1/2 of success, until there has been at least one success. Find the PMF of the number of trials performed.

(b) Independent Bernoulli trials are performed, with probability 1/2 of success, until there has been at least one success and at least one failure. Find the PMF of the number of trials performed.
3. Let $X$ be an r.v. with CDF $F$, and $Y=\mu+\sigma X$, where $\mu$ and $\sigma$ are real numbers with $\sigma>0$. (Then $Y$ is called a *location-scale transformation* of $X$; we will encounter this concept many times in Chapter 5 and beyond.) Find the CDF of $Y$, in terms of $F$.
4. Let $n$ be a positive integer and

$F(x)=\frac{\lfloor x\rfloor}{n}$

for $0\leq x\leq n$, $F(x)=0$ for $x<0$, and $F(x)=1$ for $x>n$, where $\lfloor x\rfloor$ is the greatest integer less than or equal to $x$. Show that $F$ is a CDF, and find the PMF that it corresponds to.
5. (a) Show that $p(n)=\left(\frac{1}{2}\right)^{n+1}$ for $n=0,1,2,\dots$ is a valid PMF for a discrete r.v.

(b) Find the CDF of a random variable with the PMF from (a).
6. ⑧ *Benford’s law* states that in a very large variety of real-life data sets, the first digit approximately follows a particular distribution with about a 30% chance of a 1, an 18% chance of a 2, and in general

$P(D=j)=\log_{10}\left(\frac{j+1}{j}\right),\text{ for }j\in\{1,2,3,\dots,9\},$

where $D$ is the first digit of a randomly chosen element. Check that this is a valid PMF (using properties of logs, not with a calculator).
7. Bob is playing a video game that has 7 levels. He starts at level 1, and has probability $p_{1}$ of reaching level 2. In general, given that he reaches level $j$, he has probability $p_{j}$ of reaching level $j+1$, for $1\leq j\leq 6$. Let $X$ be the highest level that he reaches. Find the PMF of $X$ (in terms of $p_{1},\dots,p_{6}$).

###