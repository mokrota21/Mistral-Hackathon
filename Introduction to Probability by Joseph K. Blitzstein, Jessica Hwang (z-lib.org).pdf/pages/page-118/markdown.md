(b) Use the results from (a) to show that $p_{n+1}$ satisfies the following recursive equation:

$p_{n+1}=(a+b-1)p_{n}+a+b-2ab.$

(c) Use the result from (b) to find the long-run probability of success for this algorithm, $\lim_{n\to\infty}p_{n}$, assuming that this limit exists.
73. In humans (and many other organisms), genes come in pairs. A certain gene comes in two types (alleles): type $a$ and type $A$. The genotype of a person for that gene is the types of the two genes in the pair: $AA,Aa$, or $aa$ ($aA$ is equivalent to $Aa$). Assume that the Hardy-Weinberg law applies here, which means that the frequencies of $AA,Aa,aa$ in the population are $p^{2},2p(1-p),(1-p)^{2}$ respectively, for some $p$ with $0<p<1$.

When a woman and a man have a child, the child’s gene pair has one gene contributed by each parent. Suppose that the mother is equally likely to contribute either of the two genes in her gene pair, and likewise for the father, independently. Also suppose that the genotypes of the parents are independent of each other (with probabilities given by the Hardy-Weinberg law).

(a) Find the probabilities of each possible genotype $(AA,Aa,aa)$ for a child of two random parents. Explain what this says about stability of the Hardy-Weinberg law from one generation to the next.

Hint: Condition on the genotypes of the parents.

(b) A person of type $AA$ or $aa$ is called homozygous (for the gene under consideration), and a person of type $Aa$ is called heterozygous (for that gene). Find the probability that a child is homozygous, given that both parents are homozygous. Also, find the probability that a child is heterozygous, given that both parents are heterozygous.

(c) Suppose that having genotype $aa$ results in a distinctive physical characteristic, so it is easy to tell by looking at someone whether or not they have that genotype. A mother and father, neither of whom are of type $aa$, have a child. The child is also not of type $aa$. Given this information, find the probability that the child is heterozygous.

Hint: Use the definition of conditional probability. Then expand both the numerator and the denominator using LOTP, conditioning on the genotypes of the parents.
74. A standard deck of cards will be shuffled and then the cards will be turned over one at a time until the first ace is revealed. Let $B$ be the event that the next card in the deck will also be an ace.

(a) Intuitively, how do you think $P(B)$ compares in size with $1/13$ (the overall proportion of aces in a deck of cards)? Explain your intuition. (Give an intuitive discussion rather than a mathematical calculation; the goal here is to describe your intuition explicitly.)

(b) Let $C_{j}$ be the event that the first ace is at position $j$ in the deck. Find $P(B|C_{j})$ in terms of $j$, fully simplified.

(c) Using the law of total probability, find an expression for $P(B)$ as a sum. (The sum can be left unsimplified, but it should be something that could easily be computed in software such as R that can calculate sums.)

(d) Find a fully simplified expression for $P(B)$ using a symmetry argument.

Hint: If you were deciding whether to bet on the next card after the first ace being an ace or to bet on the last card in the deck being an ace, would you have a preference?