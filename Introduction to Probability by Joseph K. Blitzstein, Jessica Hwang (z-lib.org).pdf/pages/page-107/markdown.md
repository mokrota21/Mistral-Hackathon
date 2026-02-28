(b) Show that if $A$ and $B$ are independent and $C=A\cup B$, then $A$ and $B$ are conditionally dependent given $C$ (as long as $P(A\cap B)>0$ and $P(A\cup B)<1$), with

$P(A|B,C)<P(A|C).$

This phenomenon is known as Berkson’s paradox, especially in the context of admissions to a school, hospital, etc.
37. Two different diseases cause a certain weird symptom; anyone who has either or both of these diseases will experience the symptom. Let $D_{1}$ be the event of having the first disease, $D_{2}$ be the event of having the second disease, and $W$ be the event of having the weird symptom. Suppose that $D_{1}$ and $D_{2}$ are independent with $P(D_{j})=p_{j}$, and that a person with neither of these diseases will have the weird symptom with probability $w_{0}$. Let $q_{j}=1-p_{j}$, and assume that $0<p_{j}<1$.

(a) Find $P(W)$.

(b) Find $P(D_{1}|W),P(D_{2}|W)$, and $P(D_{1},D_{2}|W)$.

(c) Determine algebraically whether or not $D_{1}$ and $D_{2}$ are conditionally independent given $W$.

(d) Suppose for this part only that $w_{0}=0$. Give a clear, convincing intuitive explanation in words of whether $D_{1}$ and $D_{2}$ are conditionally independent given $W$.
38. We want to design a spam filter for email. As described in Exercise 1, a major strategy is to find phrases that are much more likely to appear in a spam email than in a non-spam email. In that exercise, we only consider one such phrase: “free money”. More realistically, suppose that we have created a list of 100 words or phrases that are much more likely to be used in spam than in non-spam.

Let $W_{j}$ be the event that an email contains the $j$th word or phrase on the list. Let

$p=P(\text{spam}),p_{j}=P(W_{j}|\text{spam}),r_{j}=P(W_{j}|\text{not spam}),$

where “spam” is shorthand for the event that the email is spam.

Assume that $W_{1},\ldots,W_{100}$ are conditionally independent given that the email is spam, and conditionally independent given that it is not spam. A method for classifying emails (or other objects) based on this kind of assumption is called a naive Bayes classifier. (Here “naive” refers to the fact that the conditional independence is a strong assumption, not to Bayes being naive. The assumption may or may not be realistic, but naive Bayes classifiers sometimes work well in practice even if the assumption is not realistic.)

Under this assumption we know, for example, that

$P(W_{1},W_{2},W_{3}^{c},W_{4}^{c},\ldots,W_{100}^{c}|\text{spam})=p_{1}p_{2}(1-p_{3})(1-p_{4})\ldots(1-p_{100}).$

Without the naive Bayes assumption, there would be vastly more statistical and computational difficulties since we would need to consider $2^{100}\approx 1.3\times 10^{30}$ events of the form $A_{1}\cap A_{2}\cdots\cap A_{100}$ with each $A_{j}$ equal to either $W_{j}$ or $W_{j}^{c}$. A new email has just arrived, and it includes the 23rd, 64th, and 65th words or phrases on the list (but not the other 97). So we want to compute

$P(\text{spam}|W_{1}^{c},\ldots,W_{22}^{c},W_{23},W_{24}^{c},\ldots,W_{63}^{c},W_{64},W_{65},W_{66}^{c},\ldots,W_{100}^{c}).$

Note that we need to condition on all the evidence, not just the fact that $W_{23}\cap W_{64}\cap W_{65}$ occurred. Find the conditional probability that the new email is spam (in terms of $p$ and the $p_{j}$ and $r_{j}$