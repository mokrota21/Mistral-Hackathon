3.3 Bernoulli and Binomial

Some distributions are so ubiquitous in probability and statistics that they have their own names. We will introduce these *named distributions* throughout the book, starting with a very simple but useful case: an r.v. that can take on only two possible values, 0 and 1.

###### Definition 3.3.1 (Bernoulli distribution).

An r.v. $X$ is said to have the *Bernoulli distribution* with parameter $p$ if $P(X=1)=p$ and $P(X=0)=1-p$, where $0<p<1$. We write this as $X\sim\text{Bern}(p)$. The symbol $\sim$ is read “is distributed as”.

*Any* r.v. whose possible values are 0 and 1 has a $\text{Bern}(p)$ distribution, with $p$ the probability of the r.v. equaling 1. This number $p$ in $\text{Bern}(p)$ is called the *parameter* of the distribution; it determines which specific Bernoulli distribution we have. Thus there is not just one Bernoulli distribution, but rather a *family* of Bernoulli distributions, indexed by $p$. For example, if $X\sim\text{Bern}(1/3)$, it would be correct but incomplete to say “$X$ is Bernoulli”; to fully specify the distribution of $X$, we should both say its name (Bernoulli) and its parameter value (1/3), which is the point of the notation $X\sim\text{Bern}(1/3)$.

*Any* event has a Bernoulli r.v. that is naturally associated with it, equal to 1 if the event happens and 0 otherwise. This is called the *indicator random variable* of the event; we will see that such r.v.s are extremely useful.

###### Definition 3.3.2 (Indicator random variable).

The *indicator random variable* of an event $A$ is the r.v. which equals 1 if $A$ occurs and 0 otherwise. We will denote the indicator r.v. of $A$ by $I_{A}$ or $I(A)$. Note that $I_{A}\sim\text{Bern}(p)$ with $p=P(A)$.

We often imagine Bernoulli r.v.s using coin tosses, but this is just convenient language for discussing the following general story.

###### Story 3.3.3 (Bernoulli trial).

An experiment that can result in either a “success” or a “failure” (but not both) is called a *Bernoulli trial*. A Bernoulli random variable can be thought of as the *indicator of success* in a Bernoulli trial: it equals 1 if success occurs and 0 if failure occurs in the trial. ∎

Because of this story, the parameter $p$ is often called the *success probability* of the $\text{Bern}(p)$ distribution. Once we start thinking about Bernoulli trials, it’s hard not to start thinking about what happens when we have more than one trial.

###### Story 3.3.4 (Binomial distribution).

Suppose that $n$ *independent* Bernoulli trials are performed, each with the same success probability $p$. Let $X$ be the number of successes. The distribution of $X$ is called the *Binomial distribution* with parameters $n$ and $p$. We write $X\sim\text{Bin}(n,p)$ to mean that $X$ has the Binomial distribution with parameters $n$ and $p$, where $n$ is a positive integer and $0<p<1$. ∎

Notice that we define the Binomial distribution not by its PMF, but by a *story