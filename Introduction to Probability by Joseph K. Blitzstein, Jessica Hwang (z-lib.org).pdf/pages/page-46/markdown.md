1.8 R

R is a very powerful, popular environment for statistical computing and graphics, freely available for Mac OS X, Windows, and UNIX systems. Knowing how to use R is an extremely useful skill. R and various supporting information can be obtained at https://www.r-project.org. RStudio is an excellent alternative interface for R, freely available at https://www.rstudio.com.

In the R section at the end of each chapter, we provide R code to let you try out some of the examples from the chapter, especially via simulation. These sections are not intended to be a full introduction to R; many R tutorials are available for free online, and many books on R are available. But the R sections show how to implement various simulations, computations, and visualizations that naturally accompany the material from each chapter. The R code at the end of each chapter is also available at http://stat110.net.

#### Vectors

R is built around vectors, and getting familiar with “vectorized thinking” is very important for using R effectively. To create a vector, we can use the c command (which stands for combine or concatenate). For example,

```
v <- c(3,1,4,1,5,9)
```

defines v to be the vector $(3,1,4,1,5,9)$. (The left arrow <- is typed as < followed by -. The symbol = can be used instead, but the arrow is more suggestive of the fact that the variable on the left is being set equal to the value on the right.) Similarly, n <- 110 sets $n$ equal to 110; R views $n$ as a vector of length 1.

```
sum(v)
```

adds up the entries of v, max(v) gives the largest value, min(v) gives the smallest value, and length(v) gives the length.

A shortcut for getting the vector $(1,2,\ldots,n)$ is to type 1:n; more generally, if $m$ and $n$ are integers then m:n gives the sequence of integers from $m$ to $n$ (in increasing order if $m\leq n$ and in decreasing order otherwise).

To access the $i$th entry of a vector v, use v[i]. We can also get subvectors easily:

```
v[c(1,3,5)]
```

gives the vector consisting of the 1st, 3rd, and 5th entries of v. It’s also possible to get a subvector by specifying what to exclude, using a minus sign:

```
v[-(2:4)]