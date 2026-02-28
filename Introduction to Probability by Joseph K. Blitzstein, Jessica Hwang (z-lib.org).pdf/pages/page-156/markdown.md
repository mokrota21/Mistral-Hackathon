We can also evaluate PMFs and CDFs at an entire vector of values. For example, recall that 0:n is a quick way to list the integers from 0 to $n$. The command dbinom(0:5,5,0.2) returns 6 numbers, $P(X=0),P(X=1),\ldots,P(X=5)$, where $X\sim\text{Bin}(5,0.2)$.

#### Hypergeometric distribution

The Hypergeometric distribution also has three functions: dhyper, phyper, and rhyper. As one might expect, dhyper is the Hypergeometric PMF, phyper is the Hypergeometric CDF, and rhyper generates Hypergeometric r.v.s. Since the Hypergeometric distribution has three parameters, each of these functions takes four inputs. For dhyper and phyper, the first input is the value at which we wish to evaluate the PMF or CDF, and the remaining inputs are the parameters of the distribution.

Thus dhyper(k,w,b,n) returns $P(X=k)$ where $X\sim\text{HGeom}(w,b,n)$, and phyper(k,w,b,n) returns $P(X\leq k)$. For rhyper, the first input is the number of r.v.s we want to generate, and the remaining inputs are the parameters; rhyper(100,w,b,n) generates 100 i.i.d. HGeom$(w,b,n)$ r.v.s.

#### Discrete distributions with finite support

We can generate r.v.s from any discrete distribution with finite support using the sample command. When we first introduced the sample command, we said that it can be used in the form sample(n,k) or sample(n,k,replace=TRUE) to sample $k$ times from the integers 1 through $n$, either without or with replacement. For example, to generate 5 independent DUnif$(1,2,\ldots,100)$ r.v.s, we can use the command sample(100,5,replace=TRUE).

It turns out that sample is far more versatile. If we want to sample from the values $x_{1},\ldots,x_{n}$ with probabilities $p_{1},\ldots,p_{n}$, we simply create a vector x containing all the $x_{i}$ and a vector p containing all the $p_{i}$, then feed them into sample. Suppose we want realizations of i.i.d. r.v.s $X_{1},\ldots,X_{100}$ whose PMF is

$P(X_{j}=0)=0.25,$
$P(X_{j}=1)=0.5,$
$P(X_{j}=5)=0.1,$
$P(X_{j}=10)=0.15,$

and $P(X_{j}=x)=0$ for all other values of $x$. First, we use the c function to create vectors with the support of the distribution and the corresponding probabilities.

```
x <- c(0,1,5,10)
p <- c(0.25,0.5,0.1,0.15)