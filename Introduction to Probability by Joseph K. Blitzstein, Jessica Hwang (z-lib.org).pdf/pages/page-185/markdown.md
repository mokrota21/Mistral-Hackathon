Introduction to Probability

|   | With replacement | Without replacement  |
| --- | --- | --- |
|  Fixed number of trials | Binomial | Hypergeometric  |
|  Fixed number of successes | Negative Binomial | Negative Hypergeometric  |

Example 4.4.7 (Negative Hypergeometric). An urn contains  $w$  white balls and  $b$  black balls, which are randomly drawn one by one without replacement, until  $r$  white balls have been obtained. The number of black balls drawn before drawing the  $r$ th white ball has a Negative Hypergeometric distribution with parameters  $w, b, r$ . We denote this distribution by  $\mathrm{NHGeom}(w, b, r)$ . Of course, we assume that  $r \leq w$ . For example, if we shuffle a deck of cards and deal them one at a time, the number of cards dealt before uncovering the first ace is  $\mathrm{NHGeom}(4, 48, 1)$ .

As another example, suppose a college offers  $g$  good courses and  $b$  bad courses (for some definition of "good" and "bad"), and a student wants to find 4 good courses to take. Not having any idea which of the courses are good, the student randomly tries out courses one at a time, stopping when they have obtained 4 good courses. Then the number of bad courses the student tries out is  $\mathrm{NHGeom}(g, b, 4)$ .

We can obtain the PMF of  $X \sim \mathrm{NHGeom}(w, b, r)$  by noting that, in the urn context,  $X = k$  means that the  $(r + k)$ th ball chosen is white and exactly  $r - 1$  of the first  $r + k - 1$  balls chosen are white. This gives

$$
P (X = k) = \frac {\binom {w} {r - 1} \binom {b} {k}}{\binom {w + b} {r + k - 1}} \cdot \frac {w - r + 1}{w + b - r - k + 1}
$$

for  $k = 0,1,\ldots ,b$  (and 0 otherwise).

Alternatively, we can imagine that we continue drawing balls until the urn has been emptied out; this is valid since whether or not we continue to draw balls after obtaining the  $r$ th white ball has no effect on  $X$ . Think of the  $w + b$  balls as lined up in a random order, the order in which they will be drawn.

Then  $X = k$  means that among the first  $r + k - 1$  balls there are exactly  $r - 1$  white balls, then there is a white ball, and then among the last  $w + b - r - k$  balls there are exactly  $w - r$  white balls. All  $\binom{w+b}{w}$  possibilities for the locations of the white balls in the line are equally likely. So by the naive definition of probability, we have the following slightly simpler expression for the PMF:

$$
P (X = k) = \frac {\binom {r + k - 1} {r - 1} \binom {w + b - r - k} {w - r}}{\binom {w + b} {w}},
$$

for  $k = 0,1,\ldots ,b$  (and 0 otherwise).

Finding the expected value of a Negative Hypergeometric r.v. directly from the definition of expectation results in complicated sums. But the answer is very simple: for  $X \sim \mathrm{NHGeom}(w, b, r)$ , we have  $E(X) = rb / (w + 1)$ .

Let's prove this using indicator r.v.s. As explained above, we can assume that we