A third way to describe a distribution is with a story that explains (in a precise way) how the distribution can arise. We used the stories of the Binomial and Hypergeometric distributions to derive the corresponding PMFs. Thus the story and the PMF also contain the same information, though we can often achieve more intuitive proofs with the story than with PMF calculations.

### 3.7 Functions of random variables

In this section we will discuss what it means to take a function of a random variable, and we will build understanding for why *a function of a random variable is a random variable*. That is, if $X$ is a random variable, then $X^{2}$, $e^{X}$, and $\sin(X)$ are also random variables, as is $g(X)$ for any function $g:\mathbb{R}\to\mathbb{R}$.

For example, imagine that two basketball teams (A and B) are playing a seven-game match, and let $X$ be the number of wins for team A (so $X\sim\text{Bin}(7,1/2)$ if the teams are evenly matched and the games are independent). Let $g(x)=7-x$, and let $h(x)=1$ if $x\geq 4$ and $h(x)=0$ if $x<4$. Then $g(X)=7-X$ is the number of wins for team B, and $h(X)$ is the indicator of team A winning the majority of the games. Since $X$ is an r.v., both $g(X)$ and $h(X)$ are also r.v.s.

To see how to define functions of an r.v. formally, let’s rewind a bit. At the beginning of this chapter, we considered a random variable $X$ defined on a sample space with 6 elements. Figure 3.1 used arrows to illustrate how $X$ maps each pebble in the sample space to a real number, and the left half of Figure 3.2 showed how we can equivalently imagine $X$ writing a real number inside each pebble.

Now we can, if we want, apply the same function $g$ to all the numbers inside the pebbles. Instead of the numbers $X(s_{1})$ through $X(s_{6})$, we now have the numbers $g(X(s_{1}))$ through $g(X(s_{6}))$, which gives a new mapping from sample outcomes to real numbers—we’ve created a new random variable, $g(X)$.

###### Definition 3.7.1 (Function of an r.v.).

For an experiment with sample space $S$, an r.v. $X$, and a function $g:\mathbb{R}\to\mathbb{R}$, $g(X)$ is the r.v. that maps $s$ to $g(X(s))$ for all $s\in S$.

Taking $g(x)=\sqrt{x}$ for concreteness, Figure 3.9 shows that $g(X)$ is the *composition* of the functions $X$ and $g$, saying “first apply $X$, then apply $g$”. Figure 3.10 represents $g(X)$ more succinctly by directly labeling the sample outcomes. Both figures show us that $g(X)$ is an r.v.; if $X$ crystallizes to 4, then $g(X)$ crystallizes to 2.

Given a discrete r.v. $X$ with a known PMF, how can we find the PMF of $Y=g(X)$? In the case where $g$ is a one-to-one function, the answer is straightforward: the support of $Y$ is the set of all $g(x)$ with $x$ in the support of $X$, and

$P(Y=g(x))=P(g(X)=g(x))=P(X=x).$