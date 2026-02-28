4.1 Definition of expectation

In the previous chapter, we introduced the *distribution* of a random variable, which gives us full information about the probability that the r.v. will fall into any particular set. For example, we can say how likely it is that the r.v. will exceed 1000, that it will equal 5, or that it will be in the interval $[0,7]$. It can be unwieldy to manage so many probabilities though, so often we want just one number summarizing the “average” value of the r.v.

There are several senses in which the word “average” is used, but by far the most commonly used is the *mean* of an r.v., also known as its *expected value*. In addition, much of statistics is about understanding *variability* in the world, so it is often important to know how “spread out” the distribution is; we will formalize this with the concepts of *variance* and *standard deviation*. As we’ll see, variance and standard deviation are defined in terms of expected values, so the uses of expected values go far beyond just computing averages.

Given a list of numbers $x_{1},x_{2},\ldots,x_{n}$, the familiar way to average them is to add them up and divide by $n$. This is called the *arithmetic mean*, and is defined by

$\bar{x}=\frac{1}{n}\sum_{j=1}^{n}x_{j}.$

More generally, we can define a *weighted mean* of $x_{1},\ldots,x_{n}$ as

$\text{weighted-mean}(x)=\sum_{j=1}^{n}x_{j}p_{j},$

where the weights $p_{1},\ldots,p_{n}$ are pre-specified nonnegative numbers that add up to 1 (so the unweighted mean $\bar{x}$ is obtained when $p_{j}=1/n$ for all $j$).

The definition of expectation for a discrete r.v. is inspired by the weighted mean of a list of numbers, with weights given by probabilities.

###### Definition 4.1.1 (Expectation of a discrete r.v.).

The *expected value* (also called the *expectation* or *mean*) of a discrete r.v. $X$ whose distinct possible values are