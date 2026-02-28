Conditional probability

however, is $P(\mathrm{innocence}|\mathrm{evidence})$, the probability that the defendant is innocent given all the evidence. By Bayes’ rule,

$P(\mathrm{innocence}|\mathrm{evidence})=\frac{P(\mathrm{evidence}|\mathrm{innocence})P(\mathrm{innocence})}{P(\mathrm{evidence})},$

so to calculate the conditional probability of innocence given the evidence, we must take into account $P(\mathrm{innocence})$, the prior probability of innocence. This probability is extremely high: although double deaths due to SIDS are rare, so are double infanticides! Expanding the denominator as

$P(\mathrm{evidence}|\mathrm{innocence})P(\mathrm{innocence})+P(\mathrm{evidence}|\mathrm{guilt})P(\mathrm{guilt}),$

note that if $P(\mathrm{guilt})$ is small enough so that the second term is negligible compared to the first term, then the denominator of $P(\mathrm{innocence}|\mathrm{evidence})$ is approximately equal to the numerator, making $P(\mathrm{innocence}|\mathrm{evidence})$ close to 1.

The posterior probability of innocence given the evidence depends strongly on both $P(\mathrm{evidence}|\mathrm{innocence})$, which is very low, and $P(\mathrm{innocence})$, which is very high. The expert’s probability of $(1/8500)^{2}$, questionable in and of itself, is only part of the equation.

Sadly, Clark was convicted of murder and sent to prison, partly based on the expert’s wrongheaded testimony, and spent over three years in jail before her conviction was overturned. The outcry over the misuse of conditional probability in the Sally Clark case led to the review of hundreds of other cases where similar faulty logic was used by the prosecution.

$\nLeftrightarrow$ 2.8.2 (Defense attorney’s fallacy). A woman has been murdered, and her husband is put on trial for this crime. Evidence comes to light that the defendant had a history of abusing his wife. The defense attorney argues that the evidence of abuse should be excluded on grounds of irrelevance, since only 1 in 10,000 men with wives they abuse subsequently murder their wives. Should the judge grant the defense attorney’s motion to bar this evidence from trial?

Suppose that the defense attorney’s 1-in-10,000 figure is correct, and further assume the following for a relevant population of husbands and wives: 1 in 10 husbands abuse their wives, 1 in 5 murdered wives were murdered by their husbands, and 50% of husbands who murder their wives previously abused them. Also, assume that if the husband of a murdered wife is *not* guilty of the murder, then the probability that he abused his wife reverts to the unconditional probability of abuse.

How to define the “relevant population” and how to estimate such probabilities are difficult issues. For example, should we look at citywide, statewide, national, or international statistics? How should we account for unreported abuse and unsolved murders? What if murder rates are changing over time? For this problem, assume that a reasonable choice of the relevant population has been agreed on, and that the stated probabilities are known to be correct.