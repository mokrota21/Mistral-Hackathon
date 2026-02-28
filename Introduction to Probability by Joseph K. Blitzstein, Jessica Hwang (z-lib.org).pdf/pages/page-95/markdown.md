The above equations express $P(A|B)$ as a weighted average of $P(A|C,B)$ and $P(A|C^{c},B)$, and $P(A|B^{c})$ as a weighted average of $P(A|C,B^{c})$ and $P(A|C^{c},B^{c})$. If the corresponding weights were the same in both of these weighted averages, then Simpson’s paradox could not occur. But the weights here are *different*:

$P(C|B)<P(C|B^{c})\mbox{ and }P(C^{c}|B)>P(C^{c}|B^{c}),$

since Dr. Nick is much less likely than Dr. Hibbert to be performing a heart surgery.

Although we have

$P(A|C,B)<P(A|C,B^{c})$

and

$P(A|C^{c},B)<P(A|C^{c},B^{c}),$

the fact that the weights are so different results in the inequality flipping when we do not condition on whether or not $C$ occurred:

$P(A|B)>P(A|B^{c}).$

Numerically, the two weighted averages are

$P(A|B)$ $=$ $0.83=(2/10)\cdot 0.1+(81/90)\cdot 0.9$
$P(A|B^{c})$ $=$ $0.80=(70/90)\cdot 0.9+(10/10)\cdot 0.1.$

The first equation (corresponding to Dr. Nick) puts much more weight on the second term (corresponding to the easier surgery) than does the second equation.

Aggregation across different types of surgeries presents a misleading picture of the doctors’ abilities because we lose the information about which doctor tends to perform which type of surgery. When we think *confounding variables* like surgery type could be at play, we should examine the disaggregated data to see what is really going on.

Simpson’s paradox arises in many real-world contexts. In the following examples, you should try to identify the events $A$, $B$, and $C$ that create the paradox.

- *Gender discrimination in college admissions*: In the 1970s, men were significantly more likely than women to be admitted for graduate study at the University of California, Berkeley, leading to charges of gender discrimination. Yet within most individual departments, women were admitted at a higher rate than men. It was found that women tended to apply to the departments with more competitive admissions, while men tended to apply to less competitive departments.
- *Baseball batting averages*: It is possible for player 1 to have a higher batting average than player 2 in the first half of a baseball season *and* a higher batting average than player 2 in the second half of the season, yet have a lower overall batting average for the entire season. It depends on how many at-bats the players have in each half of the season. (An *at-bat* is when it’s a player’s turn to try to hit the ball; the player’s *batting average* is the number of hits the player gets divided by the player’s number of at-bats.)