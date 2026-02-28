Random variables and their distributions

The next two examples show seemingly dissimilar scenarios that are nonetheless isomorphic to the urn story.

Example 3.4.3 (Elk capture-recapture). A forest has  $N$  elk. Today,  $m$  of the elk are captured, tagged, and released into the wild. At a later date,  $n$  elk are recaptured at random. Assume that the recaptured elk are equally likely to be any set of  $n$  of the elk, e.g., an elk that has been captured does not learn how to avoid being captured again.

By the story of the Hypergeometric, the number of tagged elk in the recaptured sample is  $\mathrm{HGeom}(m,N - m,n)$ . The  $m$  tagged elk in this story correspond to the white balls and the  $N - m$  untagged elk correspond to the black balls. Instead of sampling  $n$  balls from the urn, we recapture  $n$  elk from the forest.

Example 3.4.4 (Aces in a poker hand). In a five-card hand drawn at random from a well-shuffled standard deck, the number of aces in the hand has the HGeom(4, 48, 5) distribution, which can be seen by thinking of the aces as white balls and the non-aces as black balls. Using the Hypergeometric PMF, the probability that the hand has exactly three aces is

$$
\frac {\binom {4} {3} \binom {4 8} {2}}{\binom {5 2} {5}} \approx 0. 0 0 1 7.
$$

The following table summarizes how the above examples can be thought of in terms of two sets of tags. In each example, the r.v. of interest is the number of items falling into both the second and the fourth columns: white and sampled, tagged and recaptured, ace and in one's hand.

|  Story | First set of tags |   | Second set of tags  |   |
| --- | --- | --- | --- | --- |
|  urn | white | black | sampled | not sampled  |
|  elk | tagged | untagged | recaptured | not recaptured  |
|  cards | ace | not ace | in hand | not in hand  |

The next theorem describes a symmetry between two Hypergeometric distributions with different parameters; the proof follows from swapping the two sets of tags in the Hypergeometric story.

Theorem 3.4.5. The  $\mathrm{HGeom}(w,b,n)$  and  $\mathrm{HGeom}(n,w + b - n,w)$  distributions are identical. That is, if  $X\sim \mathrm{HGeom}(w,b,n)$  and  $Y\sim \mathrm{HGeom}(n,w + b - n,w)$ , then  $X$  and  $Y$  have the same distribution.

Proof. Using the story of the Hypergeometric, imagine an urn with  $w$  white balls,  $b$  black balls, and a sample of size  $n$  made without replacement. Let  $X \sim \mathrm{HGeom}(w, b, n)$  be the number of white balls in the sample, thinking of white/black as the first set of tags and sampled/not sampled as the second set of tags. Let  $Y \sim \mathrm{HGeom}(n, w + b - n, w)$  be the number of sampled balls among the white balls, thinking of sampled/not sampled as the first set of tags and white/black as