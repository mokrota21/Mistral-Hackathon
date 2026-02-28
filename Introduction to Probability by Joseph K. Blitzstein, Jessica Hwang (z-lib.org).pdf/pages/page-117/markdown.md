Fred: That outcome would be incredibly unlikely with fair coins. They must be using trick coins (maybe with double-headed coins), or the experiment must have been rigged somehow (maybe with magnets).

Fred’s friend: It’s true that the string HH…H of length 92 is very unlikely; the chance is $1/2^{92}\approx 2\times 10^{-28}$ with fair coins. But any other specific string of H’s and T’s with length 92 has exactly the same probability! The reason the outcome seems extremely unlikely is that the number of possible outcomes grows exponentially as the number of spins grows, so any outcome would seem extremely unlikely. You could just as well have made the same argument even without looking at the results of their experiment, which means you really don’t have evidence against the coins being fair.

Discuss these comments, to help Fred and his friend resolve their debate.

(b) Suppose there are only two possibilities: either the coins are all fair (and spun fairly), or double-headed coins are being used (in which case the probability of Heads is 1). Let $p$ be the prior probability that the coins are fair. Find the posterior probability that the coins are fair, given that they landed Heads in 92 out of 92 trials.

(c) Continuing from (b), for which values of $p$ is the posterior probability that the coins are fair greater than 0.5? For which values of $p$ is it less than 0.05?
71. There are $n$ types of toys, which you are collecting one by one. Each time you buy a toy, it is randomly determined which type it has, with equal probabilities. Let $p_{ij}$ be the probability that just after you have bought your $i$th toy, you have exactly $j$ toy types in your collection, for $i\geq 1$ and $0\leq j\leq n$. (This problem is in the setting of the coupon collector problem, a famous problem which we study in Example 4.3.12.)

(a) Find a recursive equation expressing $p_{ij}$ in terms of $p_{i-1,j}$ and $p_{i-1,j-1}$, for $i\geq 2$ and $1\leq j\leq n$.

(b) Describe how the recursion from (a) can be used to calculate $p_{ij}$.
72. A/B testing is a form of randomized experiment that is used by many companies to learn about how customers will react to different treatments. For example, a company may want to see how users will respond to a new feature on their website (compared with how users respond to the current version of the website) or compare two different advertisements.

As the name suggests, two different treatments, Treatment A and Treatment B, are being studied. Users arrive one by one, and upon arrival are randomly assigned to one of the two treatments. The trial for each user is classified as “success” (e.g., the user made a purchase) or “failure”. The probability that the $n$th user receives Treatment A is allowed to depend on the outcomes for the previous users. This set-up is known as a two-armed bandit.

Many algorithms for how to randomize the treatment assignments have been studied. Here is an especially simple (but fickle) algorithm, called a stay-with-a-winner procedure:

1. Randomly assign the first user to Treatment A or Treatment B, with equal probabilities.
2. If the trial for the $n$th user is a success, stay with the same treatment for the $(n+1)$st user; otherwise, switch to the other treatment for the $(n+1)$st user.

Let $a$ be the probability of success for Treatment A, and $b$ be the probability of success for Treatment B. Assume that $a\neq b$, but that $a$ and $b$ are unknown (which is why the test is needed). Let $p_{n}$ be the probability of success on the $n$th trial and $a_{n}$ be the probability that Treatment A is assigned on the $n$th trial (using the above algorithm).

(a) Show that

$p_{n}$ $=(a-b)a_{n}+b,$
$a_{n+1}$ $=(a+b-1)a_{n}+1-b.$