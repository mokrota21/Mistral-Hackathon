- when the naive definition serves as a useful null model. In this setting, we assume that the naive definition applies just to see what predictions it would yield, and then we can compare observed data with predicted values to assess whether the hypothesis of equally likely outcomes is tenable.

### 1.4 How to count

Calculating the naive probability of an event $A$ involves counting the number of pebbles in $A$ and the number of pebbles in the sample space $S$. Often the sets we need to count are extremely large. This section introduces some fundamental methods for counting; further methods can be found in books on combinatorics, the branch of mathematics that studies counting.

#### 1.4.1 Multiplication rule

In some problems, we can directly count the number of possibilities using a basic but versatile principle called the multiplication rule. We’ll see that the multiplication rule leads naturally to counting rules for sampling with replacement and sampling without replacement, two scenarios that often arise in probability and statistics.

###### Theorem 1.4.1 (Multiplication rule).

Consider a compound experiment consisting of two sub-experiments, Experiment A and Experiment B. Suppose that Experiment A has $a$ possible outcomes, and for each of those outcomes Experiment B has $b$ possible outcomes. Then the compound experiment has $ab$ possible outcomes.

To see why the multiplication rule is true, imagine a tree diagram as in Figure 1.2. Let the tree branch $a$ ways according to the possibilities for Experiment A, and for each of those branches create $b$ further branches for Experiment B. Overall, there are $\underbrace{b+b+\cdots+b}_{a}=ab$ possibilities.

It is often easier to think about the experiments as being in chronological order, but there is no requirement in the multiplication rule that Experiment A has to be performed before Experiment B.

###### Example 1.4.3 (Runners).

Suppose that 10 people are running a race. Assume that ties are not possible and that all 10 will complete the race, so there will be well-defined first place, second place, and third place winners. How many possibilities are there for the first, second, and third place winners?

Solution: There are 10 possibilities for who gets first place, then once that is fixed there are 9 possibilities for who gets second place, and once these are both fixed