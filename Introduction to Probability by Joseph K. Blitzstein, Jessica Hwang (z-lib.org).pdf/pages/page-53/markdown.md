Introduction to Probability

$\bullet$ $\{1\}$, $\{2,3,4\}$
$\bullet$ $\{1,2\}$, $\{3,4\}$
$\bullet$ $\{2\}$, $\{1,3,4\}$
$\bullet$ $\{1,3\}$, $\{2,4\}$
$\bullet$ $\{3\}$, $\{1,2,4\}$
$\bullet$ $\{4\}$, $\{1,2,3\}$
$\bullet$ $\{1,4\}$, $\{2,3\}$

Prove the following identities:

(a)

$$
\left\{ \begin{array}{c} n + 1 \\ k \end{array} \right\} = \left\{ \begin{array}{c} n \\ k - 1 \end{array} \right\} + k \left\{ \begin{array}{c} n \\ k \end{array} \right\}.
$$

Hint: I'm either in a group by myself or I'm not.

(b)

$$
\sum_{j = k}^{n} \binom{n}{j} \left\{ \begin{array}{l} j \\ k \end{array} \right\} = \left\{ \begin{array}{l} n + 1 \\ k + 1 \end{array} \right\}.
$$

Hint: First decide how many people are not going to be in my group.

22. The Dutch mathematician R.J. Stroeker remarked:

Every beginning student of number theory surely must have marveled at the miraculous fact that for each natural number $n$ the sum of the first $n$ positive consecutive cubes is a perfect square. [26]

Furthermore, it is the square of the sum of the first $n$ positive integers! That is,

$$
1^{3} + 2^{3} + \cdots + n^{3} = (1 + 2 + \cdots + n)^{2}.
$$

Usually this identity is proven by induction, but that does not give much insight into why the result is true, nor does it help much if we wanted to compute the left-hand side but didn't already know this result. In this problem, you will give a story proof of the identity.

(a) Give a story proof of the identity

$$
1 + 2 + \cdots + n = \binom{n + 1}{2}.
$$

Hint: Consider a round-robin tournament (see Exercise 4).

(b) Give a story proof of the identity

$$
1^{3} + 2^{3} + \cdots + n^{3} = 6 \binom{n + 1}{4} + 6 \binom{n + 1}{3} + \binom{n + 1}{2}.
$$

It is then just basic algebra (not required for this problem) to check that the square of the right-hand side in (a) is the right-hand side in (b).

Hint: Imagine choosing a number between 1 and $n$ and then choosing 3 numbers between 0 and $n$ smaller than the original number, with replacement. Then consider cases based on how many distinct numbers were chosen.

## Naive definition of probability

23. Three people get into an empty elevator at the first floor of a building that has 10 floors. Each presses the button for their desired floor (unless one of the others has already pressed that button). Assume that they are equally likely to want to go to floors 2 through 10 (independently of each other). What is the probability that the buttons for 3 consecutive floors are pressed?