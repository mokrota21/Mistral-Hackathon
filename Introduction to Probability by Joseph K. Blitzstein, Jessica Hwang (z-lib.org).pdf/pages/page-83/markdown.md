Introduction to Probability

To state this formally, let $F$ be the event that we’ve chosen the fair coin, and let $A_{1}$ and $A_{2}$ be the events that the first and second coin tosses land Heads. Conditional on $F$, $A_{1}$ and $A_{2}$ are independent, but $A_{1}$ and $A_{2}$ are not unconditionally independent because $A_{1}$ provides information about $A_{2}$. ∎

###### Example 2.5.11 (Independence doesn’t imply conditional independence).

My friends Alice and Bob are the only two people who ever call me on the phone. Each day, they decide independently whether to call me that day. Let $A$ be the event that Alice calls me next Friday and $B$ be the event that Bob calls me next Friday. Assume $A$ and $B$ are unconditionally independent with $P(A)&gt;0$ and $P(B)&gt;0$.

However, given that I receive exactly one call next Friday, $A$ and $B$ are no longer independent: the call is from Alice if and only if it is not from Bob. In other words, letting $C$ be the event that I receive exactly one call next Friday, $P(B|C)&gt;0$ while $P(B|A,C)=0$, so $A$ and $B$ are not conditionally independent given $C$. ∎

###### Example 2.5.12.

(Why is the baby crying?) A certain baby cries if and only if she is hungry, tired, or both. Let $C$ be the event that the baby is crying, $H$ be the event that she is hungry, and $T$ be the event that she is tired. Let $P(C)=c,P(H)=h$, and $P(T)=t$, where none of $c,h,t$ are equal to 0 or 1. Let $H$ and $T$ be independent.

(a) Find $c$, in terms of $h$ and $t$.

(b) Find $P(H|C),P(T|C)$, and $P(H,T|C)$.

(c) Are $H$ and $T$ conditionally independent given $C$? Explain in two ways: algebraically using the quantities from (b), and with an intuitive explanation in words.

Solution:

(a) Since $H$ and $T$ are independent, we have

$P(C)=P(H\cup T)=P(H)+P(T)-P(H\cap T)=h+t-ht$.

(b) By Bayes’ rule,

$P(H|C)$ $=\frac{P(C|H)P(H)}{P(C)}=\frac{h}{c},$

$P(T|C)$ $=\frac{P(C|T)P(T)}{P(C)}=\frac{t}{c},$

$P(H,T|C)$ $=\frac{P(C|H,T)P(H,T)}{P(C)}=\frac{ht}{c}.$

(c) No, $H$ and $T$ are not conditionally independent given $C$, since

$P(H,T|C)=\frac{ht}{c}&lt;\frac{ht}{c^{2}}=P(H|C)P(T|C).$

We can also see intuitively why they are not conditionally independent given $C$: if the baby is crying but not hungry, she must be tired.