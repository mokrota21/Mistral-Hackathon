(c) Bob runs the 1st program and $M_{1}$ occurs. He updates his probabilities and then runs the 2nd program. Let $\tilde{P}(A)=P(A|M_{1})$ be the updated probability function after running the 1st program. Explain briefly in words whether or not $\tilde{P}(L|M_{2})=P(L|M_{1}\cap M_{2})$: is conditioning on $M_{1}\cap M_{2}$ in one step equivalent to first conditioning on $M_{1}$, then updating probabilities, and then conditioning on $M_{2}$?
27. Suppose that there are 5 blood types in the population, named type 1 through type 5, with probabilities $p_{1},p_{2},\ldots,p_{5}$. A crime was committed by two individuals. A suspect, who has blood type 1, has prior probability $p$ of being guilty. At the crime scene, blood evidence is collected, which shows that one of the criminals has type 1 and the other has type 2.

Find the posterior probability that the suspect is guilty, given the evidence. Does the evidence make it more likely or less likely that the suspect is guilty, or does this depend on the values of the parameters $p,p_{1},\ldots,p_{5}$? If it depends on these values, give a simple criterion for when the evidence makes it more likely that the suspect is guilty.
28. Fred has just tested positive for a certain disease.

(a) Given this information, find the posterior odds that he has the disease, in terms of the prior odds, the sensitivity of the test, and the specificity of the test.

(b) Not surprisingly, Fred is much more interested in $P(\text{have disease}|\text{test positive})$, known as the positive predictive value, than in the sensitivity $P(\text{test positive}|\text{have disease})$. A handy rule of thumb in biostatistics and epidemiology is as follows:

For a rare disease and a reasonably good test, specificity matters much more than sensitivity in determining the positive predictive value.

Explain intuitively why this rule of thumb works. For this part you can make up some specific numbers and interpret probabilities in a frequentist way as proportions in a large population, e.g., assume the disease afflicts 1% of a population of 10000 people and then consider various possibilities for the sensitivity and specificity.
29. A family has two children. Let $C$ be a characteristic that a child can have, and assume that each child has characteristic $C$ with probability $p$, independently of each other and of gender. For example, $C$ could be the characteristic “born in winter” as in Example 2.2.7. Under the assumptions of Example 2.2.5, show that the probability that both children are girls given that at least one is a girl with characteristic $C$ is $\frac{2-p}{4-p}$. Note that this is $1/3$ if $p=1$ (agreeing with the first part of Example 2.2.5) and approaches $1/2$ from below as $p\to 0$ (agreeing with Example 2.2.7).

### Independence and conditional independence

30. $\circledS$ A family has 3 children, creatively named $A,B$, and $C$.

(a) Discuss intuitively (but clearly) whether the event “$A$ is older than $B$” is independent of the event “$A$ is older than $C$”.

(b) Find the probability that $A$ is older than $B$, given that $A$ is older than $C$.
31. $\circledS$ Is it possible that an event is independent of itself? If so, when is this the case?
32. $\circledS$ Consider four nonstandard dice (the Efron dice), whose sides are labeled as follows (the 6 sides on each die are equally likely).

A: $4,4,4,4,0,0$

B: $3,3,3,3,3,3$

C: $6,6,2,2,2,2$