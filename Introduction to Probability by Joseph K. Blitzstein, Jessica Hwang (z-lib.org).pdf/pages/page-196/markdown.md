Expectation

(c) The number $X$ of empty boxes is approximately $\operatorname{Pois}(3)$, since there are a lot of boxes but each is very unlikely to be empty; the probability that a specific box is empty is $(1-\frac{1}{n})^{k}=\frac{1}{n}\cdot E(X)\approx 0.003$. So

$P(X\geq 1)=1-P(X=0)\approx 1-e^{-3}\approx 1-\frac{1}{20}=0.95.\qed$

Poisson approximation greatly simplifies obtaining a good approximate solution to the birthday problem discussed in Chapter 1, and makes it possible to obtain good approximations to various variations which would be hard to solve exactly.

###### Example 4.7.5 (Birthday problem continued).

If we have $m$ people and make the usual assumptions about birthdays, then each pair of people has probability $p=1/365$ of having the same birthday, and there are ${m\choose 2}$ pairs. By the Poisson paradigm the distribution of the number $X$ of birthday matches is approximately $\operatorname{Pois}(\lambda)$, where $\lambda={m\choose 2}\frac{1}{365}$. Then the probability of at least one match is

$P(X\geq 1)=1-P(X=0)\approx 1-e^{-\lambda}.$

For $m=23$, $\lambda=253/365$ and $1-e^{-\lambda}\approx 0.500002$, which agrees with our finding from Chapter 1 that we need 23 people to have a 50-50 chance of a matching birthday.

Note that even though $m=23$ is fairly small, the relevant quantity in this problem is actually ${m\choose 2}$, which is the total number of “trials” for a successful birthday match, so the Poisson approximation still performs well. ∎

###### Example 4.7.6 (Near-birthday problem).

What if we want to find the number of people required in order to have a 50-50 chance that two people would have birthdays within one day of each other (i.e., on the same day or one day apart)? Unlike the original birthday problem, this is difficult to obtain an exact answer for, but the Poisson paradigm still applies. The probability that any two people have birthdays within one day of each other is $3/365$ (choose a birthday for the first person, and then the second person needs to be born on that day, the day before, or the day after). Again there are ${m\choose 2}$ possible pairs, so the number of within-one-day matches is approximately $\operatorname{Pois}(\lambda)$ where $\lambda={m\choose 2}\frac{3}{365}$. Then a calculation similar to the one above tells us that we need $m=14$ or more. This was a quick approximation, but it turns out that $m=14$ is the exact answer! ∎

###### Example 4.7.7 (Birth-minute and birth-hour).

There are 1600 sophomores at a certain college. Throughout this example, make the usual assumptions as in the birthday problem.

(a) Find a Poisson approximation for the probability that there are two sophomores who were born not only on the same day of the year, but also at the same hour and the same minute (e.g., both sophomores were born at 8:20 pm on March 31, not necessarily in the same year).

(b) With assumptions as in (a), what is the probability that there are four sophomores who were born not only on the same day, but also at the same hour (e.g., all were born between 2 pm and 3 pm on March 31, not necessarily in the same year)?