Conditional probability

(a) Show that if the disease is rare, both for exposed people and for unexposed people, then the relative risk is approximately equal to the odds ratio.

(b) Let $p_{ij}$ for $i = 0,1$ and $j = 0,1$ be the probabilities in the following $2 \times 2$ table.

|   | D | D^{c}  |
| --- | --- | --- |
|  C | p_{11} | p_{10}  |
|  C^{c} | p_{01} | p_{00}  |

For example, $p_{10} = P(C, D^c)$. Show that the odds ratio can be expressed as a cross-product ratio, in the sense that

$$
\mathrm{OR} = \frac{p_{11} p_{00}}{p_{10} p_{01}}.
$$

(c) Show that the odds ratio has the neat symmetry property that the roles of $C$ and $D$ can be swapped without changing the value:

$$
\mathrm{OR} = \frac{\mathrm{odds}(C|D)}{\mathrm{odds}(C|D^c)}.
$$

This property is one of the main reasons why the odds ratio is so widely used, since it turns out that it allows the odds ratio to be estimated in a wide variety of problems where relative risk would be hard to estimate well.

69. A researcher wants to estimate the percentage of people in some population who have used illegal drugs, by conducting a survey. Concerned that a lot of people would lie when asked a sensitive question like “Have you ever used illegal drugs?”, the researcher uses a method known as randomized response. A hat is filled with slips of paper, each of which says either “I have used illegal drugs” or “I have not used illegal drugs”. Let $p$ be the proportion of slips of paper that say “I have used illegal drugs” ($p$ is chosen by the researcher in advance).

Each participant chooses a random slip of paper from the hat and answers (truthfully) “yes” or “no” to whether the statement on that slip is true. The slip is then returned to the hat. The researcher does not know which type of slip the participant had. Let $y$ be the probability that a participant will say “yes”, and $d$ be the probability that a participant has used illegal drugs.

(a) Find $y$, in terms of $d$ and $p$.

(b) What would be the worst possible choice of $p$ that the researcher could make in designing the survey? Explain.

(c) Now consider the following alternative system. Suppose that proportion $p$ of the slips of paper say “I have used illegal drugs”, but that now the remaining $1 - p$ say “I was born in winter” rather than “I have not used illegal drugs”. Assume that $1/4$ of people are born in winter, and that a person’s season of birth is independent of whether they have used illegal drugs. Find $d$, in terms of $y$ and $p$.

70. At the beginning of the play Rosencrantz and Guildenstern Are Dead by Tom Stoppard [25], Guildenstern is spinning coins and Rosencrantz is betting on the outcome for each. The coins have been landing Heads over and over again, prompting the following remark:

Guildenstern: A weaker man might be moved to re-examine his faith, if in nothing else at least in the law of probability.

The coin spins have resulted in Heads 92 times in a row.

(a) Fred and his friend are watching the play. Upon seeing the events described above, they have the following conversation: