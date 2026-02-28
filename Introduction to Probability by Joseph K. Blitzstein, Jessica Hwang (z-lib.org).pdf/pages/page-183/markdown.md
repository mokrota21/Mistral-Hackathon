has the right support because $X$ can’t take on the value $n-1$: if $n-1$ cards are matches, then the $n$th card must be a match as well. So $X$ does not follow a named distribution we have studied, but we can readily find its mean using indicator r.v.s: let’s write $X=I_{1}+I_{2}+\cdots+I_{n}$, where

\[ I_{j}=\left\{\begin{array}[]{ll}1&\mbox{if the $j$th card in the deck is a match,}\\
0&\mbox{otherwise.}\end{array}\right. \]

In other words, $I_{j}$ is the indicator for $A_{j}$, the event that the $j$th card in the deck is a match. We can imagine that each $I_{j}$ “raises its hand” to be counted if its card is a match; adding up the raised hands, we get the total number of matches, $X$.

By the fundamental bridge,

$E(I_{j})=P(A_{j})=\frac{1}{n}$

for all $j$. So by linearity,

$E(X)=E(I_{1})+\cdots+E(I_{n})=n\cdot\frac{1}{n}=1.$

The expected number of matched cards is $1$, regardless of $n$. Even though the $I_{j}$ are dependent in a complicated way that makes the distribution of $X$ neither Binomial nor Hypergeometric, linearity still holds. ∎

###### Example 4.4.5 (Distinct birthdays, birthday matches).

In a group of $n$ people, under the usual assumptions about birthdays, what is the expected number of distinct birthdays among the $n$ people, i.e., the expected number of days on which at least one of the people was born? What is the expected number of birthday matches, i.e., pairs of people with the same birthday?

*Solution*:

Let $X$ be the number of distinct birthdays, and write $X=I_{1}+\cdots+I_{365}$, where

\[ I_{j}=\left\{\begin{array}[]{ll}1&\mbox{if the $j$th day is represented,}\\
0&\mbox{otherwise.}\end{array}\right. \]

We create an indicator for each *day* of the year because $X$ counts the number of *days* of the year that are represented. By the fundamental bridge,

$E(I_{j})=P(j\mbox{th day is represented})=1-P(\mbox{no one born on day $j$)}=1-\left(\frac{364}{365}\right)^{n}$

for all $j$. Then by linearity,

$E(X)=365\left(1-\left(\frac{364}{365}\right)^{n}\right).$

Now let $Y$ be the number of birthday matches. Label the people as $1,2,\ldots,n$, and order the $\binom{n}{2}$ pairs of people in some definite way. Then we can write

$Y=J_{1}+\cdots+J_{\binom{n}{2}},$