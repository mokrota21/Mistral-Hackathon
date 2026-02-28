4. Each of $n$ balls is independently placed into one of $n$ boxes, with all boxes equally likely. What is the probability that exactly one box is empty?
5. A *norepeatword* is a sequence of at least one (and possibly all) of the usual 26 letters a,b,c,…,z, with repetitions not allowed. For example, “course” is a norepeatword, but “statistics” is not. Order matters, e.g., “course” is not the same as “source”.

A norepeatword is chosen randomly, with all norepeatwords equally likely. Show that the probability that it uses all 26 letters is very close to $1/e$.

### Axioms of probability

1. Show that for any events $A$ and $B$,

$P(A)+P(B)-1\leq P(A\cap B)\leq P(A\cup B)\leq P(A)+P(B).$

For each of these three inequalities, give a simple criterion for when the inequality is actually an equality (e.g., give a simple condition such that $P(A\cap B)=P(A\cup B)$ if and only if the condition holds).
2. Let $A$ and $B$ be events. The *difference* $B-A$ is defined to be the set of all elements of $B$ that are not in $A$. Show that if $A\subseteq B$, then

$P(B-A)=P(B)-P(A),$

directly using the axioms of probability.
3. Let $A$ and $B$ be events. The *symmetric difference* $A\triangle B$ is defined to be the set of all elements that are in $A$ or $B$ but not both. In logic and engineering, this event is also called the *XOR* (*exclusive or*) of $A$ and $B$. Show that

$P(A\triangle B)=P(A)+P(B)-2P(A\cap B),$

directly using the axioms of probability.
4. Let $A_{1},A_{2},\ldots,A_{n}$ be events. Let $B_{k}$ be the event exactly $k$ of the $A_{i}$ occur, and $C_{k}$ be the event that at least $k$ of the $A_{i}$ occur, for $0\leq k\leq n$. Find a simple expression for $P(B_{k})$ in terms of $P(C_{k})$ and $P(C_{k+1})$.
5. Events $A$ and $B$ are *independent* if $P(A\cap B)=P(A)P(B)$ (independence is explored in detail in the next chapter).

(a) Give an example of independent events $A$ and $B$ in a finite sample space $S$ (with neither equal to $\emptyset$ or $S$), and illustrate it with a Pebble World diagram.

(b) Consider the experiment of picking a random point in the rectangle

$R=\{(x,y):0<x<1,0<y<1\},$

where the probability of the point being in any particular region contained within $R$ is the area of that region. Let $A_{1}$ and $B_{1}$ be rectangles contained within $R$, with areas not equal to $0$ or $1$. Let $A$ be the event that the random point is in $A_{1}$, and $B$ be the event that the random point is in $B_{1}$. Give a geometric description of when it is true that $A$ and $B$ are independent. Also, give an example where they are independent and another example where they are not independent.

(c) Show that if $A$ and $B$ are independent, then

$P(A\cup B)=P(A)+P(B)-P(A)P(B)=1-P(A^{c})P(B^{c}).$