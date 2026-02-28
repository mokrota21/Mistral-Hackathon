same line as the corresponding code; longer comments should be on separate lines. For example, a commented version of the above simulation is:

```
n <- 100 # number of cards
r <- replicate(10^4,sum(sample(n)==(1:n))) # shuffle; count matches
sum(r>=1)/10^4 # proportion with a match
```

What did you get when you ran the code? We got 0.63, which is quite close to $1-1/e$.

#### 3.2.2 Birthday problem calculation and simulation

The following code uses prod (which gives the product of a vector) to calculate the probability of at least one birthday match in a group of 23 people:

```
k <- 23
1-prod((365-k+1):365)/365^k
```

Better yet, R has built-in functions, pbirthday and qbirthday, for the birthday problem! pbirthday(k) returns the probability of at least one match if the room has k people. qbirthday(p) returns the number of people needed in order to have probability p of at least one match. For example, pbirthday(23) is 0.507 and qbirthday(0.5) is 23.

We can also find the probability of having at least one triple birthday match, i.e., three people with the same birthday; all we have to do is add coincident=3 to say we’re looking for triple matches. For example, pbirthday(23,coincident=3) returns 0.014, so 23 people give us only a 1.4% chance of a triple birthday match. qbirthday(0.5,coincident=3) returns 88, so we’d need 88 people to have at least a 50% chance of at least one triple birthday match.

To simulate the birthday problem, we can use

```
b <- sample(1:365,23,replace=TRUE)
tabulate(b)
```

to generate random birthdays for 23 people and then tabulate the counts of how many people were born on each day (the command table(b) creates a prettier table, but is slower). We can run $10^{4}$ repetitions as follows:

```
r <- replicate(10^4, max(tabulate(sample(1:365,23,replace=TRUE))))
sum(r>=2)/10^4
```

If the probabilities of various days are not all equal, the calculation becomes much more difficult, but the simulation can easily be extended since sample allows us to specify the probability of each day (by default sample assigns equal probabilities, so in the above the probability is 1/365 for each day).