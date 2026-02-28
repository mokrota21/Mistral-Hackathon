The Poisson paradigm is also called the law of rare events. The interpretation of “rare” is that the $p_{j}$ are small, not that $\lambda$ is small. For example, in the email example, the low probability of getting an email from a specific person in a particular hour is offset by the large number of people who could send you an email in that hour.

In the examples we gave above, the number of events that occur isn’t exactly Poisson because a Poisson random variable has no upper bound, whereas how many of $A_{1},\ldots,A_{n}$ occur is at most $n$, and there is a limit to how many chocolate chips can be crammed into a cookie. But the Poisson distribution often gives good approximations. Note that the conditions for the Poisson paradigm to hold are fairly flexible: the $n$ trials can have different success probabilities, and the trials don’t have to be independent, though they should not be very dependent. So there are a wide variety of situations that can be cast in terms of the Poisson paradigm. This makes the Poisson a popular model, or at least a starting point, for data whose values are nonnegative integers (called count data in statistics).

###### Example 4.7.4 (Balls in boxes).

There are $k$ distinguishable balls and $n$ distinguishable boxes. The balls are randomly placed in the boxes, with all $n^{k}$ possibilities equally likely. Problems in this setting are called occupancy problems, and are at the core of many widely used algorithms in computer science.

(a) Find the expected number of empty boxes (fully simplified, not as a sum).

(b) Find the probability that at least one box is empty. Express your answer as a sum of at most $n$ terms.

(c) Now let $n=1000,\,k=5806$. The expected number of empty boxes is then approximately $3$. Find a good approximation as a decimal for the probability that at least one box is empty. The handy fact $e^{3}\approx 20$ may help.

Solution:

(a) Let $I_{j}$ be the indicator r.v. for the $j$th box being empty. Then

$E(I_{j})=P(I_{j}=1)=\left(1-\frac{1}{n}\right)^{k}.$

By linearity,

$E\left(\sum_{j=1}^{n}I_{j}\right)=\sum_{j=1}^{n}E(I_{j})=n\left(1-\frac{1}{n}\right)^{k}.$

(b) The probability is $1$ for $k<n$. In general, let $A_{j}$ be the event that box $j$ is empty. By inclusion-exclusion,

$P(A_{1}\cup A_{2}\cup\cdots\cup A_{n})$ $=\sum_{j=1}^{n}(-1)^{j+1}\binom{n}{j}P(A_{1}\cap A_{2}\cap\cdots\cap A_{j})$
$=\sum_{j=1}^{n-1}(-1)^{j+1}\binom{n}{j}\left(1-\frac{j}{n}\right)^{k}.$