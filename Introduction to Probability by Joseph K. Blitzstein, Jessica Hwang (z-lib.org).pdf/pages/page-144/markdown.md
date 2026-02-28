Random variables and their distributions

|  s | X | Y | max(X,Y)  |
| --- | --- | --- | --- |
|  (1,2) | 1 | 2 | 2  |
|  (1,6) | 1 | 6 | 6  |
|  (2,5) | 2 | 5 | 5  |
|  (3,1) | 3 | 1 | 3  |
|  (4,3) | 4 | 3 | 4  |
|  (5,4) | 5 | 4 | 5  |
|  (6,6) | 6 | 6 | 6  |

So  $\max(X, Y)$  assigns a numerical value to each sample outcome. The PMF is

$P(\max (X,Y) = 1) = 1 / 36,$

$P(\max (X,Y) = 2) = 3 / 36,$

$P(\max (X,Y) = 3) = 5 / 36,$

$P(\max (X,Y) = 4) = 7 / 36,$

$P(\max (X,Y) = 5) = 9 / 36,$

$P(\max (X,Y) = 6) = 11 / 36.$

These probabilities can be obtained by tabulating the values of  $\max(x, y)$  in a  $6 \times 6$  grid and counting how many times each value appears in the grid, or with calculations such as

$P(\max (X,Y) = 5) = P(X = 5,Y\leq 4) + P(X\leq 4,Y = 5) + P(X = 5,Y = 5)$

$= 2P(X = 5,Y\leq 4) + 1 / 36$

$= 2(4 / 36) + 1 / 36 = 9 / 36.$

$\star$  3.7.7 (Category errors and sympathetic magic). Many common mistakes in probability can be traced to confusing two of the following fundamental objects with each other: distributions, random variables, events, and numbers. Such mistakes are examples of category errors. In general, a category error is a mistake that doesn't just happen to be wrong, but in fact is necessarily wrong since it is based on the wrong category of object. For example, answering the question "How many people live in Boston?" with "-42" or "π" or "pink elephants" would be a category error—we may not know the population size of a city, but we do know that it is a nonnegative integer at any point in time. To help avoid being categorically wrong, always think about what category an answer should have.

An especially common category error is to confuse a random variable with its distribution. We call this error sympathetic magic; this term comes from anthropology, where it is used for the belief that one can influence an object by manipulating a representation of that object. The following saying sheds light on the distinction between a random variable and its distribution:

The word is not the thing; the map is not the territory. - Alfred Korzybski