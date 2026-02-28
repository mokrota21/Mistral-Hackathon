that gender and season are independent:

$P(\text{both girls, at least one winter girl})$ $=P(\text{both girls, at least one winter child})$
$=(1/4)P(\text{at least one winter child})$
$=(1/4)(1-P(\text{both are non-winter}))$
$=(1/4)(1-(3/4)^{2}).$

Thus,

$P(\text{both girls}|\text{at least one winter girl})=\frac{(1/4)(1-(3/4)^{2})}{1-(7/8)^{2}}=\frac{7/64}{15/64}=7/15.$

At first this result seems absurd! In Example 2.2.5, the result was that the conditional probability of both children being girls, given that at least one is a girl, is 1/3; why should it be any different when we learn that at least one is a winter-born girl? The point is that information about the birth season brings “at least one is a girl” closer to “a specific one is a girl”. Conditioning on more and more specific information brings the probability closer and closer to 1/2.

For example, conditioning on “at least one is a girl who was born on a March 31 at 8:20 pm” comes very close to specifying a child, and learning information about a specific child does not give us information about the other child. The seemingly irrelevant information such as season of birth interpolates between the two parts of Example 2.2.5. Exercise 29 generalizes this example to an arbitrary characteristic that is independent of gender. $\square$

### 2.3 Bayes’ rule and the law of total probability

The definition of conditional probability is simple—just a ratio of two probabilities—but it has far-reaching consequences. The first consequence is obtained easily by moving the denominator in the definition to the other side of the equation.

###### Theorem 2.3.1 (Probability of the intersection of two events).

For any events $A$ and $B$ with positive probabilities,

$P(A\cap B)=P(B)P(A|B)=P(A)P(B|A).$

This follows from taking the definition of $P(A|B)$ and multiplying both sides by $P(B)$, and then taking the definition of $P(B|A)$ and multiplying both sides by $P(A)$. At first sight this theorem may not seem very useful: it *is* the definition of conditional probability, just written slightly differently, and anyway it seems circular to use $P(A|B)$ to help find $P(A\cap B)$ when $P(A|B)$ was defined in terms of $P(A\cap B)$. But we will see that the theorem is in fact very useful, since it often turns out to be