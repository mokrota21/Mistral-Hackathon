Solution:

Intuitively, the answer should be $1/2$: imagine that the child we encountered is in front of us and the other is at home. Both being girls just says that the child who is at home is a girl, which seems to have nothing to do with the fact that the child in front of us is a girl. But let us check this more carefully, using the definition of conditional probability. This is also good practice with writing events in set notation.

Let $G_{1},G_{2}$, and $G_{3}$ be the events that the elder, younger, and random child is a girl, respectively. By assumption, $P(G_{1})=P(G_{2})=P(G_{3})=1/2$ . By the naive definition, or by independence as explained in Section 2.5, $P(G_{1}\cap G_{2})=1/4$. Thus,

$P(G_{1}\cap G_{2}|G_{3})=P(G_{1}\cap G_{2}\cap G_{3})/P(G_{3})=(1/4)/(1/2)=1/2,$

since $G_{1}\cap G_{2}\cap G_{3}=G_{1}\cap G_{2}$ (if both children are girls, it guarantees that the random child is a girl).

Keep in mind though that in order to arrive at $1/2$, an assumption was needed about how the random child was selected. In statistical language, we say that we collected a *random sample*; here the sample consists of one of the two children. One of the most important principles in statistics is that it is essential to think carefully about how the sample was collected, not just stare at the raw data without understanding where they came from. To take a simple extreme case, suppose that a repressive law forbids a boy from leaving the house if he has a sister. Then “the random child is a girl” is equivalent to “at least one of the children is a girl”, so the problem reduces to the first part of Example 2.2.5. ∎

###### Example 2.2.7 (A girl born in winter).

A family has two children. Find the probability that both children are girls, given that at least one of the two is a girl who was born in winter. In addition to the assumptions from Example 2.2.5, assume that the four seasons are equally likely and that gender is independent of season. (This means that knowing the gender gives no information about the probabilities of the seasons, and vice versa; see Section 2.5 for much more about independence.)

*Solution*:

By definition of conditional probability,

$P(\text{both girls}|\text{at least one winter girl})=\frac{P(\text{both girls, at least one winter girl})}{P(\text{at least one winter girl})}.$

Since the probability that a specific child is a winter-born girl is $1/8$, the denominator equals

$P(\text{at least one winter girl})=1-(7/8)^{2}.$

To compute the numerator, use the fact that “both girls, at least one winter girl” is the same event as “both girls, at least one winter child”; then use the assumption