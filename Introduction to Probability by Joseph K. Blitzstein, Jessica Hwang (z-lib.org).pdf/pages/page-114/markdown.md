Conditional probability

For lab A, the probability of someone testing *positive* given that they *do* have the disease is $a_{1}$, and the probability of someone testing *negative* given that they do *not* have the disease is $a_{2}$. The corresponding probabilities for lab B are $b_{1}$ and $b_{2}$.

1. Find the probability that the patient has the disease, given that they tested positive.

2. Find the probability that the patient’s blood sample was analyzed by lab A, given that the patient tested positive.
6. Fred decides to take a series of $n$ tests, to diagnose whether he has a certain disease (any individual test is not perfectly reliable, so he hopes to reduce his uncertainty by taking multiple tests). Let $D$ be the event that he has the disease, $p=P(D)$ be the prior probability that he has the disease, and $q=1-p$. Let $T_{j}$ be the event that he tests positive on the $j$th test.

1. Assume for this part that the test results are conditionally independent given Fred’s disease status. Let $a=P(T_{j}|D)$ and $b=P(T_{j}|D^{c})$, where $a$ and $b$ don’t depend on $j$. Find the posterior probability that Fred has the disease, given that he tests positive on all $n$ of the $n$ tests.

2. Suppose that Fred tests positive on all $n$ tests. However, some people have a certain gene that makes them *always* test positive. Let $G$ be the event that Fred has the gene. Assume that $P(G)=1/2$ and that $D$ and $G$ are independent. If Fred does *not* have the gene, then the test results are conditionally independent given his disease status. Let $a_{0}=P(T_{j}|D,G^{c})$ and $b_{0}=P(T_{j}|D^{c},G^{c})$, where $a_{0}$ and $b_{0}$ don’t depend on $j$. Find the posterior probability that Fred has the disease, given that he tests positive on all $n$ of the tests.
6. A certain hereditary disease can be passed from a mother to her children. Given that the mother has the disease, her children independently will have it with probability $1/2$. Given that she doesn’t have the disease, her children won’t have it either. A certain mother, who has probability $1/3$ of having the disease, has two children.

1. Find the probability that neither child has the disease.

2. Is whether the elder child has the disease independent of whether the younger child has the disease? Explain.

3. The elder child is found not to have the disease. A week later, the younger child is also found not to have the disease. Given this information, find the probability that the mother has the disease.
6. Three fair coins are tossed at the same time. Explain what is wrong with the following argument: “there is a 50% chance that the three coins all landed the same way, since obviously it is possible to find two coins that match, and then the other coin has a 50% chance of matching those two”.
6. An urn contains red, green, and blue balls. Let $r,g,b$ be the proportions of red, green, blue balls, respectively ($r+g+b=1$).

1. Balls are drawn randomly *with replacement*. Find the probability that the first time a green ball is drawn is before the first time a blue ball is drawn.

Hint: Explain how this relates to finding the probability that a draw is green, given that it is either green or blue.

2. Balls are drawn randomly *without replacement*. Find the probability that the first time a green ball is drawn is before the first time a blue ball is drawn. Is the answer the same or different than the answer in (a)?

Hint: Imagine the balls all lined up, in the order in which they will be drawn. Note that where the red balls are standing in this line is irrelevant.