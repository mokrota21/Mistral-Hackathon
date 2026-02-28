experiment. These must not be confused with posterior probabilities conditional on the evidence $A$.

###### Example 2.3.9 (Testing for a rare disease).

A patient named Fred is tested for a disease called conditionitis, a medical condition that afflicts 1% of the population. The test result is positive, i.e., the test claims that Fred has the disease. Let $D$ be the event that Fred has the disease and $T$ be the event that he tests positive.

Suppose that the test is “95% accurate”; there are different measures of the accuracy of a test, but in this problem it is assumed to mean that $P(T|D)=0.95$ and $P(T^{c}|D^{c})=0.95$. The quantity $P(T|D)$ is known as the sensitivity or true positive rate of the test, and $P(T^{c}|D^{c})$ is known as the specificity or true negative rate.

Find the conditional probability that Fred has conditionitis, given the evidence provided by the test result.

Solution:

Applying Bayes’ rule and the law of total probability, we have

$P(D|T)$ $=\frac{P(T|D)P(D)}{P(T)}$
$=\frac{P(T|D)P(D)}{P(T|D)P(D)+P(T|D^{c})P(D^{c})}$
$=\frac{0.95\cdot 0.01}{0.95\cdot 0.01+0.05\cdot 0.99}$
$\approx 0.16.$

So there is only a 16% chance that Fred has conditionitis, given that he tested positive, even though the test seems to be quite reliable!

Most people find it surprising to learn that the conditional probability of having the disease given a positive test result is only 16%, even though the test is 95% accurate (see Gigerenzer and Hoffrage *[13]*). The key to understanding this surprisingly low posterior probability of having the disease is to realize that there are two factors at play: the evidence from the test, and our prior information about the prevalence of the disease.

Although the test provides evidence in favor of disease, conditionitis is also a rare condition! The conditional probability $P(D|T)$ reflects a balance between these two factors, appropriately weighing the rarity of the disease against the rarity of a mistaken test result.

For further intuition, consider a population of 10000 people as illustrated in Figure 2.4, where 100 have conditionitis and 9900 don’t; this corresponds to a 1% disease rate. If we tested everybody in the population, we’d expect that out of the 100 diseased individuals, 95 would test positive and 5 would test negative. Out of the 9900 healthy individuals, we’d expect $(0.95)(9900)\approx 9405$ to test negative and 495 to test positive.