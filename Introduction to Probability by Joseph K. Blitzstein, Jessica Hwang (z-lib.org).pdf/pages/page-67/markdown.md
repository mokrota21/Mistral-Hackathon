- It assumes that gender is binary, so that each child can be definitively categorized as a boy or a girl. In fact, many people don’t neatly fit into either of the categories “male” or “female”, and identify themselves as having a non-binary gender.
- It assumes that $P(\text{boy})=P(\text{girl})$, both for the elder child and for the younger child. In fact, in most countries slightly more boys are born than girls. For example, in the United States it is commonly estimated that 105 boys are born for every 100 girls who are born.
- It assumes that the genders of the two children are independent, i.e., knowing the elder child’s gender gives no information about the younger child’s gender, and vice versa. This would be unrealistic if, e.g., the children were identical twins.

Under these (admittedly problematic) simplifying assumptions, we can solve the problem as follows.

*Solution*:

With the assumptions listed above, the definition of conditional probability gives

$P(\text{both girls}|\text{elder is a girl})=\frac{P(\text{both girls, elder is a girl})}{P(\text{elder is a girl})}=\frac{1/4}{1/2}=1/2,$
$P(\text{both girls}|\text{at least one girl})=\frac{P(\text{both girls, at least one girl})}{P(\text{at least one girl})}=\frac{1/4}{3/4}=1/3.$

(We solved the second part of the problem in terms of girls rather than boys to make it a bit easier to compare the two parts of the problem.) It may seem counterintuitive that the two results are different, since there is no reason for us to care whether the elder child is a girl as opposed to the younger child. Indeed, by symmetry,

$P(\text{both girls}|\text{younger is a girl})=P(\text{both girls}|\text{elder is a girl})=1/2.$

However, there is no such symmetry between the conditional probabilities $P(\text{both girls}|\text{elder is a girl})$ and $P(\text{both girls}|\text{at least one girl})$. Saying that the elder child is a girl designates a *specific* child, and then the other child (the younger child) has a 50% chance of being a girl. “At least one” does *not* refer to a specific child. Conditioning on a specific child being a girl knocks away 2 of the 4 “pebbles” in the sample space $\{GG,GB,BG,BB\}$, where, for example, $GB$ means the elder child is a girl and the younger child is a boy. In contrast, conditioning on at least one child being a girl knocks away only $BB$. ∎

###### Example 2.2.6 (Random child is a girl).

A family has two children. You randomly run into one of the two, and learn that she is a girl. With assumptions as in the previous example, what is the conditional probability that both are girls? Also assume that you are equally likely to run into either child, and that which one you run into has nothing to do with gender.