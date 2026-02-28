Random variables and their distributions

Example 3.2.5 (Sum of die rolls). We roll two fair 6-sided dice. Let  $T = X + Y$  be the total of the two rolls, where  $X$  and  $Y$  are the individual rolls. The sample space of this experiment has 36 equally likely outcomes:

$$
S = \{(1, 1), (1, 2), \dots , (6, 5), (6, 6) \}.
$$

For example, 7 of the 36 outcomes  $s$  are shown in the table below, along with the corresponding values of  $X, Y$ , and  $T$ . After the experiment is performed, we observe values for  $X$  and  $Y$ , and then the observed value of  $T$  is the sum of those values.

|  s | X | Y | X + Y  |
| --- | --- | --- | --- |
|  (1,2) | 1 | 2 | 3  |
|  (1,6) | 1 | 6 | 7  |
|  (2,5) | 2 | 5 | 7  |
|  (3,1) | 3 | 1 | 4  |
|  (4,3) | 4 | 3 | 7  |
|  (5,4) | 5 | 4 | 9  |
|  (6,6) | 6 | 6 | 12  |

Since the dice are fair, the PMF of  $X$  is

$$
P (X = j) = 1 / 6,
$$

for  $j = 1,2,\ldots ,6$  (and  $P(X = j) = 0$  otherwise); we say that  $X$  has a Discrete Uniform distribution on  $1,2,\ldots ,6$ . Similarly,  $Y$  is also Discrete Uniform on  $1,2,\ldots ,6$ .

Note that  $Y$  has the same distribution as  $X$  but is not the same random variable as  $X$ . In fact, we have

$$
P (X = Y) = 6 / 3 6 = 1 / 6.
$$

Two more r.v.s in this experiment with the same distribution as  $X$  are  $7 - X$  and  $7 - Y$ . To see this, we can use the fact that for a standard die,  $7 - X$  is the value on the bottom if  $X$  is the value on the top. If the top value is equally likely to be any of the numbers  $1, 2, \ldots, 6$ , then so is the bottom value. Note that even though  $7 - X$  has the same distribution as  $X$ , it is never equal to  $X$  in a run of the experiment!

Let's now find the PMF of  $T$ . By the naive definition of probability,

$$
P (T = 2) = P (T = 1 2) = 1 / 3 6,
$$

$$
P (T = 3) = P (T = 1 1) = 2 / 3 6,
$$

$$
P (T = 4) = P (T = 1 0) = 3 / 3 6,
$$

$$
P (T = 5) = P (T = 9) = 4 / 3 6,
$$

$$
P (T = 6) = P (T = 8) = 5 / 3 6,
$$

$$
P (T = 7) = 6 / 3 6.
$$

For all other values of  $t$ ,  $P(T = t) = 0$ . We can see directly that the support of  $T$