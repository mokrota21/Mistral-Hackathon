Introduction to Probability

# Named distributions

15. Find the CDF of an r.v. $X\sim\mathrm{DUnif}(1,2,\ldots,n).$

16. Let $X\sim\mathrm{DUnif}(C)$, and $B$ be a nonempty subset of $C$. Find the conditional distribution of $X$, given that $X$ is in $B$.

17. An airline overbooks a flight, selling more tickets for the flight than there are seats on the plane (figuring that it’s likely that some people won’t show up). The plane has 100 seats, and 110 people have booked the flight. Each person will show up for the flight with probability 0.9, independently. Find the probability that there will be enough seats for everyone who shows up for the flight.

18. $\circledS$ (a) In the World Series of baseball, two teams (call them A and B) play a sequence of games against each other, and the first team to win four games wins the series. Let $p$ be the probability that A wins an individual game, and assume that the games are independent. What is the probability that team A wins the series?

(b) Give a clear intuitive explanation of whether the answer to (a) depends on whether the teams always play 7 games (and whoever wins the majority wins the series), or the teams stop playing more games as soon as one team has won 4 games (as is actually the case in practice: once the match is decided, the two teams do not keep playing more games).

19. In a chess tournament, $n$ games are being played, independently. Each game ends in a win for one player with probability 0.4 and ends in a draw (tie) with probability 0.6. Find the PMFs of the number of games ending in a draw, and of the number of players whose games end in draws.

20. Suppose that a lottery ticket has probability $p$ of being a winning ticket, independently of other tickets. A gambler buys 3 tickets, hoping this will triple the chance of having at least one winning ticket.

(a) What is the distribution of how many of the 3 tickets are winning tickets?

(b) Show that the probability that at least 1 of the 3 tickets is winning is $3p - 3p^{2} + p^{3}$, in two different ways: by using inclusion-exclusion, and by taking the complement of the desired event and then using the PMF of a certain named distribution.

(c) Show that the gambler’s chances of having at least one winning ticket do not quite triple (compared with buying only one ticket), but that they do approximately triple if $p$ is small.

21. $\circledS$ Let $X \sim \operatorname{Bin}(n, p)$ and $Y \sim \operatorname{Bin}(m, p)$, independent of $X$. Show that $X - Y$ is not Binomial.

22. There are two coins, one with probability $p_1$ of Heads and the other with probability $p_2$ of Heads. One of the coins is randomly chosen (with equal probabilities for the two coins). It is then flipped $n \geq 2$ times. Let $X$ be the number of times it lands Heads.

(a) Find the PMF of $X$.

(b) What is the distribution of $X$ if $p_1 = p_2$?

(c) Give an intuitive explanation of why $X$ is not Binomial for $p_1 \neq p_2$ (its distribution is called a mixture of two Binomials). You can assume that $n$ is large for your explanation, so that the frequentist interpretation of probability can be applied.

23. There are $n$ people eligible to vote in a certain election. Voting requires registration. Decisions are made independently. Each of the $n$ people will register with probability $p_1$. Given that a person registers, they will vote with probability $p_2$. Given that a person votes, they will vote for Kodos (who is one of the candidates) with probability $p_3$. What is the distribution of the number of votes for Kodos (give the PMF, fully simplified, or the name of the distribution, including its parameters)?