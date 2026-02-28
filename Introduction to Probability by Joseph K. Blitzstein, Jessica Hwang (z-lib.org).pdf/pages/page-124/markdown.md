finite or countably infinite set of values $x$ such that $P(X=x)>0$ is called the *support* of $X$.

Most commonly in applications, the support of a discrete r.v. is a set of integers. In contrast, a *continuous* r.v. can take on any real value in an interval (possibly even the entire real line); such r.v.s are defined more precisely in 5. It is also possible to have an r.v. that is a hybrid of discrete and continuous, such as by flipping a coin and then generating a discrete r.v. if the coin lands Heads and generating a continuous r.v. if the coin lands Tails. But the starting point for understanding such r.v.s is to understand discrete and continuous r.v.s.

Given a random variable, we would like to be able to describe its behavior using the language of probability. For example, we might want to answer questions about the probability that the r.v. will fall into a given range: if $L$ is the lifetime earnings of a randomly chosen U.S. college graduate, what is the probability that $L$ exceeds a million dollars? If $M$ is the number of major earthquakes in California in the next five years, what is the probability that $M$ equals 0?

The *distribution* of a random variable provides the answers to these questions; it specifies the probabilities of all events associated with the r.v., such as the probability of it equaling 3 and the probability of it being at least 110. We will see that there are several equivalent ways to express the distribution of an r.v. For a discrete r.v., the most natural way to do so is with a *probability mass function*, which we now define.

###### Definition 3.2.2 (Probability mass function).

The *probability mass function* (PMF) of a discrete r.v. $X$ is the function $p_{X}$ given by $p_{X}(x)=P(X=x)$. Note that this is positive if $x$ is in the support of $X$, and 0 otherwise.

###### 3.2.3.

In writing $P(X=x)$, we are using $X=x$ to denote an *event*, consisting of all outcomes $s$ to which $X$ assigns the number $x$. This event is also written as $\{X=x\}$; formally, $\{X=x\}$ is defined as $\{s\in S:X(s)=x\}$, but writing $\{X=x\}$ is shorter and more intuitive. Going back to Example 3.1.2, if $X$ is the number of Heads in two fair coin tosses, then $\{X=1\}$ consists of the sample outcomes $HT$ and $TH$, which are the two outcomes to which $X$ assigns the number 1. Since $\{HT,TH\}$ is a subset of the sample space, it is an event. So it makes sense to talk about $P(X=1)$, or more generally, $P(X=x)$. If $\{X=x\}$ were anything other than an event, it would make no sense to calculate its probability! It does not make sense to write “$P(X)$”; we can only take the probability of an event, not of an r.v.

Let’s look at a few examples of PMFs.

###### Example 3.2.4 (Coin tosses continued).

In this example we’ll find the PMFs of all the random variables in Example 3.1.2, the example with two fair coin tosses. Here are the r.v.s we defined, along with their PMFs:

- $X$, the number of Heads. Since $X$ equals 0 if $TT$ occurs, 1 if $HT$ or $TH$ occurs,