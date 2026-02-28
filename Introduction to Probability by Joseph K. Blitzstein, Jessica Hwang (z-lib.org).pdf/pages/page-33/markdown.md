For $k>n$, we have $\binom{n}{k}=0$.

###### Proof.

Let $A$ be a set with $|A|=n$. Any subset of $A$ has size at most $n$, so $\binom{n}{k}=0$ for $k>n$. Now let $k\leq n$. By Theorem 1.4.8, there are $n(n-1)\cdots(n-k+1)$ ways to make an *ordered* choice of $k$ elements without replacement. This overcounts each subset of interest by a factor of $k!$ (since we don’t care how these elements are ordered), so we can get the correct count by dividing by $k!$. ∎

$\nLeftrightarrow$ 1.4.16. The binomial coefficient $\binom{n}{k}$ is often defined in terms of factorials, but keep in mind that $\binom{n}{k}$ is $0$ if $k>n$, even though the factorial of a negative number is undefined. Also, the middle expression in Theorem 1.4.15 is often better for computation than the expression with factorials, since factorials grow *extremely* fast. For example,

$\binom{100}{2}=\frac{100\cdot 99}{2}=4950$

can even be done by hand, whereas computing $\binom{100}{2}=100!/(98!\cdot 2!)$ by first calculating $100!$ and $98!$ would be wasteful and possibly dangerous because of the extremely large numbers involved ($100!\approx 9.33\times 10^{157}$).

###### Example 1.4.17 (Club officers).

In a club with $n$ people, there are $n(n-1)(n-2)$ ways to choose a president, vice president, and treasurer, and there are

$\binom{n}{3}=\frac{n(n-1)(n-2)}{3!}$

ways to choose $3$ officers without predetermined titles. ∎

###### Example 1.4.18 (Permutations of a word).

How many ways are there to permute the letters in the word LALALAAA? To determine a permutation, we just need to choose where the $5$ A’s go (or, equivalently, just decide where the $3$ L’s go). So there are

$\binom{8}{5}=\binom{8}{3}=\frac{8\cdot 7\cdot 6}{3!}=56\text{ permutations}.$

How many ways are there to permute the letters in the word STATISTICS? Here are two approaches. We could choose where to put the S’s, then where to put the T’s (from the remaining positions), then where to put the I’s, then where to put the A (and then the C is determined). Alternatively, we can start with $10!$ and then adjust for overcounting, dividing by $3!3!2!$ to account for the fact that the S’s can be permuted among themselves in any way, and likewise for the T’s and I’s. This gives

$\binom{10}{3}\binom{7}{3}\binom{4}{2}\binom{2}{1}=\frac{10!}{3!3!2!}=50400\text{ possibilities}.\qed$

###### Example 1.4.19 (Binomial theorem).

The *binomial theorem* states that

$(x+y)^{n}=\sum_{k=0}^{n}\binom{n}{k}x^{k}y^{n-k},$