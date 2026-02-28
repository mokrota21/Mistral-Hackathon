Probability and counting

4. Let $D$ be the event that there were at least two consecutive Heads. As a set,

$D=\bigcup_{j=1}^{9}(A_{j}\cap A_{j+1}).\qed$

###### Example 1.2.3 (Pick a card, any card).

Pick a card from a standard deck of 52 cards. The sample space $S$ is the set of all 52 cards (so there are 52 pebbles, one for each card). Consider the following four events:

- $A$: card is an ace.
- $B$: card has a black suit.
- $D$: card is a diamond.
- $H$: card is a heart.

As a set, $H$ consists of 13 cards:

$\{\mbox{Ace of Hearts, Two of Hearts,}\dots\mbox{, King of Hearts}\}.$

We can create various other events in terms of the events $A,B,D$, and $H$. Unions, intersections, and complements are especially useful for this. For example:

- $A\cap H$ is the event that the card is the Ace of Hearts.
- $A\cap B$ is the event $\{\mbox{Ace of Spades, Ace of Clubs}\}$.
- $A\cup D\cup H$ is the event that the card is red or an ace.
- $(A\cup B)^{c}=A^{c}\cap B^{c}$ is the event that the card is a red non-ace.

Also, note that $(D\cup H)^{c}=D^{c}\cap H^{c}=B$, so $B$ can be expressed in terms of $D$ and $H$. On the other hand, the event that the card is a spade can’t be written in terms of $A,B,D,H$ since none of them are fine-grained enough to be able to distinguish between spades and clubs.

There are *many* other events that could be defined using this sample space. In fact, the counting methods introduced later in this chapter show that there are $2^{52}\approx 4.5\times 10^{15}$ events in this problem, even though there are only 52 pebbles.

What if the card drawn were a joker? That would indicate that we had the wrong sample space; we are assuming that the outcome of the experiment is guaranteed to be an element of $S$. ∎

As the preceding examples demonstrate, events can be described in English or in set notation. Sometimes the English description is easier to interpret while the set notation is easier to manipulate. Let $S$ be a sample space and $s_{\mathrm{actual}}$ be the actual outcome of the experiment (the pebble that ends up getting chosen when the experiment is performed). A mini-dictionary for converting between English and sets is given on the next page.