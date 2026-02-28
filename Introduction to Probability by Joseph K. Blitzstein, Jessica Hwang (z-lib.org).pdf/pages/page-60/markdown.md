62. In the birthday problem, we assumed that all 365 days of the year are equally likely (and excluded February 29). In reality, some days are slightly more likely as birthdays than others. For example, scientists have long struggled to understand why more babies are born 9 months after a holiday. Let $\mathbf{p}=(p_{1},p_{2},\ldots,p_{365})$ be the vector of birthday probabilities, with $p_{j}$ the probability of being born on the $j$th day of the year (February 29 is still excluded, with no offense intended to Leap Dayers).

The $k$th *elementary symmetric polynomial* in the variables $x_{1},\ldots,x_{n}$ is defined by

$e_{k}(x_{1},\ldots,x_{n})=\sum_{1\leq j_{1}<j_{2}<\cdots<j_{k}\leq n}x_{j_{1}}\ldots x_{j_{k}}.$

This just says to add up all of the $\binom{n}{k}$ terms we can get by choosing and multiplying $k$ of the variables. For example, $e_{1}(x_{1},x_{2},x_{3})=x_{1}+x_{2}+x_{3}$, $e_{2}(x_{1},x_{2},x_{3})=x_{1}x_{2}+x_{1}x_{3}+x_{2}x_{3}$, and $e_{3}(x_{1},x_{2},x_{3})=x_{1}x_{2}x_{3}$.

Now let $k\geq 2$ be the number of people.

(a) Find a simple expression for the probability that there is at least one birthday match, in terms of $\mathbf{p}$ and an elementary symmetric polynomial.

(b) Explain intuitively why it makes sense that $P(\text{at least one birthday match})$ is minimized when $p_{j}=\frac{1}{365}$ for all $j$, by considering simple and extreme cases.

(c) The famous *arithmetic mean-geometric mean inequality* says that for $x,y\geq 0$,

$\frac{x+y}{2}\geq\sqrt{xy}.$

This inequality follows from adding $4xy$ to both sides of $x^{2}-2xy+y^{2}=(x-y)^{2}\geq 0$.

Define $\mathbf{r}=(r_{1},\ldots,r_{365})$ by $r_{1}=r_{2}=(p_{1}+p_{2})/2$, $r_{j}=p_{j}$ for $3\leq j\leq 365$. Using the arithmetic mean-geometric mean bound and the fact, which you should verify, that

$e_{k}(x_{1},\ldots,x_{n})=x_{1}x_{2}e_{k-2}(x_{3},\ldots,x_{n})+(x_{1}+x_{2})e_{k-1}(x_{3},\ldots,x_{n})+e_{k}(x_{3},\ldots,x_{n}),$

show that

$P(\text{at least one birthday match}|\mathbf{p})\geq P(\text{at least one birthday match}|\mathbf{r}),$

with strict inequality if $\mathbf{p}\neq\mathbf{r}$, where the “given $\mathbf{r}$” notation means that the birthday probabilities are given by $\mathbf{r}$. Using this, show that the value of $\mathbf{p}$ that minimizes the probability of at least one birthday match is given by $p_{j}=\frac{1}{365}$ for all $j$.

##