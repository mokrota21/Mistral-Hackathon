Learning any $Y_{i}$ gives information about the other values (so $Y_{1},\ldots,Y_{5}$ are *not* independent, as defined in Section 3.8), but symmetry still holds since, unconditionally, the $j$th slip drawn is equally likely to be any of the slips. This is the *unconditional* distribution of $Y_{j}$: we are working from a vantage point before drawing any of the slips.

For further insight into why each of $Y_{1},\ldots,Y_{5}$ is Discrete Uniform and how to think about $Y_{j}$ unconditionally, imagine that instead of one person drawing five slips, one at a time, there are five people who draw one slip each, all reaching into the hat *simultaneously*, with all possibilities equally likely for who gets which slip. This formulation does not change the problem in any important way, and it helps avoid getting distracted by irrelevant chronological details. Label the five people $1,2,\ldots,5$ in some way, e.g., from youngest to oldest, and let $Z_{j}$ be the value drawn by person $j$. By symmetry, $Z_{j}\sim\text{DUnif}(1,2,\ldots,100)$ for each $j$; the $Z_{j}$’s are dependent but, looked at individually, each person is drawing a uniformly random slip.

(f) The events $Y_{1}=100,\ldots,Y_{5}=100$ are disjoint since we are now sampling without replacement, so

$P(Y_{j}=100\text{ for some }j)=P(Y_{1}=100)+\cdots+P(Y_{5}=100)=0.05.$

*Sanity check*: This answer makes sense intuitively since we can just as well think of first choosing five random slips out of 100 blank slips and then randomly writing the numbers from 1 to 100 on the slips, which gives a 5/100 chance that the number 100 is on one of the five chosen slips.

It would be bizarre if the answer to (c) were greater than or equal to the answer to (f), since sampling without replacement makes it easier to find the number 100. (For the same reason, when searching for a lost possession it makes more sense to sample locations without replacement than with replacement.) But it makes sense that the answer to (c) is only slightly less than the answer to (f), since it is unlikely in (c) that the same slip will be sampled more than once (though by the birthday problem it’s less unlikely than many people would guess).

More generally, if $k$ slips are drawn without replacement, where $0\leq k\leq 100$, then the same reasoning gives that the probability of drawing the number 100 is $k/100$. Note that this makes sense in the extreme case $k=100$, since in that case we draw *all* of the slips. ∎

### 3.6 Cumulative distribution functions

Another function that describes the distribution of an r.v. is the *cumulative distribution function* (CDF). Unlike the PMF, which only discrete r.v.s possess, the CDF is defined for *all* r.v.s.