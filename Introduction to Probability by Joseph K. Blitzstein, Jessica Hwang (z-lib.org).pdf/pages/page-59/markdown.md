Find the probability that at least one molecule in the breath you just took was shared with Caesar’s last breath, and give a simple approximation in terms of $e$.

Hint: As discussed in the math appendix, $(1+\frac{x}{n})^{n}\approx e^{x}$ for $n$ large.
58. A widget inspector inspects 12 widgets and finds that exactly 3 are defective. Unfortunately, the widgets then get all mixed up and the inspector has to find the 3 defective widgets again by testing widgets one by one.

1. Find the probability that the inspector will now have to test at least 9 widgets.
2. Find the probability that the inspector will now have to test at least 10 widgets.
59. There are 15 chocolate bars and 10 children. In how many ways can the chocolate bars be distributed to the children, in each of the following scenarios?

1. The chocolate bars are fungible (interchangeable).
2. The chocolate bars are fungible, and each child must receive at least one.

Hint: First give each child a chocolate bar, and then decide what to do with the rest.

1. The chocolate bars are not fungible (it matters which particular bar goes where).
2. The chocolate bars are not fungible, and each child must receive at least one.

Hint: The strategy suggested in (b) does not apply. Instead, consider *randomly* giving the chocolate bars to the children, and apply inclusion-exclusion.
60. Given $n\geq 2$ numbers $(a_{1},a_{2},\ldots,a_{n})$ with no repetitions, a *bootstrap sample* is a sequence $(x_{1},x_{2},\ldots,x_{n})$ formed from the $a_{j}$’s by sampling with replacement with equal probabilities. Bootstrap samples arise in a widely used statistical method known as the *bootstrap*. For example, if $n=2$ and $(a_{1},a_{2})=(3,1)$, then the possible bootstrap samples are $(3,3),(3,1),(1,3)$, and $(1,1)$.

1. How many possible bootstrap samples are there for $(a_{1},\ldots,a_{n})$?

1. How many possible bootstrap samples are there for $(a_{1},\ldots,a_{n})$, if order does not matter (in the sense that it only matters how many times each $a_{j}$ was chosen, not the order in which they were chosen)?

1. One random bootstrap sample is chosen (by sampling from $a_{1},\ldots,a_{n}$ with replacement, as described above). Show that not all unordered bootstrap samples (in the sense of (b)) are equally likely. Find an unordered bootstrap sample $\mathbf{b}_{1}$ that is as likely as possible, and an unordered bootstrap sample $\mathbf{b}_{2}$ that is as unlikely as possible. Let $p_{1}$ be the probability of getting $\mathbf{b}_{1}$ and $p_{2}$ be the probability of getting $\mathbf{b}_{2}$ (so $p_{i}$ is the probability of getting the *specific* unordered bootstrap sample $\mathbf{b}_{i}$). What is $p_{1}/p_{2}$? What is the ratio of the probability of getting an unordered bootstrap sample whose probability is $p_{1}$ to the probability of getting an unordered sample whose probability is $p_{2}$?
61. ⑧ There are 100 passengers lined up to board an airplane with 100 seats (with each seat assigned to one of the passengers). The first passenger in line crazily decides to sit in a randomly chosen seat (with all seats equally likely). Each subsequent passenger takes their assigned seat if available, and otherwise sits in a random available seat. What is the probability that the last passenger in line gets to sit in their assigned seat? (This is a common interview problem, and a beautiful example of the power of symmetry.)

Hint: Call the seat assigned to the $j$th passenger in line “seat $j$” (regardless of whether the airline calls it seat 23A or whatever). What are the possibilities for which seats are available to the last passenger in line, and what is the probability of each of these possibilities?