ing and working with events; Section A.1 of the math appendix provides a review of set theory. Set operations, especially unions, intersections, and complements, make it easy to build new events in terms of already-defined events. These concepts also let us express an event in more than one way; often, one expression for an event is much easier to work with than another expression for the same event.

For example, let $S$ be the sample space of an experiment and let $A,B\subseteq S$ be events. Then the union $A\cup B$ is the event that occurs if and only if *at least one* of $A,B$ occurs, the intersection $A\cap B$ is the event that occurs if and only if *both* $A$ and $B$ occur, and the complement $A^{c}$ is the event that occurs if and only if $A$ does *not* occur. We also have *De Morgan’s laws*:

$(A\cup B)^{c}=A^{c}\cap B^{c}\text{ and }(A\cap B)^{c}=A^{c}\cup B^{c},$

since saying that it is *not* the case that at least one of $A$ and $B$ occur is the same as saying that $A$ does not occur and $B$ does not occur, and saying that it is *not* the case that both occur is the same as saying that at least one does not occur. Analogous results hold for unions and intersections of more than two events.

In the example shown in Figure 1, $A$ is a set of 5 pebbles, $B$ is a set of 4 pebbles, $A\cup B$ consists of the 8 pebbles in $A$ or $B$ (including the pebble that is in both), $A\cap B$ consists of the pebble that is in both $A$ and $B$, and $A^{c}$ consists of the 4 pebbles that are not in $A$.

The notion of sample space is very general and abstract, so it is important to have some concrete examples in mind.

###### Example 1.2.2 (Coin flips).

A coin is flipped 10 times. Writing Heads as $H$ and Tails as $T$, a possible outcome (pebble) is $HHHTHHTTHT$, and the sample space is the set of all possible strings of length 10 of $H$’s and $T$’s. We can (and will) encode $H$ as 1 and $T$ as 0, so that an outcome is a sequence $(s_{1},\ldots,s_{10})$ with $s_{j}\in\{0,1\}$, and the sample space is the set of all such sequences. Now let’s look at some events:

1. Let $A_{1}$ be the event that the first flip is Heads. As a set,

$A_{1}=\{(1,s_{2},\ldots,s_{10}):s_{j}\in\{0,1\}\text{ for }2\leq j\leq 10\}.$

This is a subset of the sample space, so it is indeed an event; saying that $A_{1}$ occurs is the same thing as saying that the first flip is Heads. Similarly, let $A_{j}$ be the event that the $j$th flip is Heads for $j=2,3,\ldots,10$.

2. Let $B$ be the event that at least one flip was Heads. As a set,

$B=\bigcup_{j=1}^{10}A_{j}.$

3. Let $C$ be the event that all the flips were Heads. As a set,

$C=\bigcap_{j=1}^{10}A_{j}.$