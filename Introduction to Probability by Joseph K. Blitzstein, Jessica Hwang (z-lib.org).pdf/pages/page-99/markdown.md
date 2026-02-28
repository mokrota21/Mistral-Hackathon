Following the frequentist interpretation, we count the number of repetitions where $B$ occurred and name it n.b, and we also count the number of repetitions where $A\cap B$ occurred and name it n.ab. Finally, we divide n.ab by n.b to approximate $P(A|B)$.

n.b <- sum(child1==1) n.ab <- sum(child1==1 & child2==1) n.ab/n.b

The ampersand & is an elementwise AND, so n.ab is the number of families where both the first child and the second child are girls. When we ran this code, we got 0.50, which agrees with $P(\text{both girls}|\text{elder is a girl})=1/2$.

Now let $A$ be the event that both children are girls and $B$ the event that at least one of the children is a girl. Then $A\cap B$ is the same, but n.b needs to count the number of families where at least one child is a girl. This is accomplished with the elementwise OR operator | (this is *not* a conditioning bar; it is an inclusive OR, returning TRUE if at least one element is TRUE).

n.b <- sum(child1==1 | child2==1) n.ab <- sum(child1==1 & child2==1) n.ab/n.b

We got 0.33, which agrees with $P(\text{both girls}|\text{at least one girl})=1/3$.

#### Monty Hall simulation

Many long, bitter debates about the Monty Hall problem could have been averted by *trying it out* with a simulation. To study how well the never-switch strategy performs, let’s generate $10^{5}$ runs of the Monty Hall game. To simplify notation, assume the contestant always chooses door 1. Then we can generate a vector specifying which door has the car for each repetition:

n <- 10^5 cardoor <- sample(3,n,replace=TRUE)

At this point we could generate the vector specifying which doors Monty opens, but that’s unnecessary since the never-switch strategy succeeds if and only if door 1 has the car! So the fraction of times when the never-switch strategy succeeds is sum(cardoor==1)/n, which was 0.334 in our simulation. This is very close to the true value, 1/3.

What if we want to *play* the Monty Hall game interactively? We can do this by programming a *function*. Entering the following code in R defines a function called monty, which can then be invoked by entering the command monty() any time you feel like playing the game!