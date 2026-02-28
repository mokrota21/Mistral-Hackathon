This is a natural approach if we want to think of everything in our problem as being conditioned on $C$.

3. We can use Bayes’ rule with extra conditioning on $B$ to get

$P(A|B,C)=\frac{P(C|A,B)P(A|B)}{P(C|B)}.$

This is the same as the previous approach, except with the roles of $B$ and $C$ swapped. We mention it separately just to emphasize that it’s a bad idea to plug into a formula without thinking about which event should play which role.

It is both challenging and powerful that there are a variety of ways to approach this kind of conditioning problem.

### 2.5 Independence of events

We have now seen several examples where conditioning on one event changes our beliefs about the probability of another event. The situation where events provide no information about each other is called independence.

###### Definition 2.5.1 (Independence of two events).

Events $A$ and $B$ are independent if

$P(A\cap B)=P(A)P(B).$

If $P(A)>0$ and $P(B)>0$, then this is equivalent to

$P(A|B)=P(A),$

and also equivalent to $P(B|A)=P(B)$.

In words, two events are independent if we can obtain the probability of their intersection by multiplying their individual probabilities. Alternatively, $A$ and $B$ are independent if learning that $B$ occurred gives us no information that would change our probabilities for $A$ occurring (and vice versa).

Note that independence is a symmetric relation: if $A$ is independent of $B$, then $B$ is independent of $A$.

$\text{\text{✺ 2.5.2.}$ Independence is completely different from disjointness. If $A$ and $B$ are disjoint, then $P(A\cap B)=0$, so disjoint events can be independent only if $P(A)=0$ or $P(B)=0$. Knowing that $A$ occurs tells us that $B$ definitely did not occur, so $A$ clearly conveys information about $B$, meaning the two events are not independent (except if $A$ or $B$ already has zero probability).

Intuitively, it makes sense that if $A$ provides no information about whether or not $B$ occurred, then it also provides no information about whether or not $B^{c}$ occurred. We now prove a handy result along those lines.