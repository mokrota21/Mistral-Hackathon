Introduction to Probability

men are more likely to have a certain disease, or whether they are equally likely. A random sample of  $n$  women and  $m$  men is gathered, and each person is tested for the disease (assume for this problem that the test is completely accurate). The numbers of women and men in the sample who have the disease are  $X$  and  $Y$  respectively, with  $X \sim \operatorname{Bin}(n, p_1)$  and  $Y \sim \operatorname{Bin}(m, p_2)$ , independently. Here  $p_1$  and  $p_2$  are unknown, and we are interested in testing whether  $p_1 = p_2$  (this is known as a null hypothesis in statistics).

Consider a  $2 \times 2$  table with rows corresponding to disease status and columns corresponding to gender. Each entry is the count of how many people have that disease status and gender, so  $n + m$  is the sum of all 4 entries. Suppose that it is observed that  $X + Y = r$ .

The Fisher exact test is based on conditioning on both the row and column sums, so  $n, m, r$  are all treated as fixed, and then seeing if the observed value of  $X$  is "extreme" compared to this conditional distribution. Assuming the null hypothesis, find the conditional PMF of  $X$  given  $X + Y = r$ .

Solution:

First we'll build the  $2 \times 2$  table, treating  $n$ ,  $m$ , and  $r$  as fixed.

|   | Women | Men | Total  |
| --- | --- | --- | --- |
|  Disease | x | r-x | r  |
|  No disease | n-x | m-r+x | n+m-r  |
|  Total | n | m | n+m  |

Next, let's compute the conditional PMF  $P(X = x|X + Y = r)$ . By Bayes' rule,

$$
\begin{array}{l} P (X = x | X + Y = r) = \frac {P (X + Y = r | X = x) P (X = x)}{P (X + Y = r)} \\ = \frac {P (Y = r - x) P (X = x)}{P (X + Y = r)}. \\ \end{array}
$$

The step  $P(X + Y = r|X = x) = P(Y = r - x)$  is justified by the independence of  $X$  and  $Y$ . Assuming the null hypothesis and letting  $p = p_1 = p_2$ , we have  $X \sim \operatorname{Bin}(n, p)$  and  $Y \sim \operatorname{Bin}(m, p)$ , independently, so  $X + Y \sim \operatorname{Bin}(n + m, p)$ . Thus,

$$
\begin{array}{l} P (X = x | X + Y = r) = \frac {\binom {m} {r - x} p ^ {r - x} (1 - p) ^ {m - r + x} \binom {n} {x} p ^ {x} (1 - p) ^ {n - x}}{\binom {n + m} {r} p ^ {r} (1 - p) ^ {n + m - r}} \\ = \frac {\binom {n} {x} \binom {m} {r - x}}{\binom {n + m} {r}}. \\ \end{array}
$$

So the conditional distribution of  $X$  is Hypergeometric with parameters  $n, m, r$ .

To understand why the Hypergeometric appeared, seemingly out of nowhere, let's connect this problem to the elk story for the Hypergeometric. In the elk story, we are