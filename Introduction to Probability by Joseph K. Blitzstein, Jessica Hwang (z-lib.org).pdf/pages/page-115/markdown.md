(c) Generalize the result from (a) to the following setting. Independent trials are performed, and the outcome of each trial is classified as being exactly one of type 1, type 2, …, or type $n$, with probabilities $p_{1},p_{2},\ldots,p_{n}$, respectively. Find the probability that the first trial to result in type $i$ comes before the first trial to result in type $j$, for $i\neq j$.
65. Marilyn vos Savant was asked the following question for her column in *Parade*:

> You’re at a party with 199 other guests when robbers break in and announce that they are going to rob one of you. They put 199 blank pieces of paper in a hat, plus one marked “you lose.” Each guest must draw, and the person who draws “you lose” will get robbed. The robbers offer you the option of drawing first, last, or at any time in between. When would you take your turn?

The draws are made *without replacement*, and for (a) are uniformly random.

1. Determine whether it is optimal to draw first, last, or somewhere in between (or whether it does not matter), to maximize the probability of not being robbed. Give a clear, concise, and compelling explanation.
2. More generally, suppose that there is one “you lose” piece of paper, with “weight” $v$, and there are $n$ blank pieces of paper, each with “weight” $w$. At each stage, draws are made with probability proportional to weight, i.e., the probability of drawing a particular piece of paper is its weight divided by the sum of the weights of all the remaining pieces of paper. Determine whether it is better to draw first or second (or whether it does not matter); here $v>0,w>0$, and $n\geq 1$ are known constants.
66. A fair die is rolled repeatedly, until the running total is at least 100 (at which point the rolling stops). Find the most likely value of the final running total (i.e., the value of the running total at the first time when it is at least 100).

Hint: Consider the possibilities for what the running total is just before the last roll.
67. Homer has a box of donuts, which currently contains exactly $c$ chocolate, $g$ glazed, and $j$ jelly donuts. Homer eats donuts one after another, each time choosing uniformly at random from the remaining donuts.

1. Find the probability that the last donut remaining in the box is a chocolate donut.
2. Find the probability of the following event: glazed is the first type of donut that Homer runs out of, and then jelly is the second type of donut that he runs out of.

Hint: Consider the last donut remaining, and the last donut that is either glazed or jelly.
68. Let $D$ be the event that a person develops a certain disease, and $C$ be the event that the person was exposed to a certain substance (e.g., $D$ may correspond to lung cancer and $C$ may correspond to smoking cigarettes). We are interested in whether exposure to the substance is related to developing the disease (and if so, how they are related).

The *odds ratio* is a very widely used measure in epidemiology of the association between disease and exposure, defined as

$\mathrm{OR}=\frac{\mathrm{odds}(D|C)}{\mathrm{odds}(D|C^{c})},$

where conditional odds are defined analogously to unconditional odds: $\mathrm{odds}(A|B)=\frac{P(A|B)}{P(A^{c}|B)}$. The *relative risk* of the disease for someone exposed to the substance, another widely used measure, is

$\mathrm{RR}=\frac{P(D|C)}{P(D|C^{c})}.$

The relative risk is especially easy to interpret, e.g., $\mathrm{RR}=2$ says that someone exposed to the substance is twice as likely to develop the disease as someone who isn’t exposed (though this does not necessarily mean that the substance *causes* the increased chance of getting the disease, nor is there necessarily a causal interpretation for the odds ratio).