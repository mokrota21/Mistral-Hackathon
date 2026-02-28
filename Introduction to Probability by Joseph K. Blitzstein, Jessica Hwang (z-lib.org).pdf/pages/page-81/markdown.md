###### Proposition 2.5.3.

If $A$ and $B$ are independent, then $A$ and $B^{c}$ are independent, $A^{c}$ and $B$ are independent, and $A^{c}$ and $B^{c}$ are independent.

###### Proof.

Let $A$ and $B$ be independent. We will first show that $A$ and $B^{c}$ are independent. If $P(A)=0$, then $A$ is independent of *every* event, including $B^{c}$. So assume $P(A)\neq 0$. Then

$P(B^{c}|A)=1-P(B|A)=1-P(B)=P(B^{c}),$

so $A$ and $B^{c}$ are independent. Swapping the roles of $A$ and $B$, we have that $A^{c}$ and $B$ are independent. Using the fact that $A,B$ independent implies $A,B^{c}$ independent, with $A^{c}$ playing the role of $A$, we also have that $A^{c}$ and $B^{c}$ are independent. ∎

We also often need to talk about independence of three or more events.

###### Definition 2.5.4 (Independence of three events).

Events $A$, $B$, and $C$ are said to be *independent* if all of the following equations hold:

$P(A\cap B)$ $=P(A)P(B),$
$P(A\cap C)$ $=P(A)P(C),$
$P(B\cap C)$ $=P(B)P(C),$
$P(A\cap B\cap C)$ $=P(A)P(B)P(C).$

If the first three conditions hold, we say that $A$, $B$, and $C$ are *pairwise independent*. Pairwise independence does *not* imply independence: it is possible that just learning about $A$ or just learning about $B$ is of no use in predicting whether $C$ occurred, but learning that *both* $A$ and $B$ occurred could still be highly relevant for $C$. Here is a simple example of this distinction.

###### Example 2.5.5 (Pairwise independence doesn’t imply independence).

Consider two fair, independent coin tosses, and let $A$ be the event that the first is Heads, $B$ the event that the second is Heads, and $C$ the event that both tosses have the same result. Then $A$, $B$, and $C$ are pairwise independent but not independent, since $P(A\cap B\cap C)=1/4$ while $P(A)P(B)P(C)=1/8$. The point is that just knowing about $A$ or just knowing about $B$ tells us nothing about $C$, but knowing what happened with *both* $A$ and $B$ gives us information about $C$ (in fact, in this case it gives us perfect information about $C$). ∎

On the other hand, $P(A\cap B\cap C)=P(A)P(B)P(C)$ does not imply pairwise independence; this can be seen quickly by looking at the extreme case $P(A)=0$, when the equation becomes $0=0$, which tells us nothing about $B$ and $C$.

We can define independence of any number of events similarly. Intuitively, the idea is that knowing what happened with any particular subset of the events gives us no information about what happened with the events not in that subset.