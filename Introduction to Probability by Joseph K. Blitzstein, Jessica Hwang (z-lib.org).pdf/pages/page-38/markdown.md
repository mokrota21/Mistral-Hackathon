Probability and counting

Story proof: Consider a group of $n$ people, from which a team of $k$ will be chosen, one of whom will be the team captain. To specify a possibility, we could first choose the team captain and then choose the remaining $k-1$ team members; this gives the left-hand side. Equivalently, we could first choose the $k$ team members and then choose one of them to be captain; this gives the right-hand side. ∎

Example 1.5.3 (Vandermonde’s identity). A famous relationship between binomial coefficients, called Vandermonde’s identity, says that

$$
\binom{m + n}{k} = \sum_{j = 0}^{k} \binom{m}{j} \binom{n}{k - j}.
$$

This identity will come up several times in this book. Trying to prove it with a brute force expansion of all the binomial coefficients would be a nightmare. But a story proves the result elegantly and makes it clear why the identity holds.

Story proof: Consider a student organization consisting of $m$ juniors and $n$ seniors, from which a committee of size $k$ will be chosen. There are $\binom{m+n}{k}$ possibilities. If there are $j$ juniors in the committee, then there must be $k - j$ seniors in the committee. The right-hand side of the identity sums up the cases for $j$. ∎

Example 1.5.4 (Partnerships). Let’s use a story proof to show that

$$
\frac{(2n)!}{2^n \cdot n!} = (2n - 1)(2n - 3) \cdots 3 \cdot 1.
$$

Story proof: We will show that both sides count the number of ways to break $2n$ people into $n$ partnerships. Take $2n$ people, and give them ID numbers from 1 to $2n$. We can form partnerships by lining up the people in some order and then saying the first two are a pair, the next two are a pair, etc. This overcounts by a factor of $n! \cdot 2^n$ since the order of pairs doesn’t matter, nor does the order within each pair. Alternatively, count the number of possibilities by noting that there are $2n - 1$ choices for the partner of person 1, then $2n - 3$ choices for person 2 (or person 3, if person 2 was already paired to person 1), and so on. ∎

## 1.6 Non-naive definition of probability

We have now seen several methods for counting outcomes in a sample space, allowing us to calculate probabilities if the naive definition applies. But the naive definition can only take us so far, since it requires equally likely outcomes and can’t handle

²Vandermonde’s identity is named after the 18th century French mathematician Alexandre-Théophile Vandermonde, but it was discovered much earlier, and stated in 1303 by the Chinese mathematician Zhu Shijie.