Random variables and their distributions

In this chapter, we introduce *random variables*, an incredibly useful concept that simplifies notation and expands our ability to quantify uncertainty and summarize the results of experiments. Random variables are essential throughout the rest of this book, and throughout statistics, so it is crucial to think through what they mean, both intuitively and mathematically.

### 3.1 Random variables

To see why our current notation can quickly become unwieldy, consider again the gambler’s ruin problem from Chapter 2. In this problem, we may be very interested in how much wealth each gambler has at any particular time. So we could make up notation like letting $A_{jk}$ be the event that gambler A has exactly $j$ dollars after $k$ rounds, and similarly defining an event $B_{jk}$ for gambler B, for all $j$ and $k$.

This is already too complicated. Furthermore, we may also be interested in other quantities, such as the difference in their wealths (gambler A’s minus gambler B’s) after $k$ rounds, or the duration of the game (the number of rounds until one player is bankrupt). Expressing the event “the duration of the game is $r$ rounds” in terms of the $A_{jk}$ and $B_{jk}$ would involve a long, awkward string of unions and intersections. And then what if we want to express gambler A’s wealth as the equivalent amount in euros rather than dollars? We can multiply a *number* in dollars by a currency exchange rate, but we can’t multiply an *event* by an exchange rate.

Instead of having convoluted notation that obscures how the quantities of interest are related, wouldn’t it be nice if we could say something like the following?

> Let $X_{k}$ be the wealth of gambler A after $k$ rounds. Then $Y_{k}=N-X_{k}$ is the wealth of gambler B after $k$ rounds (where $N$ is the fixed total wealth); $X_{k}-Y_{k}=2X_{k}-N$ is the difference in wealths after $k$ rounds; $c_{k}X_{k}$ is the wealth of gambler A in euros after $k$ rounds, where $c_{k}$ is the euros per dollar exchange rate after $k$ rounds; and the duration is $R=\min\{n:X_{n}=0\text{ or }Y_{n}=0\}$.

The notion of a random variable will allow us to do exactly this! It needs to be introduced carefully though, to make it both conceptually and technically correct. Sometimes a definition of “random variable” is given that is a barely paraphrased