Give two different Poisson approximations for this value, one based on creating an indicator r.v. for each quadruplet of sophomores, and the other based on creating an indicator r.v. for each possible day-hour. Which do you think is more accurate?

*Solution*:

(a) This is the birthday problem, with $c=365\cdot 24\cdot 60=525600$ categories rather than 365 categories. Let $n=1600$. Creating an indicator r.v. for each pair of sophomores, by linearity the expected number of pairs born on the same day-hour-minute is

$\lambda_{1}={n\choose 2}\frac{1}{c}.$

By Poisson approximation, the probability of at least one match is approximately

$1-\exp(-\lambda_{1})\approx 0.9122.$

This approximation is very accurate: typing pbirthday(1600, classes=365*24*60) in R yields 0.9125.

(b) Now there are $b=365\cdot 24=8760$ categories. Let’s explore two different methods of Poisson approximation.

*Method 1*: Create an indicator for each set of 4 sophomores. By linearity, the expected number of sets of 4 sophomores born on the same day-hour is

$\lambda_{2}={n\choose 4}\frac{1}{b^{3}}.$

Poisson approximation gives that the desired probability is approximately

$1-\exp(-\lambda_{2})\approx 0.333.$

*Method 2*: Create an indicator for each possible day-hour. Let $I_{j}$ be the indicator for at least 4 people having been born on the $j$th day-hour of the year (ordered chronologically), for $1\leq j\leq b$. Let $p=1/b$ and $q=1-p$. Then

$E(I_{j})$ $=$ $P(I_{j}=1)$
$=$ $1-P(\mbox{at most 3 people born on the $j$th day-hour})$
$=$ $1-q^{n}-npq^{n-1}-{n\choose 2}p^{2}q^{n-2}-{n\choose 3}p^{3}q^{n-3}.$

The expected number of day-hours on which at least 4 sophomores were born is

$\lambda_{3}=b\cdot E(I_{1}),$

with $E(I_{1})$ as above. We then have the Poisson approximation

$1-\exp(-\lambda_{3})\approx 0.295.$