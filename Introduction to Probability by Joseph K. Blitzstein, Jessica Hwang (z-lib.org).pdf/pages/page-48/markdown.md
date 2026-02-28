The sample command also allows us to specify general probabilities for sampling each number. For example,

```
sample(4, 3, replace=TRUE, prob=c(0.1,0.2,0.3,0.4))
```

samples three numbers between 1 and 4, with replacement, and with probabilities given by $(0.1,0.2,0.3,0.4)$. If the sampling is without replacement, then at each stage the probability of any not-yet-chosen number is *proportional* to its original probability.

Generating *many* random samples allows us to perform a *simulation* for a probability problem. The replicate command, which is explained below, is a convenient way to do this.

#### 3.2.2 Matching problem simulation

Let’s show by simulation that the probability of a matching card in Example 1.6.4 is approximately $1-1/e$ when the deck is sufficiently large. Using R, we can perform the experiment a bunch of times and see how many times we encounter at least one matching card:

```
n <- 100
r <- replicate(10^4,sum(sample(n)==(1:n)))
sum(r>=1)/10^4
```

In the first line, we choose how many cards are in the deck (here, 100 cards). In the second line, let’s work from the inside out:

- sample(n)==(1:n) is a vector of length n, the $i$th element of which equals 1 if the $i$th card matches its position in the deck and 0 otherwise. That’s because for two numbers $a$ and $b$, the expression a==b is TRUE if $a=b$ and FALSE otherwise, and TRUE is encoded as 1 and FALSE is encoded as 0.
- sum adds up the elements of the vector, giving us the number of matching cards in this run of the experiment.
- replicate does this $10^{4}$ times. We store the results in r, a vector of length $10^{4}$ containing the numbers of matched cards from each run of the experiment.

In the last line, we add up the number of times where there was at least one matching card, and we divide by the number of simulations.

To explain what the code is doing within the code rather than in separate documentation, we can add *comments* using the # symbol to mark the start of a comment. Comments are ignored by R but can make the code much easier to understand for the reader (who could be you—even if you will be the only one using your code, it is often hard to remember what everything means and how the code is supposed to work when looking at it a month after writing it). Short comments can be on the