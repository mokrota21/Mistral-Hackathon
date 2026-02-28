but in general we do *not* have $E(g(X))=g(E(X))$ for arbitrary functions $g$. We must be careful not to move the $E$ around when $g$ is not linear. The next example shows a situation in which $E(g(X))$ is *very* different from $g(E(X))$.

###### Example 4.3.14 (St. Petersburg paradox).

Suppose a wealthy stranger offers to play the following game with you. You will flip a fair coin until it lands Heads for the first time, and you will receive $2 if the game lasts for 1 round, $4 if the game lasts for 2 rounds, $8 if the game lasts for 3 rounds, and in general, $2^{n} if the game lasts for $n$ rounds. What is the fair value of this game (the expected payoff)? How much would you be willing to pay to play this game once?

*Solution*:

Let $X$ be your winnings from playing the game. By definition, $X=2^{N}$ where $N$ is the number of rounds that the game lasts. Then $X$ is 2 with probability 1/2, 4 with probability 1/4, 8 with probability 1/8, and so on, so

$E(X)=\frac{1}{2}\cdot 2+\frac{1}{4}\cdot 4+\frac{1}{8}\cdot 8+\cdots=\infty.$

The expected winnings are infinite! On the other hand, the number of rounds $N$ that the game lasts is the number of tosses until the first Heads, so $N\sim\text{FS}(1/2)$ and $E(N)=2$. Thus $E(2^{N})=\infty$ while $2^{E(N)}=4$. Infinity certainly does not equal 4, illustrating the danger of confusing $E(g(X))$ with $g(E(X))$ when $g$ is not linear.

This problem is often considered a paradox because although the game’s expected payoff is infinite, most people would not be willing to pay very much to play the game (even if they could afford to lose the money). One explanation is to note that *the amount of money in the real world is finite*. Suppose that if the game lasts longer than 40 rounds, the wealthy stranger flees the country and you get nothing. Since $2^{40}\approx 1.1\times 10^{12}$, this still gives you the potential to earn over a trillion dollars, and anyway it’s incredibly unlikely that the game will last longer than 40 rounds. But in this setting, your expected value is

$E(X)=\sum_{n=1}^{40}\frac{1}{2^{n}}\cdot 2^{n}+\sum_{n=41}^{\infty}\frac{1}{2^{n}}\cdot 0=40.$

Is this drastic reduction because the wealthy stranger may flee the country? Let’s suppose instead that the wealthy stranger caps your winnings at $2^{40}$, so if the game lasts more than 40 rounds you will get this amount rather than walking away empty-handed. Now your expected value is

$E(X)=\sum_{n=1}^{40}\frac{1}{2^{n}}\cdot 2^{n}+\sum_{n=41}^{\infty}\frac{1}{2^{n}}\cdot 2^{40}=40+1=41,$

an increase of only $1 from the previous scenario. The $\infty$ in the St. Petersburg paradox is driven by an infinite “tail” of extremely rare events where you get extremely large payoffs. Cutting off this tail at some point, which makes sense in the real world, dramatically reduces the expected value of the game. ∎