variable, then

$E(Y)=\sum_{s}Y(s)P(\{s\}).$

We *can* combine $\sum_{s}X(s)P(\{s\})$ and $\sum_{s}Y(s)P(\{s\})$, which gives

$E(X)+E(Y)=\sum_{s}X(s)P(\{s\})+\sum_{s}Y(s)P(\{s\})=\sum_{s}(X+Y)(s)P(\{s\})=E(X+Y).$

Another intuition for linearity of expectation is via the concept of *simulation*. If we simulate many, many times from the distribution of $X$, the histogram of the simulated values will look very much like the true PMF of $X$. In particular, the *arithmetic mean* of the simulated values will be very close to the true value of $E(X)$ (the precise nature of this convergence is described by the law of large numbers, an important theorem that we will discuss in detail in Chapter 10).

Let $X$ and $Y$ be r.v.s summarizing a certain experiment. Suppose we perform the experiment $n$ times, where $n$ is a very large number, and we write down the values realized by $X$ and $Y$ each time. For each repetition of the experiment, we obtain an $X$ value, a $Y$ value, and (by adding them) an $X+Y$ value. In Figure 4.4, each row represents a repetition of the experiment. The left column contains the draws of $X$, the middle column contains the draws of $Y$, and the right column contains the draws of $X+Y$.

There are two ways to calculate the sum of all the numbers in the last column. The straightforward way is just to add all the numbers in that column. But an equally valid way is to add all the numbers in the first column, add all the numbers in the second column, and then add the two column sums.

Dividing by $n$ everywhere, what we’ve argued is that the following procedures are equivalent:

- Taking the arithmetic mean of all the numbers in the last column. By the law of large numbers, this is very close to $E(X+Y)$.
- Taking the arithmetic mean of the first column and the arithmetic mean of the second column, then adding the two column means. By the law of large numbers, this is very close to $E(X)+E(Y)$.

Linearity of expectation thus emerges as a simple fact about arithmetic (we’re just adding numbers in two different orders)! Notice that nowhere in our argument did we rely on whether $X$ and $Y$ were independent. In fact, in Figure 4.4, $X$ and $Y$ appear to be dependent: $Y$ tends to be large when $X$ is large, and $Y$ tends to be small when $X$ is small (in the language of Chapter 7, we say that $X$ and $Y$ are *positively correlated*). But this dependence is irrelevant: shuffling the draws of $Y$ could completely alter the pattern of dependence between $X$ and $Y$, but would have no effect on the column sums.