Probability and counting

# Story proofs

15. ⑤ Give a story proof that $\sum_{k=0}^{n} \binom{n}{k} = 2^n$.

16. ⑤ Show that for all positive integers $n$ and $k$ with $n \geq k$,

$$
\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k},
$$

doing this in two ways: (a) algebraically and (b) with a story, giving an interpretation for why both sides count the same thing.

Hint: for the story proof: Imagine an organization consisting of $n + 1$ people, with one of them pre-designated as the president of the organization.

17. Give a story proof that

$$
\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n},
$$

for all positive integers $n$.

18. Give a story proof that

$$
\sum_{k=1}^{n} k \binom{n}{k}^2 = n \binom{2n-1}{n-1},
$$

for all positive integers $n$.

Hint: Consider choosing a committee of size $n$ from two groups of size $n$ each, where only one of the two groups has people eligible to become the chair of the committee.

19. Give a story proof that

$$
\sum_{k=2}^{n} \binom{k}{2} \binom{n-k+2}{2} = \binom{n+3}{5},
$$

for all integers $n \geq 2$.

Hint: Consider the middle number in a subset of $\{1, 2, \ldots, n + 3\}$ of size 5.

20. ⑤ (a) Show using a story proof that

$$
\binom{k}{k} + \binom{k+1}{k} + \binom{k+2}{k} + \cdots + \binom{n}{k} = \binom{n+1}{k+1},
$$

where $n$ and $k$ are positive integers with $n \geq k$. This is called the hockey stick identity.

Hint: Imagine arranging a group of people by age, and then think about the oldest person in a chosen subgroup.

(b) Suppose that a large pack of Haribo gummi bears can have anywhere between 30 and 50 gummi bears. There are 5 delicious flavors: pineapple (clear), raspberry (red), orange (orange), strawberry (green, mysteriously), and lemon (yellow). There are 0 non-delicious flavors. How many possibilities are there for the composition of such a pack of gummi bears? You can leave your answer in terms of a couple binomial coefficients, but not a sum of lots of binomial coefficients.

21. Define $\binom{n}{k}$ as the number of ways to partition $\{1, 2, \ldots, n\}$ into $k$ nonempty subsets, or the number of ways to have $n$ students split up into $k$ groups such that each group has at least one student. For example, $\binom{4}{2} = 7$ because we have the following possibilities.