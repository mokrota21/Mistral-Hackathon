Random variables and their distributions

The case where  $Y = g(X)$  with  $g$  one-to-one is illustrated in the following tables; the idea is that if the distinct possible values of  $X$  are  $x_{1}, x_{2}, \ldots$  with probabilities  $p_{1}, p_{2}, \ldots$  (respectively), then the distinct possible values of  $Y$  are  $g(x_{1}), g(x_{2}), \ldots$ , with the same list  $p_{1}, p_{2}, \ldots$  of probabilities.

|  x | P(X=x)  |
| --- | --- |
|  x1 | p1  |
|  x2 | p2  |
|  x3 | p3  |
|  : | :  |

PMF of  $X$ , in table form

|  y | P(Y=y)  |
| --- | --- |
|  g(x1) | p1  |
|  g(x2) | p2  |
|  g(x3) | p3  |
|  : | :  |

PMF of  $Y$ , in table form

This suggests a strategy for finding the PMF of an r.v. with an unfamiliar distribution: try to express the r.v. as a one-to-one function of an r.v. with a known distribution. The next example illustrates this method.

Example 3.7.2 (Random walk). A particle moves  $n$  steps on a number line. The particle starts at 0, and at each step it moves 1 unit to the right or to the left, with equal probabilities. Assume all steps are independent. Let  $Y$  be the particle's position after  $n$  steps. Find the PMF of  $Y$ .

# Solution:

Consider each step to be a Bernoulli trial, where right is considered a success and left is considered a failure. Then the number of steps the particle takes to the right is a  $\operatorname{Bin}(n, 1/2)$  random variable, which we can name  $X$ . If  $X = j$ , then the particle has taken  $j$  steps to the right and  $n - j$  steps to the left, giving a final position of  $j - (n - j) = 2j - n$ . So we can express  $Y$  as a one-to-one function of  $X$ , namely,  $Y = 2X - n$ . Since  $X$  takes values in  $\{0, 1, 2, \ldots, n\}$ ,  $Y$  takes values in  $\{-n, 2 - n, 4 - n, \ldots, n\}$ .

The PMF of  $Y$  can then be found from the PMF of  $X$ :

$$
P (Y = k) = P (2 X - n = k) = P (X = (n + k) / 2) = \left( \begin{array}{c} n \\ \frac {n + k}{2} \end{array} \right) \left(\frac {1}{2}\right) ^ {n},
$$

if  $k$  is an integer between  $-n$  and  $n$  (inclusive) such that  $n + k$  is an even number.

If  $g$  is not one-to-one, then for a given  $y$ , there may be multiple values of  $x$  such that  $g(x) = y$ . To compute  $P(g(X) = y)$ , we need to sum up the probabilities of  $X$  taking on any of these candidate values of  $x$ .

Theorem 3.7.3 (PMF of  $g(X)$ ). Let  $X$  be a discrete r.v. and  $g: \mathbb{R} \to \mathbb{R}$ . Then the support of  $g(X)$  is the set of all  $y$  such that  $g(x) = y$  for at least one  $x$  in the support of  $X$ , and the PMF of  $g(X)$  is

$$
P (g (X) = y) = \sum_ {x: g (x) = y} P (X = x),
$$