Probability and counting

for some $c$, then we can adjust by dividing by $c$. For example, if we have exactly double-counted each possibility, we can divide by 2 to get the correct count. We call this *adjusting for overcounting*.

###### Example 1.4.13 (Committees and teams).

Consider a group of four people.

(a) How many ways are there to choose a two-person committee?

(b) How many ways are there to break the people into two teams of two?

Solution:

(a) One way to count the possibilities is by listing them out: labeling the people as 1, 2, 3, 4, the possibilities are $\boxed{12}$, $\boxed{13}$, $\boxed{14}$, $\boxed{23}$, $\boxed{24}$, $\boxed{34}$.

Another approach is to use the multiplication rule with an adjustment for overcounting. By the multiplication rule, there are 4 ways to choose the first person on the committee and 3 ways to choose the second person on the committee, but this counts each possibility twice, since picking 1 and 2 to be on the committee is the same as picking 2 and 1 to be on the committee. Since we have overcounted by a factor of 2, the number of possibilities is $(4\cdot 3)/2=6$.

(b) Here are 3 ways to see that there are 3 ways to form the teams. Labeling the people as $1,2,3,4$, we can directly list out the possibilities: $\boxed{12}\boxed{34}$, $\boxed{13}\boxed{24}$, and $\boxed{14}\boxed{23}$. Listing out all possibilities would quickly become tedious or infeasible with more people though. Another approach is to note that it suffices to specify person 1’s teammate (and then the other team is determined). A third way is to use (a) to see that there are 6 ways to choose one team. This overcounts by a factor of 2, since picking 1 and 2 to be a team is equivalent to picking 3 and 4 to be a team. So again the answer is $6/2=3$. $\square$

A *binomial coefficient* counts the number of subsets of a certain size for a set, such as the number of ways to choose a committee of size $k$ from a set of $n$ people. Sets and subsets are by definition *unordered*, e.g., $\{3,1,4\}=\{4,1,3\}$, so we are counting the number of ways to choose $k$ objects out of $n$, without replacement and without distinguishing between the different orders in which they could be chosen.

###### Definition 1.4.14 (Binomial coefficient).

For any nonnegative integers $k$ and $n$, the *binomial coefficient* $\binom{n}{k}$, read as “$n$ choose $k$”, is the number of subsets of size $k$ for a set of size $n$.

For example, $\binom{4}{2}=6$, as shown in Example 1.4.13. The binomial coefficient $\binom{n}{k}$ is sometimes called a *combination*, but we do not use that terminology here since “combination” is such a useful general-purpose word. Algebraically, binomial coefficients can be computed as follows.

###### Theorem 1.4.15 (Binomial coefficient formula).

For $k\leq n$, we have

$\binom{n}{k}=\frac{n(n-1)\cdots(n-k+1)}{k!}=\frac{n!}{(n-k)!k!}\cdot$