and A starts out with much less money than B, then A’s chance of winning the game is low. Having $p<1/2$ may also make A’s chance of winning low, even if $p$ is only a little bit less than $1/2$ and the players start out with the same amount of money. For example, if $p=0.49$ and each player starts out with $100, then A has only about a 1.8% chance of winning the game.

We have focused on the probability of A winning the game, but what about B? Rather than starting from scratch, we can use *symmetry*: aside from notation, there is nothing in the description of the game to distinguish A from B. By symmetry, the probability of B winning from a starting wealth of $N-i$ is obtained by switching the roles of $q$ and $p$, and of $i$ and $N-i$. This gives

\[ P(\text{B wins}|\text{B starts at }N-i)=\left\{\begin{array}[]{ll}\frac{1-\left(\frac{p}{q}\right)^{N-i}}{1-\left(\frac{p}{q}\right)^{N}}&\text{if }p\neq 1/2,\\
\frac{N-i}{N}&\text{if }p=1/2.\end{array}\right. \]

It can then be verified that for all $i$ and all $p$, $P(\text{A wins})+P(\text{B wins})=1$, so the game is guaranteed to end: the probability is 0 that it will oscillate forever. ∎

### 2.8 Pitfalls and paradoxes

The next two examples are fallacies of conditional thinking that have arisen in the legal context. The prosecutor’s fallacy is the confusion of $P(A|B)$ with $P(B|A)$; the defense attorney’s fallacy is the failure to condition on *all* the evidence.

###### 2.8.1 (Prosecutor’s fallacy).

In 1998, Sally Clark was tried for murder after two of her sons died shortly after birth. During the trial, an expert witness for the prosecution testified that the probability of a newborn dying of sudden infant death syndrome (SIDS) was $1/8500$, so the probability of two deaths due to SIDS in one family was $(1/8500)^{2}$, or about one in 73 million. Therefore, he continued, the probability of Clark’s innocence was one in 73 million.

There are at least two major problems with this line of reasoning. First, the expert witness found the probability of the intersection of “first son dies of SIDS” and “second son dies of SIDS” by multiplying the individual event probabilities; as we know, this is only valid if deaths due to SIDS are *independent* within a family. This independence would not hold if genetic or other family-specific risk factors cause all newborns within certain families to be at increased risk of SIDS.

Second, the so-called expert has confused two different conditional probabilities: $P(\text{innocence}|\text{evidence})$ is different from $P(\text{evidence}|\text{innocence})$. The witness claims that the probability of observing two newborn deaths if the defendant were innocent is extremely low; that is, $P(\text{evidence}|\text{innocence})$ is small. What we are interested in,