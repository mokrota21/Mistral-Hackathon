2.4 Conditional probabilities are probabilities

When we condition on an event $E$, we update our beliefs to be consistent with this knowledge, effectively putting ourselves in a universe where we know that $E$ occurred. Within our new universe, however, the laws of probability operate just as before. Conditional probability satisfies all the properties of probability! Therefore, any of the results we have derived about probability are still valid if we replace all unconditional probabilities with probabilities conditional on $E$. In particular:

- Conditional probabilities are between 0 and 1.
- $P(S|E)=1$, $P(\emptyset|E)=0$.
- If $A_{1},A_{2},\dots$ are disjoint, then $P(\cup_{j=1}^{\infty}A_{j}|E)=\sum_{j=1}^{\infty}P(A_{j}|E)$.
- $P(A^{c}|E)=1-P(A|E)$.
- Inclusion-exclusion: $P(A\cup B|E)=P(A|E)+P(B|E)-P(A\cap B|E)$.

###### 2.4.1.

When we write $P(A|E)$, it does *not* mean that $A|E$ is an event and we’re taking its probability; $A|E$ is not an event. Rather, $P(\cdot|E)$ is a probability function which assigns probabilities in accordance with the knowledge that $E$ has occurred, and $P(\cdot)$ is a different probability function which assigns probabilities without regard for whether $E$ has occurred or not. When we take an event $A$ and plug it into the $P(\cdot)$ function, we’ll get a number, $P(A)$; when we plug it into the $P(\cdot|E)$ function, we’ll get another number, $P(A|E)$, which incorporates the information (if any) provided by knowing that $E$ occurred.

To prove mathematically that conditional probabilities are probabilities, fix an event $E$ with $P(E)>0$, and for any event $A$, define $\tilde{P}(A)=P(A|E)$. This notation helps emphasize the fact that we are fixing $E$ and treating $P(\cdot|E)$ as our new probability function. We just need to check the two axioms of probability. First,

$\tilde{P}(\emptyset)=P(\emptyset|E)=\frac{P(\emptyset\cap E)}{P(E)}=0,\tilde{P}(S)=P(S|E)=\frac{P(S\cap E)}{P(E)}=1.$

Second, if $A_{1},A_{2},\dots$ are disjoint events, then

$\tilde{P}(A_{1}\cup A_{2}\cup\cdots)=\frac{P((A_{1}\cap E)\cup(A_{2}\cap E)\cup\cdots)}{P(E)}=\frac{\sum_{j=1}^{\infty}P(A_{j}\cap E)}{P(E)}=\sum_{j=1}^{\infty}\tilde{P}(A_{j}).$

So $\tilde{P}$ satisfies the axioms of probability.

Conversely, *all* probabilities can be thought of as conditional probabilities: whenever we make a probability statement, there is always some background information that we are conditioning on, even if we don’t state it explicitly. Consider the rain example from the beginning of this chapter. It would be natural to base the initial probability