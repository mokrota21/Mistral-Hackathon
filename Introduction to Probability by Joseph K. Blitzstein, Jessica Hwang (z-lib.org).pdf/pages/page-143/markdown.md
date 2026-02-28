Introduction to Probability

for all $y$ in the support of $g(X)$.

Example 3.7.4. Continuing as in the previous example, let $D$ be the particle's distance from the origin after $n$ steps. Assume that $n$ is even. Find the PMF of $D$.

Solution:

We can write $D = |Y|$; this is a function of $Y$, but it isn't one-to-one. The event $D = 0$ is the same as the event $Y = 0$. For $k = 2,4,\ldots ,n$, the event $D = k$ is the same as the event $\{Y = k\} \cup \{Y = -k\}$. So the PMF of $D$ is

$$
P (D = 0) = \left( \begin{array}{c} n \\ \frac {n}{2} \end{array} \right) \left(\frac {1}{2}\right) ^ {n},
$$

$$
P (D = k) = P (Y = k) + P (Y = - k) = 2 \binom {n} {\frac {n + k}{2}} \left(\frac {1}{2}\right) ^ {n},
$$

for $k = 2,4,\ldots ,n$. In the final step we used symmetry (imagine a new random walk that moves left each time our random walk moves right, and vice versa) to see that $P(Y = k) = P(Y = -k)$.

The same reasoning we have used to handle functions of one random variable can be extended to deal with functions of multiple random variables. We have already seen an example of this with the addition function (which maps two numbers $x, y$ to their sum $x + y$): in Example 3.2.5, we saw how to view $T = X + Y$ as an r.v. in its own right, where $X$ and $Y$ are obtained by rolling dice.

Definition 3.7.5 (Function of two r.v.s). Given an experiment with sample space $S$, if $X$ and $Y$ are r.v.s that map $s \in S$ to $X(s)$ and $Y(s)$ respectively, then $g(X,Y)$ is the r.v. that maps $s$ to $g(X(s),Y(s))$.

Note that we are assuming that $X$ and $Y$ are defined on the same sample space $S$. Usually we assume that $S$ is chosen to be rich enough to encompass whatever r.v.s we wish to work with. For example, if $X$ is based on a coin flip and $Y$ is based on a die roll, and we initially were using the sample space $S_{1} = \{H,T\}$ for $X$ and the sample space $S_{2} = \{1,2,3,4,5,6\}$ for $Y$, we can easily redefine $X$ and $Y$ so that both are defined on the richer space $S = S_{1} \times S_{2} = \{(s_{1},s_{2}): s_{1} \in S_{1}, s_{2} \in S_{2}\}$.

One way to understand the mapping from $S$ to $\mathbb{R}$ represented by the r.v. $g(X,Y)$ is with a table displaying the values of $X, Y$, and $g(X,Y)$ under various possible outcomes. Interpreting $X + Y$ as an r.v. is intuitive: if we observe $X = x$ and $Y = y$, then $X + Y$ crystallizes to $x + y$. For a less familiar example like $\max(X,Y)$, students often are unsure how to interpret it as an r.v. But the idea is the same: if we observe $X = x$ and $Y = y$, then $\max(X,Y)$ crystallizes to $\max(x,y)$.

Example 3.7.6 (Maximum of two die rolls). We roll two fair 6-sided dice. Let $X$ be the number on the first die and $Y$ the number on the second die. The following table gives the values of $X, Y$, and $\max(X, Y)$ under 7 of the 36 outcomes in the sample space, analogously to the table in Example 3.2.5.