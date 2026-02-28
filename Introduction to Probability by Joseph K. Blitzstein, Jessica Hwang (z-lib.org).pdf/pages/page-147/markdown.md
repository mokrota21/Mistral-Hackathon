Introduction to Probability

needed to verify pairwise independence for all  $\binom{n}{2}$  pairs, three-way independence for all  $\binom{n}{3}$  triplets, and so on. However, upon closer examination of the definition, we see that independence of r.v.s requires the equality to hold for all possible  $x_{1},\ldots ,x_{n}$  — infinitely many conditions! If we can find even a single list of values  $x_{1},\ldots ,x_{n}$  for which the above equality fails to hold, then  $X_{1},\ldots ,X_{n}$  are not independent.

$\star 3.8.3$ . If  $X_{1}, \ldots, X_{n}$  are independent, then they are pairwise independent, i.e.,  $X_{i}$  is independent of  $X_{j}$  for  $i \neq j$ . The idea behind proving that  $X_{i}$  and  $X_{j}$  are independent is to let all the  $x_{k}$  other than  $x_{i}, x_{j}$  go to  $\infty$  in the definition of independence, since we already know  $X_{k} &lt; \infty$  is true (though it takes some work to give a complete justification for the limit). But pairwise independence does not imply independence in general, as we saw in Chapter 2 for events.

Example 3.8.4. In a roll of two fair dice, if  $X$  is the number on the first die and  $Y$  is the number on the second die, then  $X + Y$  is not independent of  $X - Y$  since

$$
0 = P (X + Y = 1 2, X - Y = 1) \neq P (X + Y = 1 2) P (X - Y = 1) = \frac {1}{3 6} \cdot \frac {5}{3 6}.
$$

Knowing the total is 12 tells us the difference must be 0, so the r.v.s provide information about each other.

If  $X$  and  $Y$  are independent then it is also true, e.g., that  $X^2$  is independent of  $Y^4$ , since if  $X^2$  provided information about  $Y^4$ , then  $X$  would give information about  $Y$  (using  $X^2$  and  $Y^4$  as intermediaries:  $X$  determines  $X^2$ , which would give information about  $Y^4$ , which in turn would give information about  $Y$ ). More generally, we have the following result (for which we omit a formal proof).

Theorem 3.8.5 (Functions of independent r.v.s). If  $X$  and  $Y$  are independent r.v.s, then any function of  $X$  is independent of any function of  $Y$ .

Definition 3.8.6 (i.i.d.). We will often work with random variables that are independent and have the same distribution. We call such r.v.s independent and identically distributed, or i.i.d. for short.

$\star 3.8.7$  (i. vs. i.d.). "Independent" and "identically distributed" are two often-confused but completely different concepts. Random variables are independent if they provide no information about each other; they are identically distributed if they have the same PMF (or equivalently, the same CDF). Whether two r.v.s are independent has nothing to do with whether they have the same distribution. We can have r.v.s that are:

- independent and identically distributed. Let  $X$  be the result of a die roll, and let  $Y$  be the result of a second, independent die roll. Then  $X$  and  $Y$  are i.i.d.
- independent and not identically distributed. Let  $X$  be the result of a die roll, and let  $Y$  be the closing price of the Dow Jones (a stock market index) a month from now. Then  $X$  and  $Y$  provide no information about each other (one would fervently hope), and  $X$  and  $Y$  do not have the same distribution.