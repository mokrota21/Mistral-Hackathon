8. There are 100 prizes, with one worth $1, one worth $2, $\dots$, and one worth $100. There are 100 boxes, each of which contains one of the prizes. You get 5 prizes by picking random boxes one at a time, *without replacement*. Find the PMF of how much your most valuable prize is worth (as a simple expression in terms of binomial coefficients).
9. Let $F_{1}$ and $F_{2}$ be CDFs, $0<p<1$, and $F(x)=pF_{1}(x)+(1-p)F_{2}(x)$ for all $x$.

(a) Show directly that $F$ has the properties of a valid CDF (see Theorem 3.6.3). The distribution defined by $F$ is called a *mixture* of the distributions defined by $F_{1}$ and $F_{2}$.

(b) Consider creating an r.v. in the following way. Flip a coin with probability $p$ of Heads. If the coin lands Heads, generate an r.v. according to $F_{1}$; if the coin lands Tails, generate an r.v. according to $F_{2}$. Show that the r.v. obtained in this way has CDF $F$.
10. (a) Is there a discrete distribution with support $1,2,3,\dots$, such that the value of the PMF at $n$ is proportional to $1/n$?

Hint: See the math appendix for a review of some facts about series.

(b) Is there a discrete distribution with support $1,2,3,\dots$, such that the value of the PMF at $n$ is proportional to $1/n^{2}$?
11. 1 Let $X$ be an r.v. whose possible values are $0,1,2,\dots$, with CDF $F$. In some countries, rather than using a CDF, the convention is to use the function $G$ defined by $G(x)=P(X<x)$ to specify a distribution. Find a way to convert from $F$ to $G$, i.e., if $F$ is a known function, show how to obtain $G(x)$ for all real $x$.
12. (a) Give an example of r.v.s $X$ and $Y$ such that $F_{X}(x)\leq F_{Y}(x)$ for all $x$, where the inequality is strict for some $x$. Here $F_{X}$ is the CDF of $X$ and $F_{Y}$ is the CDF of $Y$. For the example you gave, sketch the CDFs of both $X$ and $Y$ on the same axes. Then sketch their PMFs on a second set of axes.

(b) In Part (a), you found an example of two different CDFs where the first is less than or equal to the second everywhere. Is it possible to find two different PMFs where the first is less than or equal to the second everywhere? In other words, find discrete r.v.s $X$ and $Y$ such that $P(X=x)\leq P(Y=x)$ for all $x$, where the inequality is strict for some $x$, or show that it is impossible to find such r.v.s.
13. Let $X,Y,Z$ be discrete r.v.s such that $X$ and $Y$ have the same conditional distribution given $Z$, i.e., for all $a$ and $z$ we have

$P(X=a|Z=z)=P(Y=a|Z=z).$

Show that $X$ and $Y$ have the same distribution (unconditionally, not just when given $Z$).
14. Let $X$ be the number of purchases that Fred will make on the online site for a certain company (in some specified time period). Suppose that the PMF of $X$ is $P(X=k)=e^{-\lambda}\lambda^{k}/k!$ for $k=0,1,2,\dots$. This distribution is called the *Poisson distribution* with parameter $\lambda$, and it will be studied extensively in later chapters.

(a) Find $P(X\geq 1)$ and $P(X\geq 2)$ without summing infinite series.

(b) Suppose that the company only knows about people who have made at least one purchase on their site (a user sets up an account to make a purchase, but someone who has never made a purchase there doesn’t appear in the customer database). If the company computes the number of purchases for everyone in their database, then these data are draws from the *conditional* distribution of the number of purchases, given that at least one purchase is made. Find the conditional PMF of $X$ given $X\geq 1$. (This conditional distribution is called a *truncated Poisson distribution*.)