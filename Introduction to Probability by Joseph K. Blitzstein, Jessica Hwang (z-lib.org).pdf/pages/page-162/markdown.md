(b) Use Stirling’s approximation, which approximates the factorial function as

$n!\approx\sqrt{2\pi n}\left(\frac{n}{e}\right)^{n},$

to find a simple approximation to the probability of a tie. Your answer should be of the form $1/\sqrt{cn}$, with $c$ a constant (which you should specify).
- A message is sent over a noisy channel. The message is a sequence $x_{1},x_{2},\ldots,x_{n}$ of $n$ bits ($x_{i}\in\{0,1\}$). Since the channel is noisy, there is a chance that any bit might be corrupted, resulting in an error (a $0$ becomes a $1$ or vice versa). Assume that the error events are independent. Let $p$ be the probability that an individual bit has an error ($0<p<1/2$). Let $y_{1},y_{2},\ldots,y_{n}$ be the received message (so $y_{i}=x_{i}$ if there is no error in that bit, but $y_{i}=1-x_{i}$ if there is an error there).

To help detect errors, the $n$th bit is reserved for a parity check: $x_{n}$ is defined to be $0$ if $x_{1}+x_{2}+\cdots+x_{n-1}$ is even, and $1$ if $x_{1}+x_{2}+\cdots+x_{n-1}$ is odd. When the message is received, the recipient checks whether $y_{n}$ has the same parity as $y_{1}+y_{2}+\cdots+y_{n-1}$. If the parity is wrong, the recipient knows that at least one error occurred; otherwise, the recipient assumes that there were no errors.

(a) For $n=5,p=0.1$, what is the probability that the received message has errors which go undetected?

(b) For general $n$ and $p$, write down an expression (as a sum) for the probability that the received message has errors which go undetected.

(c) Give a simplified expression, not involving a sum of a large number of terms, for the probability that the received message has errors which go undetected.

Hint for (c): Letting

$a=\sum_{k\text{ even, }k\geq 0}\binom{n}{k}p^{k}(1-p)^{n-k}\text{ and }b=\sum_{k\text{ odd, }k\geq 1}\binom{n}{k}p^{k}(1-p)^{n-k},$

the binomial theorem makes it possible to find simple expressions for $a+b$ and $a-b$, which then makes it possible to obtain $a$ and $b$.

## Independence of r.v.s

- (a) Give an example of dependent r.v.s $X$ and $Y$ such that $P(X<Y)=1$.
- (b) Give an example of independent r.v.s $X$ and $Y$ such that $P(X<Y)=1$.
- Give an example of two discrete random variables $X$ and $Y$ on the same sample space such that $X$ and $Y$ have the same distribution, with support $\{1,2,\ldots,10\}$, but the event $X=Y$ *never* occurs. If $X$ and $Y$ are independent, is it still possible to construct such an example?
- Suppose $X$ and $Y$ are discrete r.v.s such that $P(X=Y)=1$. This means that $X$ and $Y$ always take on the same value.

(a) Do $X$ and $Y$ have the same PMF?

(b) Is it possible for $X$ and $Y$ to be independent?
- If $X,Y,Z$ are r.v.s such that $X$ and $Y$ are independent and $Y$ and $Z$ are independent, does it follow that $X$ and $Z$ are independent?

Hint: Think about simple and extreme examples.