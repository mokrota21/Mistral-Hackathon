to problems you have studied previously. We will often discuss stories that involve tossing coins or drawing balls from urns because they are simple, convenient scenarios to work with, but many other problems are *isomorphic*: they have the same essential structure, but in a different guise.

To start, let’s consider a coin-tossing example. The structure of the problem is that we have a sequence of trials where there are two possible outcomes for each trial. Here we think of the possible outcomes as $H$ (Heads) and $T$ (Tails), but we could just as well think of them as “success” and “failure” or as 1 and 0, for example.

###### Example 3.1.2 (Coin tosses).

Consider an experiment where we toss a fair coin twice. The sample space consists of four possible outcomes: $S=\{HH,HT,TH,TT\}$. Here are some random variables on this space (for practice, you can think up some of your own). Each r.v. is a numerical summary of some aspect of the experiment.

- Let $X$ be the number of Heads. This is a random variable with possible values 0, 1, and 2. Viewed as a function, $X$ assigns the value 2 to the outcome $HH$, 1 to the outcomes $HT$ and $TH$, and 0 to the outcome $TT$. That is,

$X(HH)=2,X(HT)=X(TH)=1,X(TT)=0.$
- Let $Y$ be the number of Tails. In terms of $X$, we have $Y=2-X$. In other words, $Y$ and $2-X$ are the same r.v.: $Y(s)=2-X(s)$ for all $s$.
- Let $I$ be 1 if the first toss lands Heads and 0 otherwise. Then $I$ assigns the value 1 to the outcomes $HH$ and $HT$ and 0 to the outcomes $TH$ and $TT$. This r.v. is an example of what is called an *indicator random variable* since it indicates whether the first toss lands Heads, using 1 to mean “yes” and 0 to mean “no”.

We can also encode the sample space as $\{(1,1),(1,0),(0,1),(0,0)\}$, where 1 is the code for Heads and 0 is the code for Tails. Then we can give explicit formulas for $X,Y,I$:

$X(s_{1},s_{2})=s_{1}+s_{2},\ Y(s_{1},s_{2})=2-s_{1}-s_{2},\ I(s_{1},s_{2})=s_{1},$

where for simplicity we write $X(s_{1},s_{2})$ to mean $X((s_{1},s_{2}))$, etc.

For most r.v.s we will consider, it is tedious or infeasible to write down an explicit formula in this way. Fortunately, it is usually unnecessary to do so, since (as we saw in this example) there are other ways to define an r.v., and (as we will see throughout the rest of this book) there are many ways to study the properties of an r.v. other than by doing computations with an explicit formula for what it maps each outcome $s$ to. ∎

As in the previous chapters, for a sample space with a finite number of outcomes we can visualize the outcomes as pebbles, with the mass of a pebble corresponding to its probability, such that the total mass of the pebbles is 1. A random variable simply labels each pebble with a number. Figure 3.2 shows two random variables