3.11 R

#### Distributions in R

All of the named distributions that we’ll encounter in this book have been implemented in R. In this section we’ll explain how to work with the Binomial and Hypergeometric distributions in R. We will also explain in general how to generate r.v.s from any discrete distribution with a finite support. Typing help(distributions) gives a handy list of built-in distributions; many others are available through R packages that can be loaded.

In general, for many named discrete distributions, three functions starting with d, p, and r will give the PMF, CDF, and random generation, respectively. Note that the function starting with p is not the PMF, but rather is the CDF.

#### Binomial distribution

The Binomial distribution is associated with the following three R functions: dbinom, pbinom, and rbinom. For the Bernoulli distribution we can just use the Binomial functions with $n=1$.

- dbinom is the Binomial PMF. It takes three inputs: the first is the value of $x$ at which to evaluate the PMF, and the second and third are the parameters $n$ and $p$. For example, dbinom(3,5,0.2) returns the probability $P(X=3)$ where $X\sim\text{Bin}(5,0.2)$. In other words,

$\text{dbinom}(3,5,0.2)=\binom{5}{3}(0.2)^{3}(0.8)^{2}=0.0512.$
- pbinom is the Binomial CDF. It takes three inputs: the first is the value of $x$ at which to evaluate the CDF, and the second and third are the parameters. pbinom(3,5,0.2) is the probability $P(X\leq 3)$ where $X\sim\text{Bin}(5,0.2)$. So

$\text{pbinom}(3,5,0.2)=\sum_{k=0}^{3}\binom{5}{k}(0.2)^{k}(0.8)^{5-k}=0.9933.$
- rbinom is a function for generating Binomial random variables. For rbinom, the first input is *how many* r.v.s we want to generate, and the second and third inputs are still the parameters. Thus the command rbinom(7,5,0.2) produces realizations of seven i.i.d. $\text{Bin}(5,0.2)$ r.v.s. When we ran this command, we got

```
2 1 0 0 1 0 0
```

but you’ll probably get something different when you try it!