gives the vector obtained by removing the 2nd through 4th entries of $\mathbf{v}$ (the parentheses are needed since -2:4 would be $(-2,-1,\ldots,4)$).

Many operations in R are interpreted *componentwise*. For example, in math the cube of a vector doesn’t have a standard definition, but in R typing v^3 simply cubes each entry individually. Similarly,

1/(1:100)^2

is a very compact way to get the vector $(1,\frac{1}{2^{2}},\frac{1}{3^{2}},\ldots,\frac{1}{100^{2}})$.

In math, $\mathbf{v}+\mathbf{w}$ is undefined if $\mathbf{v}$ and $\mathbf{w}$ are vectors of different lengths, but in R the shorter vector gets “recycled”! For example, v+3 adds 3 to each entry of $\mathbf{v}$.

##### Factorials and binomial coefficients

We can compute $n!$ using factorial(n) and $\binom{n}{k}$ using choose(n,k). As we have seen, factorials grow extremely quickly. What is the largest $n$ for which R returns a number for factorial(n)? Beyond that point, R will return Inf (infinity), with a warning message. But it may still be possible to use lfactorial(n) for larger values of $n$, which computes $\log(n!)$. Similarly, lchoose(n,k) computes $\log\binom{n}{k}$.

##### Sampling and simulation

The sample command is a useful way of drawing random samples in R. (Technically, they are *pseudo-random* since there is an underlying deterministic algorithm, but they “look like” random samples for almost all practical purposes.) For example,

n <- 10; k <- 5
sample(n,k)

generates an ordered random sample of 5 of the numbers from 1 to 10, without replacement, and with equal probabilities given to each number. To sample with replacement instead, just add in replace = TRUE:

n <- 10; k <- 5
sample(n,k,replace=TRUE)

To generate a random permutation of $1,2,\ldots,n$ we can use sample(n,n), which because of R’s default settings can be abbreviated to sample(n).

We can also use sample to draw from a non-numeric vector. For example, letters is built into R as the vector consisting of the 26 lowercase letters of the English alphabet, and sample(letters,7) will generate a random 7-letter “word” by sampling from the alphabet, without replacement.