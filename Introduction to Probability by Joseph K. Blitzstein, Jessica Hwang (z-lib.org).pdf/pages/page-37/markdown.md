one at a time, with replacement and with equal probabilities. Then the $n^{k}$ *ordered* samples are equally likely, making the naive definition applicable, but the $\binom{n+k-1}{k}$ unordered samples (where all that matters is how many times each person was sampled) are *not* equally likely.

As another example, with $n=365$ days in a year and $k$ people, how many possible *unordered* birthday lists are there? For example, for $k=3$, we want to count lists like (May 1, March 31, April 11), where all permutations are considered equivalent. We can’t do a simple adjustment for overcounting such as $n^{k}/3!$ since, e.g., there are 6 permutations of (May 1, March 31, April 11) but only 3 permutations of (March 31, March 31, April 11). By Bose-Einstein, the number of lists is $\binom{n+k-1}{k}$. But the ordered birthday lists are equally likely, not the unordered lists, so the Bose-Einstein value should not be used in calculating birthday probabilities. ∎

### 1.5 Story proofs

A *story proof* is a proof by interpretation. For counting problems, this often means counting the same thing in two different ways, rather than doing tedious algebra. A story proof often avoids messy calculations and goes further than an algebraic proof toward *explaining* why the result is true. The word “story” has several meanings, some more mathematical than others, but a story proof (in the sense in which we’re using the term) is a fully valid mathematical proof. Here are some examples of story proofs, which also serve as further examples of counting.

###### Example 1.5.1 (Choosing the complement).

For any nonnegative integers $n$ and $k$ with $k\leq n$, we have

$\binom{n}{k}=\binom{n}{n-k}.$

This is easy to check algebraically (by writing the binomial coefficients in terms of factorials), but a story proof makes the result easier to understand intuitively.

*Story proof*: Consider choosing a committee of size $k$ in a group of $n$ people. We know that there are $\binom{n}{k}$ possibilities. But another way to choose the committee is to specify which $n-k$ people are *not* on the committee; specifying who is on the committee determines who is *not* on the committee, and vice versa. So the two sides are equal, as they are two ways of counting the same thing. ∎

###### Example 1.5.2 (The team captain).

For any positive integers $n$ and $k$ with $k\leq n$,

$n\binom{n-1}{k-1}=k\binom{n}{k}.$

This is again easy to check algebraically (using the fact that $m!=m(m-1)!$ for any positive integer $m$), but a story proof is more insightful.