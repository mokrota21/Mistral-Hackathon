Random variables and their distributions

###### Example 3.8.12 (Matching pennies).

Consider the simple game called *matching pennies*. Each of two players, A and B, has a fair penny. They flip their pennies independently. If the pennies match, A wins; otherwise, B wins. Let $X$ be 1 if A’s penny lands Heads and $-1$ otherwise, and define $Y$ similarly for B (the r.v.s $X$ and $Y$ are called *random signs*).

Let $Z=XY$, which is 1 if A wins and $-1$ if B wins. Then $X$ and $Y$ are unconditionally independent, but given $Z=1$, we know that $X=Y$ (the pennies match). So $X$ and $Y$ are conditionally dependent given $Z$. ∎

###### Example 3.8.13 (Two friends).

Consider again the “I have only two friends who ever call me” scenario from Example 2.5.11, except now with r.v. notation. Let $X$ be the indicator of Alice calling me next Friday, $Y$ be the indicator of Bob calling me next Friday, and $Z$ be the indicator of exactly one of them calling me next Friday. Then $X$ and $Y$ are independent (by assumption). But given $Z=1$, we have that $X$ and $Y$ are completely dependent: given that $Z=1$, we have $Y=1-X$. ∎

Next let’s see why conditional independence does not imply independence.

###### Example 3.8.14 (Mystery opponent).

Suppose that you are going to play two games of tennis against one of two identical twins. Against one of the twins, you are evenly matched, and against the other you have a $3/4$ chance of winning. Suppose that you can’t tell which twin you are playing against until after the two games. Let $Z$ be the indicator of playing against the twin with whom you’re evenly matched, and let $X$ and $Y$ be the indicators of victory in the first and second games, respectively.

Conditional on $Z=1$, $X$ and $Y$ are i.i.d. Bern(1/2), and conditional on $Z=0$, $X$ and $Y$ are i.i.d. Bern(3/4). So $X$ and $Y$ are conditionally independent given $Z$. Unconditionally, $X$ and $Y$ are dependent because observing $X=1$ makes it more likely that we are playing the twin who is worse. That is,

$P(Y=1|X=1)&gt;P(Y=1).$

Past games give us information which helps us infer who our opponent is, which in turn helps us predict future games! Note that this example is isomorphic to the “random coin” scenario from Example 2.3.7. ∎

### 3.9 Connections between Binomial and Hypergeometric

The Binomial and Hypergeometric distributions are connected in two important ways. As we will see in this section, we can get from the Binomial to the Hypergeometric by *conditioning*, and we can get from the Hypergeometric to the Binomial by *taking a limit*. We’ll start with a motivating example.

###### Example 3.9.1 (Fisher exact test).

A scientist wishes to study whether women or